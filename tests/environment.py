# -*- coding: utf-8 -*-
"""
Test environment variables.
"""

import os

from dotenv import load_dotenv

load_dotenv()


LW_ACCOUNT = os.getenv("LW_ACCOUNT")
if LW_ACCOUNT is None:
    raise RuntimeError(
        "You must set the 'LW_ACCOUNT' environment variable to run the test suite"
    )

LW_API_KEY = os.getenv("LW_API_KEY")
if LW_API_KEY is None:
    raise RuntimeError(
        "You must set the 'LW_API_KEY' environment variable to run the test suite"
    )

LW_API_SECRET = os.getenv("LW_API_SECRET")
if LW_API_SECRET is None:
    raise RuntimeError(
        "You must set the 'LW_API_SECRET' environment variable to run the test suite"
    )
