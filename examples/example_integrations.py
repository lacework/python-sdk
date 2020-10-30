# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import os
import random

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Use enviroment variables to instantiate a LaceworkClient instance
    lacework_client = LaceworkClient(api_key=os.getenv("LW_API_KEY"),
                                     api_secret=os.getenv("LW_API_SECRET"),
                                     account=os.getenv("LW_ACCOUNT"))

    # Integration API

    # Get all Integrations
    integrations = lacework_client.integrations.get_all()

    # Get Integration by ID
    integration_by_id = lacework_client.integrations.get_by_id(random.choice(integrations["data"])["INTG_GUID"])

    # Get Integration Schema by Type
    lacework_client.integrations.get_schema(integration_by_id["data"][0]["TYPE"])
