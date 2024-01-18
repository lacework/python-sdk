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

    # Agent Access Token API

    # Get all Agent Access Tokens
    agent_api_tokens = lacework_client.agent_access_tokens.get()

    # Get specified Agent Access Token
    api_token = lacework_client.agent_access_tokens.get_by_id(random.choice(agent_api_tokens["data"])["accessToken"])
