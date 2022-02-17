#!/usr/bin/env python3

import csv
import json

from datetime import datetime, timedelta

from laceworksdk import LaceworkClient

# setup lacework cli (~/.lacework.toml)
lw = LaceworkClient()

start_time_dt = datetime.now() + timedelta(days=-1)
end_time_dt = datetime.now()
start_time = start_time_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = end_time_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

query = {
    "timeFilters": {
        "startTime": start_time,
        "endTime": end_time
    },
    "filters": [
        {"field": "severity", "expression": "in", "values": ["Critical", "High", "Medium"]},
        {"field": "status", "expression": "in", "values": ["VULNERABLE"]},
        {"field": "fixInfo.fix_available", "expression": "eq", "value": 1}
    ],
    "returns": [
        "startTime",
        "imageId",
        "severity",
        "status",
        "vulnId",
        "evalCtx",
        "fixInfo",
        "featureKey"
    ]
}

print("Query: {0}".format(json.dumps(query, indent=4)))

with open('container_vulnerability_summary.csv', 'w') as f:
    header = False
    write = csv.writer(f, quoting=csv.QUOTE_ALL)

    container_vulns = lw.vulnerabilities.containers.search(json=query)

    for h in container_vulns:
        for d in h['data']:
            # create the data row
            try:
                row = {
                    "startTime": d['startTime'],
                    "imageId": d['imageId'],
                    "cve_id": d.get('vulnId'),
                    "package_name": d['featureKey']['name'],
                    "package_namespace": d['featureKey']['namespace'],
                    "version": d['featureKey']['version'],
                    "fix_available": d['fixInfo']['fix_available'],
                    "fixed_version": d['fixInfo']['fixed_version'],
                    "severity": d['severity'],
                    "status": d['status'],
                    "image_created_time": d['evalCtx']['image_info'].get('created_time'),
                    "image_digest": d['evalCtx']['image_info']['digest'],
                    "image_error_msg": d['evalCtx']['image_info']['error_msg'],
                    "image_registry": d['evalCtx']['image_info']['registry'],
                    "image_repo": d['evalCtx']['image_info']['repo'],
                    "image_size": d['evalCtx']['image_info']['created_time'],
                    "image_type": d['evalCtx']['image_info']['type'],
                    "scan_status": d['evalCtx']['image_info']['status'],
                    "scan_start_time": d['evalCtx']['scan_request_props']['scan_start_time'],
                    "scan_complete_time": d['evalCtx']['scan_request_props']['scanCompletionUtcTime'],
                    "vuln_created_time": d['evalCtx']['vuln_created_time'],
                    "tags": d['evalCtx']['image_info']['tags']
                }
            except Exception as e:
                print(d)
                raise Exception(e)

            if not header:
                write.writerow(row.keys())
                header = True

            write.writerow(row.values())
