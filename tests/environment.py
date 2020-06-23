# -*- coding: utf-8 -*-
"""
Test environment variables.
"""

import os

from dotenv import load_dotenv

load_dotenv()


LACEWORK_API_KEY = os.getenv("LACEWORK_API_KEY")
if LACEWORK_API_KEY is None:
    raise RuntimeError(
        f"You must set the 'LACEWORK_API_KEY' environment variable to run the test suite"
    )

LACEWORK_API_SECRET = os.getenv("LACEWORK_API_SECRET")
if LACEWORK_API_SECRET is None:
    raise RuntimeError(
        f"You must set the 'LACEWORK_API_SECRET' environment variable to run the test suite"
    )

LACEWORK_INSTANCE = os.getenv("LACEWORK_INSTANCE")
if LACEWORK_API_KEY is None:
    raise RuntimeError(
        f"You must set the 'LACEWORK_API_KEY' environment variable to run the test suite"
    )
