"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import os
import random

#from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

#load_dotenv()

if __name__ == "__main__":

    # Use enviroment variables to instantiate a LaceworkClient instance
    lacework_client = LaceworkClient(api_key=os.getenv("LACEWORK_API_KEY"),
                                     api_secret=os.getenv("LACEWORK_API_SECRET"),
                                     instance=os.getenv("LACEWORK_INSTANCE"))

    # Run Report API

    # Run compliance report on an AWS Account
    lacework_client.runreports.run_aws_report(aws_account_id="123456789")

    # Run compliance report on an Azure Tenant Account
    lacework_client.runreports.run_azure_report(azure_tenant_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")


    # Run compliance report on a GCP Project

    lacework_client.runreports.run_gcp_report(gcp_project_id="example-project-id")

    