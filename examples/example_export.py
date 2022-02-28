# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import csv
import logging
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.INFO)

load_dotenv()

ISO_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class ReferenceLookup:
    def __init__(self, key, field, dict, multivalue=False):
        self.key = key
        self.field = field
        self.dict = dict
        self.multivalue = multivalue

    def lookup(self, value, default=None):
        # only return the first matching result or default value
        dict = list(filter(lambda x: x[self.key] == value, self.dict))

        rows = []
        for row in dict:
            # return the entire row
            if self.field is None:
                rows.append(row)
            else:
                for i in self.field.split("."):
                    if i in row:
                        row = row[i]
                    else:
                        row = default
                    rows.append(row)

        # return all multiple values
        if self.multivalue:
            return rows

        # return first value only
        else:
            return rows.pop() if len(rows) > 0 else default


class DataHandler:
    def __init__(self, format, file_path="export.csv"):
        if format not in ["csv", "dict"]:
            raise Exception(
                f"Unsupported export format, expected csv or dict found: {format}"
            )

        self.format = format
        self.file_path = file_path

    def __open(self):
        if self.format == "csv":
            self.header = False
            self.fp = open(self.file_path, "w")
            self.writer = csv.writer(self.fp, quoting=csv.QUOTE_ALL)
            self.dataset = csv.reader(self.fp)
        else:
            self.dataset = []

    def __close(self):
        if self.format == "csv":
            self.fp.close()

    def insert(self, row):
        if self.format == "csv":
            if not self.header:
                self.writer.writerow(row.keys())
                self.header = True

            self.writer.writerow(row.values())
        elif self.format == "dict":
            self.dataset.append(row)

    def get(self):
        return self.dataset

    def __enter__(self):
        self.__open()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__close()


def query(
    client,
    type,
    object,
    start_time=None,
    end_time=None,
    filters=None,
    returns=None,
):

    if start_time is None:
        start_time = datetime.now(timezone.utc) + timedelta(days=-1)
    if end_time is None:
        end_time = datetime.now(timezone.utc)
    if filters is None:
        filters = []

    # build query string
    q = {
        "timeFilter": {
            "startTime": start_time.strftime(ISO_FORMAT),
            "endTime": end_time.strftime(ISO_FORMAT),
        },
        "filters": filters,
        "returns": returns,
    }

    # create reference to search object
    obj = getattr(getattr(client, f"{type}"), f"{object}")

    # return query result reference
    return obj.search(json=q)


def lookup(key, dict, default=None):
    for i in key.split("."):
        if i in dict:
            dict = dict[i]
        else:
            return default

    return dict


def flatten_json(y):
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + "_")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def map_fields(data, field_map=None):
    if field_map is None:
        # flatten json
        data = flatten_json(data)
        field_map = {}
        for key in data.keys():
            field_map[key] = key

    result = {}
    for field in field_map.keys():
        # for reference field find the matching local key and lookup the field value
        if isinstance(field_map[field], ReferenceLookup):
            result[field] = field_map[field].lookup(lookup(field_map[field].key, data))
        else:
            result[field] = lookup(field_map[field], data)

    return result


def export(format, results, field_map=None, file_path="export.csv"):
    with DataHandler(format, file_path=file_path) as h:
        # process results
        for result in results:
            for data in result["data"]:
                # create the data row
                try:
                    row = map_fields(data=data, field_map=field_map)
                except Exception as e:
                    logging.error(f"Failed to map fields for data: {data}")
                    raise Exception(e)

                h.insert(row)

        # return
        return h.get()


