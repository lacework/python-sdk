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
    lacework_client = LaceworkClient(api_key=os.getenv("LACEWORK_API_KEY"),
                                     api_secret=os.getenv("LACEWORK_API_SECRET"),
                                     instance=os.getenv("LACEWORK_INSTANCE"))

    # Custom Compliance Config API

    # Get Custom Compliance Config
    lacework_client.compliance.config.get()
