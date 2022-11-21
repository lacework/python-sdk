# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Alert Channels API

    # Get Alert Channels
    lacework_client.alert_channels.get()

    # Search Alert Channels
    lacework_client.alert_channels.search(json={
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
