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
    return os.getenv("LW_API_KEY")


@pytest.fixture(scope="session")
def api_secret():
    return os.getenv("LW_API_SECRET")


@pytest.fixture(scope="session")
def account():
    return os.getenv("LW_ACCOUNT")


@pytest.fixture(scope="session")
def api_old(api_key, api_secret, account):
    return laceworksdk.LaceworkClient(api_key=api_key,
                                      api_secret=api_secret,
                                      instance=account)


@pytest.fixture(scope="session")
def api(account, api_key, api_secret):
    return laceworksdk.LaceworkClient(account=account,
                                      api_key=api_key,
                                      api_secret=api_secret)


@pytest.fixture(scope="session")
def api_env():
    return laceworksdk.LaceworkClient()
