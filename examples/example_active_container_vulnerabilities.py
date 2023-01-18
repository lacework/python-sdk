# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Build start/end times
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=1)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # Entities API

    # Get active image IDs
    active_containers = lacework_client.entities.containers.search(
        start_time=start_time,
        end_time=end_time,
        json={
            "returns": [
                "imageId"
            ]
        }
    )

    image_ids = set()
    for page in active_containers:
        for item in page["data"]:
            image_ids.add(item["imageId"])

    # Vulnerabilities API

    active_container_vulns = lacework_client.vulnerabilities.containers.search(
        start_time=start_time,
        end_time=end_time,
        json={
            "filters": [
                {
                    "field": "imageId",
                    "expression": "in",
                    "values": list(image_ids)
                },
                {
                    "field": "severity",
                    "expression": "in",
                    "values": [
                        "Critical",
                        "High"
                    ]
                },
                {
                    "field": "status",
                    "expression": "eq",
                    "value": "VULNERABLE"
                },
                {
                    "field": "fixInfo.fix_available",
                    "expression": "eq",
                    "value": 1
                }
            ]
        }
    )

    for page in active_container_vulns:
        # Do something way more interesting with the fixable Critical and High sev
        # vulnerabilities for containers that were active in the past 24 hours here...
        print(page["paging"]["totalRows"])
        exit()
