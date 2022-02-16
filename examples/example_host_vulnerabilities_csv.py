#!/usr/bin/env python3

from laceworksdk import LaceworkClient
from datetime import datetime, timedelta
import csv
import json

# setup lacework cli (~/.lacework.toml)
lw = LaceworkClient(profile="verato")

start_time_dt = datetime.now() + timedelta(days=-1)
end_time_dt = datetime.now()
start_time = start_time_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = end_time_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

machine_start_time_dt = datetime.now() + timedelta(days=-1)
machine_end_time_dt = datetime.now()
machine_start_time = start_time_dt.strftime("%Y-%m-%dT00:00:00Z")
machine_end_time = end_time_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

query = {
    "timeFilters": {
        "startTime": start_time,
        "endTime": end_time
    },
    "filters": [
        {"field": "status", "expression": "in", "values": ["New", "Active"]},
        {"field": "severity", "expression": "in", "values": ["Critical", "High", "Medium"]},
        {"field": "fixInfo.fix_available", "expression": "eq", "value": 1}
    ],
    "returns": [
        "startTime",
        "endTime",
        "severity",
        "status",
        "vulnId",
        "mid",
        "featureKey",
        "machineTags",
        "fixInfo",
        "cveProps"
    ]
}

print("Query: {0}".format(json.dumps(query, indent=4)))

# build a machine dictionary for handy things like hostname
machine_query = {
    "timeFilter": {
        "startTime": machine_start_time,
        "endTime": machine_end_time
    },
    "returns": [
        "startTime",
        "endTime",
        "mid",
        "hostname",
        "primaryIpAddr"
    ]
}

# build machine dictionary
results = lw.entities.machines.search(json=machine_query)
machines = []
for h in results:
    machines += h['data']

with open('host_vulnerability_summary.csv', 'w') as f:
    header = False
    write = csv.writer(f, quoting=csv.QUOTE_ALL)

    host_vulns = lw.vulnerabilities.hosts.search(json=query)

    for h in host_vulns:
        for d in h['data']:
            # create the data row
            try:
                # lookup machine based on id
                machine_details = list(filter(lambda x: x["mid"] == d['mid'], machines))
                if len(machine_details) < 1:
                    print("WARN: Failed to find machine details for mid: {0}".format(d['mid']))
                    print("Using machine tags for hostname and IP")
                    machine_details = [
                        {
                            "hostname": d['machineTags']['Hostname'],
                            "primaryIpAddr": d['machineTags']['InternalIp']
                        }
                    ]
                row = {
                    "startTime": d['startTime'],
                    "endTime": d['endTime'],
                    "cve_id": d['vulnId'],
                    "mid": d['mid'],
                    "hostname": machine_details[0]['hostname'] if len(machine_details) > 0 else None,
                    "primaryIpAddr": machine_details[0]['primaryIpAddr'] if len(machine_details) > 0 else None,
                    "package_name": d['featureKey']['name'],
                    "package_namespace": d['featureKey']['namespace'],
                    "package_active": d['featureKey']['package_active'],
                    "package_status": d['fixInfo']['eval_status'],
                    "version": d['featureKey']['version_installed'],
                    "fix_available": d['fixInfo']['fix_available'],
                    "fixed_version": d['fixInfo']['fixed_version'],
                    "severity": d['severity'],
                    "description": d['cveProps']['description'] if 'cveProps' in d.keys() else None,
                    "cve_link": d['cveProps']['link'] if 'cveProps' in d.keys() else None,
                    "status": d['status'],
                    "tags": d['machineTags']
                }
            except Exception as e:
                print(d)
                raise Exception(e)

            if not header:
                write.writerow(row.keys())
                header = True

            write.writerow(row.values())
