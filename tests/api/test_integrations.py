# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from laceworksdk.api.integrations import IntegrationsAPI

INTEGRATION_GUID = None


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


def test_integrations_api_create(api):
    response = api.integrations.create(
        name="Slack Test",
        type="SLACK_CHANNEL",
        enabled=True,
        data={
            "SLACK_URL": "https://hooks.slack.com/services/TEST/WEBHOOK"
        }
    )

    assert 'data' in response.keys()

    global INTEGRATION_GUID
    INTEGRATION_GUID = response["data"][0]["INTG_GUID"]


def test_integrations_api_update(api):
    new_name = "Slack Test Updated"
    new_enabled = False

    response = api.integrations.update(
        INTEGRATION_GUID,
        name=new_name,
        enabled=new_enabled
    )

    assert 'data' in response.keys()
    assert response["data"][0]["NAME"] == new_name
    assert response["data"][0]["ENABLED"] == int(new_enabled)


def test_integrations_api_update_by_id(api):
    new_name = "Slack Test Updated 2"
    new_enabled = True

    response = api.integrations.update_by_id(
        INTEGRATION_GUID,
        name=new_name,
        type="SLACK_CHANNEL",
        enabled=new_enabled,
        data={
            "SLACK_URL": "https://hooks.slack.com/services/TEST/WEBHOOK"
        }
    )

    assert 'data' in response.keys()
    assert response["data"][0]["NAME"] == new_name
    assert response["data"][0]["ENABLED"] == int(new_enabled)


def test_integrations_api_update_status(api):
    new_enabled = False

    response = api.integrations.update_status(
        INTEGRATION_GUID,
        enabled=new_enabled
    )

    assert 'data' in response.keys()
    assert response["data"][0]["ENABLED"] == int(new_enabled)


def test_integrations_api_delete(api):
    response = api.integrations.delete(INTEGRATION_GUID)

    print(response)

    assert response["ok"]
