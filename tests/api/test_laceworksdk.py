# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk import LaceworkClient


# Tests

def test_lacework_client_api_object_creation(api):
    assert isinstance(api, LaceworkClient)


def test_lacework_client_api_env_object_creation(api_env):
    assert isinstance(api_env, LaceworkClient)


def test_lacework_client_api_set_org(api):

    api.set_org_level_access(True)
    assert api._session._org_level_access is True

    api.set_org_level_access(False)
    assert api._session._org_level_access is False


def test_lacework_client_api_set_subaccount(api):

    old_subaccount = api._session._subaccount

    api.set_subaccount("testing")
    assert api._session._subaccount == "testing"

    api.set_subaccount(old_subaccount)
    assert api._session._subaccount == old_subaccount