if __name__ == "__main__":

    client = LaceworkClient()

    # # scenario 1 - export a list of machines to csv
    # export(
    #     "csv",
    #     query(client=client, type="entities", object="machines"),
    #     field_map={
    #         "start_time": "startTime",
    #         "end_time": "endTime",
    #         "mid": "mid",
    #         "tags": "machineTags",
    #         "hostname": "hostname",
    #         "public_ip": "machineTags.ExternalIp",
    #     },
    #     file_path="export_machines.csv",
    # )

    # # scenario 2 - export a list of containers to csv
    # export(
    #     "csv",
    #     query(
    #         client=client,
    #         type="entities",
    #         object="containers",
    #         returns=[
    #             "startTime",
    #             "endTime",
    #             "imageId",
    #             "podName",
    #             "containerName",
    #             "propsContainer",
    #         ],
    #     ),
    #     field_map={
    #         "start_time": "startTime",
    #         "image_id": "imageId",
    #         "pod_name": "podName",
    #         "container_name": "containerName",
    #         "props": "propsContainer",
    #     },
    #     file_path="export_containers.csv",
    # )

    # # scenario 3 - export a list of host vulnerabilities and lookup machine details
    # # create a machine mapping reference to be used in "join"
    # machines = export(
    #     "dict",
    #     query(
    #         client=client,
    #         type="entities",
    #         object="machines",
    #         returns=["mid", "hostname", "primaryIpAddr"],
    #     ),
    # )

    # export(
    #     "csv",
    #     query(
    #         client=client,
    #         type="vulnerabilities",
    #         object="hosts",
    #         filters=[
    #             {"field": "status", "expression": "in", "values": ["New", "Active"]},
    #             {
    #                 "field": "severity",
    #                 "expression": "in",
    #                 "values": ["Critical", "High", "Medium"],
    #             },
    #             {"field": "fixInfo.fix_available", "expression": "eq", "value": 1},
    #         ],
    #         returns=[
    #             "startTime",
    #             "endTime",
    #             "severity",
    #             "status",
    #             "vulnId",
    #             "mid",
    #             "featureKey",
    #             "machineTags",
    #             "fixInfo",
    #             "cveProps",
    #         ],
    #     ),
    #     field_map={
    #         "start_time": "startTime",
    #         "end_time": "endTime",
    #         "mid": "mid",
    #         "cve_id": "vulnId",
    #         # lookup hostname by mid and return first result
    #         "hostname": ReferenceLookup("mid", "hostname", machines),
    #         "package_name": "featureKey.name",
    #         "package_namespace": "featureKey.namespace",
    #         "package_active": "featureKey.package_active",
    #         "package_status": "fixInfo.eval_status",
    #         "version": "featureKey.version_installed",
    #         "fix_available": "fixInfo.fix_available",
    #         "fixed_version": "fixInfo.fixed_version",
    #         "severity": "severity",
    #         "tags": "machineTags",
    #         "status": "status",
    #     },
    #     file_path="export_host_vulnerabilities.csv",
    # )

    # scenario 4 - export a list of image vulnerabilities and lookup active container details
    # create a container mapping reference to be used in "join"
    containers = export(
        "dict",
        query(
            client=client,
            type="entities",
            object="containers",
            returns=[
                "imageId",
                "podName",
                # "containerName",
                # "propsContainer"
            ],
        ),
    )

    # unique image_ids
    image_ids = list(set([d["imageId"] for d in containers if "imageId" in d.keys()]))
    logging.info("Found {0} active imageIds".format(len(image_ids)))

    logging.info("Starting export of container vulnerabilities for active images...")
    export(
        "csv",
        query(
            client=client,
            type="vulnerabilities",
            object="containers",
            filters=[
                {
                    "field": "severity",
                    "expression": "in",
                    "values": ["Critical", "High", "Medium"],
                },
                {"field": "imageId", "expression": "in", "values": image_ids},
                {"field": "status", "expression": "in", "values": ["VULNERABLE"]},
                {"field": "fixInfo.fix_available", "expression": "eq", "value": 1},
            ],
            returns=[
                "startTime",
                "imageId",
                "severity",
                "status",
                "vulnId",
                "evalCtx",
                "fixInfo",
                "featureKey",
            ],
        ),
        field_map={
            "start_time": "startTime",
            "image_id": "imageId",
            "cve_id": "vulnId",
            # lookup all active containers matching image id and return all properties
            "containers": ReferenceLookup("imageId", None, containers, multivalue=True),
            "image_registry": "evalCtx.image_info.registry",
            "image_repo": "evalCtx.image_info.repo",
            "image_status": "evalCtx.image_info.status",
            "package_name": "featureKey.name",
            "package_namespace": "featureKey.namespace",
            "version": "featureKey.version",
            "fix_available": "fixInfo.fix_available",
            "fixed_version": "fixInfo.fixed_version",
            "severity": "severity",
            "status": "status",
        },
        file_path="export_container_vulnerabilities.csv",
    )
