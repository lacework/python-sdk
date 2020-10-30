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

    # Token API

    # Get all enabled API tokens
    enabled_api_tokens = lacework_client.tokens.get_enabled()

    # Get specified API token
    api_token = lacework_client.tokens.get_token(random.choice(enabled_api_tokens["data"])["ACCESS_TOKEN"])
