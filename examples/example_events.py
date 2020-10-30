# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import os
import random

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Use enviroment variables to instantiate a LaceworkClient instance
    lacework_client = LaceworkClient(api_key=os.getenv("LW_API_KEY"),
                                     api_secret=os.getenv("LW_API_SECRET"),
                                     account=os.getenv("LW_ACCOUNT"))

    # Build start/end times
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=1)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # Event API

    # Get events for specified time range
    events = lacework_client.events.get_for_date_range(start_time=start_time, end_time=end_time)

    # Get event details for specified ID
    event_details = lacework_client.events.get_details(random.choice(events["data"])["EVENT_ID"])
