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
    start_time = current_time - timedelta(days=7)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Cloud Activities API

    # Get Cloud Activities
    lacework_client.cloud_activities.get()

    # Get Cloud Activities by date range
    lacework_client.cloud_activities.get(start_time=start_time, end_time=end_time)

    # Search Cloud Activities
    lacework_client.cloud_activities.search(json={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters": [
            {
                "expression": "eq",
                "field": "eventModel",
                "value": "CloudTrailCep"
            }
        ],
        "returns": [
            "eventType",
            "eventActor"
        ]
    })
