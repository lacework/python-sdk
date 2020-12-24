# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import logging
import os

import laceworksdk
import pytest

from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

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
def subaccount():
    return os.getenv("LW_SUBACCOUNT")


@pytest.fixture(scope="session")
def api_old(account, subaccount, api_key, api_secret):
    return laceworksdk.LaceworkClient(instance=account,
                                      subaccount=subaccount,
                                      api_key=api_key,
                                      api_secret=api_secret)


@pytest.fixture(scope="session")
def api(account, subaccount, api_key, api_secret):
    return laceworksdk.LaceworkClient(account=account,
                                      subaccount=subaccount,
                                      api_key=api_key,
                                      api_secret=api_secret)


@pytest.fixture(scope="session")
def api_env():
    return laceworksdk.LaceworkClient()
