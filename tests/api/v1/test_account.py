# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v1.account import AccountAPI


# Tests

def test_account_api_object_creation(api):
    assert isinstance(api.account, AccountAPI)


def test_account_api_env_object_creation(api_env):
    assert isinstance(api_env.account, AccountAPI)


def test_account_api_get_org_info(api):
    response = api.account.get_org_info()
    assert "orgAccount" in response.keys()
    assert "orgAccountUrl" in response.keys()
