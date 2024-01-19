# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import random

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Cloud Accounts API

    # Get all Cloud Accounts
    integrations = lacework_client.cloud_accounts.get()

    cloud_account_guid = random.choice(integrations["data"])["intgGuid"]
    print(cloud_account_guid)

    # Get Cloud Account by ID
    integration_by_id = lacework_client.cloud_accounts.get_by_guid(cloud_account_guid)
    print(integration_by_id)
