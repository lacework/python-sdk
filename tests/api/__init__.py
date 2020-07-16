# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import os

import laceworksdk
import pytest

from dotenv import load_dotenv

load_dotenv()


# Fixtures

@pytest.fixture(scope="session")
def api_key():
    return os.getenv("LACEWORK_API_KEY")


@pytest.fixture(scope="session")
def api_secret():
    return os.getenv("LACEWORK_API_SECRET")


@pytest.fixture(scope="session")
def instance():
    return os.getenv("LACEWORK_INSTANCE")


@pytest.fixture(scope="session")
def api(api_key, api_secret, instance):
    return laceworksdk.LaceworkClient(api_key=api_key,
                                      api_secret=api_secret,
                                      instance=instance)
