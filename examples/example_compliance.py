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
    lacework_client = LaceworkClient(api_key=os.getenv("LACEWORK_API_KEY"),
                                     api_secret=os.getenv("LACEWORK_API_SECRET"),
                                     instance=os.getenv("LACEWORK_INSTANCE"))

    # Compliance API

    # Get latest compliance report in JSON format for AWS account
    lacework_client.compliance.get_latest_aws_report("123456789")

    # Get a list of subscriptions for an Azure Tenant
    lacework_client.compliance.list_azure_subscriptions("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
