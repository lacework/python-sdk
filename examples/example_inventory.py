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

    # Inventory API

    # Scan each CSP (cloud service provider)

    for csp in ["AWS", "GCP", "Azure"]:
        inventory_scan = lacework_client.inventory.scan(csp=csp)

        inventory_scan_status = lacework_client.inventory.status(csp=csp)
