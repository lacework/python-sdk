# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from laceworksdk.api.integrations import IntegrationsAPI


# Tests

def test_integrations_api_object_creation(api):
    assert isinstance(api.integrations, IntegrationsAPI)


def test_integrations_api_get_all(api):
    response = api.integrations.get_all()
    assert response["ok"]


def test_integrations_api_get_by_id(api):
    integrations = api.integrations.get_all()

    if len(integrations["data"]):
        integration_id = random.choice(integrations["data"])["INTG_GUID"]
        response = api.integrations.get_by_id(id=integration_id)
        assert response["ok"]
        assert len(response['data']) == 1


def test_integrations_api_get_by_type(api):
    response = api.integrations.get_by_type("AWS_CFG")
    assert response["ok"]


def test_integrations_api_get_schema(api):
    response = api.integrations.get_schema("AWS_CFG")
    assert response["ok"]
