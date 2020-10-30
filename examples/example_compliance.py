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

    # Compliance API

    # Get latest compliance report in JSON format for AWS account
    lacework_client.compliance.get_latest_aws_report(aws_account_id="123456789", file_format="json")

    # Get latest compliance report in PDF format for AWS account
    lacework_client.compliance.get_latest_aws_report(aws_account_id="123456789", file_format="pdf", pdf_path='<PATH_TO_PDF_OUTPUT>')

    # Get a list of subscriptions for an Azure Tenant
    lacework_client.compliance.list_azure_subscriptions("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
