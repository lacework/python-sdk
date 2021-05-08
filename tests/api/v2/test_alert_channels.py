# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.alert_channels import AlertChannelsAPI

INTEGRATION_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_alert_channels_api_object_creation(api):
    assert isinstance(api.alert_channels, AlertChannelsAPI)


def test_alert_channels_api_env_object_creation(api_env):
    assert isinstance(api_env.alert_channels, AlertChannelsAPI)


def test_alert_channels_api_get(api):
    response = api.alert_channels.get()
    assert "data" in response.keys()


def test_alert_channels_api_get_by_type(api):
    response = api.alert_channels.get()

    if len(response) > 0:
        alert_channel_type = random.choice(response["data"])["type"]

        response = api.alert_channels.get_by_type(type=alert_channel_type)

        assert "data" in response.keys()


def test_alert_channels_api_create(api):
    response = api.alert_channels.create(
        name=f"Slack Test {RANDOM_TEXT}",
        type="SlackChannel",
        enabled=1,
        data={
            "slackUrl": f"https://hooks.slack.com/services/TEST/WEBHOOK/{RANDOM_TEXT}"
        }
    )

    assert "data" in response.keys()

    global INTEGRATION_GUID
    INTEGRATION_GUID = response["data"]["intgGuid"]


def test_alert_channels_api_get_by_guid(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.alert_channels.get_by_guid(guid=INTEGRATION_GUID)

        assert "data" in response.keys()
        assert response["data"]["intgGuid"] == INTEGRATION_GUID


def test_alert_channels_api_search(api):
    response = api.alert_channels.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "type",
                "value": "SlackChannel"
            }
        ],
        "returns": [
            "intgGuid"
        ]
    })
    assert "data" in response.keys()


def test_alert_channels_api_test(api):
    response = api.alert_channels.search(query_data={
        "filters": [
            {
                "expression": "ilike",
                "field": "name",
                "value": "default email"
            }
        ],
        "returns": [
            "intgGuid"
        ]
    })
    default_email_guid = response["data"][0]["intgGuid"]

    if default_email_guid:
        response = api.alert_channels.test(guid=default_email_guid)
        assert response.status_code == 204


def test_alert_channels_api_update(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        new_name = f"Slack Test {RANDOM_TEXT} Updated"
        new_enabled = False

        response = api.alert_channels.update(
            INTEGRATION_GUID,
            name=new_name,
            enabled=new_enabled
        )

        assert "data" in response.keys()
        assert response["data"]["name"] == new_name
        assert response["data"]["enabled"] == int(new_enabled)


def test_alert_channels_api_delete(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.alert_channels.delete(INTEGRATION_GUID)
        assert response.status_code == 204
