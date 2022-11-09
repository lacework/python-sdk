# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import random

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

    # Alerts API

    # Get alerts for specified time range
    alerts = lacework_client.alerts.get(start_time=start_time, end_time=end_time)

    # Get alert details for specified ID
    alert_details = lacework_client.alerts.get_details(random.choice(alerts["data"])["alertId"])
