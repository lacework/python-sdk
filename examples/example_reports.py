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

    # Reports API

    # Get latest compliance report in JSON format for AWS account
    lacework_client.reports.get(
        primary_query_id="123456798012", format="json", report_type="AWS_CIS_14"
    )
