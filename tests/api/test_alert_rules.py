# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.alert_rules import AlertRulesAPI

ALERT_RULE_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_alert_rules_api_object_creation(api):
    assert isinstance(api.alert_rules, AlertRulesAPI)


def test_alert_rules_api_env_object_creation(api_env):
    assert isinstance(api_env.alert_rules, AlertRulesAPI)


def test_alert_rules_api_get(api):
    response = api.alert_rules.get()
    assert "data" in response.keys()


def test_alert_rules_api_get_by_guid(api):
    response = api.alert_rules.get()

    if len(response) > 0:
        alert_rule_guid = random.choice(response["data"])["mcGuid"]

        response = api.alert_rules.get_by_guid(guid=alert_rule_guid)

        assert "data" in response.keys()
        assert response["data"]["mcGuid"] == alert_rule_guid


def test_alert_rules_api_create(api):

    response = api.alert_channels.search(
        query_data={
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
        }
    )
    alert_channel_guid = random.choice(response["data"])["intgGuid"]

    response = api.resource_groups.search(
        query_data={
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
    resource_group_guid = random.choice(response["data"])["resourceGuid"]

    response = api.alert_rules.create(
        type="Event",
        filters={
            "name": f"Test Alert Rule {RANDOM_TEXT}",
            "description": f"Test Alert Rule Description {RANDOM_TEXT}",
            "enabled": 1,
            "resourceGroups": [resource_group_guid],
            "eventCategory": ["Compliance"],
            "severity": [1, 2, 3]
        },
        intgGuidList=[alert_channel_guid]
    )

    assert "data" in response.keys()

    global ALERT_RULE_GUID
    ALERT_RULE_GUID = response["data"]["mcGuid"]


def test_alert_rules_api_search(api):
    response = api.alert_rules.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "type",
                "value": "Event"
            }
        ],
        "returns": [
            "mcGuid"
        ]
    })
    assert "data" in response.keys()


def test_alert_rules_api_update(api):
    response = api.alert_rules.get_by_guid(guid=ALERT_RULE_GUID)

    filters = response["data"]["filters"]
    filters["name"] = f"Test Alert Rule {RANDOM_TEXT} (Updated)"
    filters["enabled"] = 0

    print(filters)

    if ALERT_RULE_GUID:
        response = api.alert_rules.update(
            ALERT_RULE_GUID,
            filters=filters
        )

        assert "data" in response.keys()

    assert ALERT_RULE_GUID is not None


def test_alert_rules_api_delete(api):
    if ALERT_RULE_GUID:
        response = api.alert_rules.delete(ALERT_RULE_GUID)
        assert response.status_code == 204

    assert ALERT_RULE_GUID is not None
