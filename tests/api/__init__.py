# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import logging
import os
import random
import string

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


@pytest.fixture(scope="session")
def random_text():
    return "".join(random.choice(string.ascii_uppercase) for _ in range(8))


@pytest.fixture(scope="session")
def email_alert_channel_guid(api):
    response = api.alert_channels.search(
        json={
            "filters": [
                {
                    "expression": "eq",
                    "field": "type",
                    "value": "EmailUser"
                }
            ],
            "returns": [
                "intgGuid"
            ]
        }
    )
    alert_channel_guid = response["data"][0]["intgGuid"]
    return alert_channel_guid


@pytest.fixture(scope="session")
def aws_resource_group_guid(api):
    response = api.resource_groups.search(
        json={
            "filters": [
                {
                    "expression": "eq",
                    "field": "resourceType",
                    "value": "AWS"
                }
            ],
            "returns": [
                "resourceGuid"
            ]
        }
    )
    resource_group_guid = response["data"][0]["resourceGuid"]
    return resource_group_guid
