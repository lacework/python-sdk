# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import os

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Use enviroment variables to instantiate a LaceworkClient instance
    lacework_client = LaceworkClient(api_key=os.getenv("LW_API_KEY"),
                                     api_secret=os.getenv("LW_API_SECRET"),
                                     account=os.getenv("LW_ACCOUNT"))

    # Alert Channels API

    # Get Alert Channels
    lacework_client.alert_channels.get()

    # Search Alert Channels
    lacework_client.alert_channels.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "type",
                "value": "SlackChannel"
            }
        ],
        "returns": [
            "intgGuid"
        ]
    })
