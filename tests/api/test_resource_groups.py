# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.resource_groups import ResourceGroupsAPI

RESOURCE_GROUP_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_resource_groups_api_object_creation(api):
    assert isinstance(api.resource_groups, ResourceGroupsAPI)


def test_resource_groups_api_env_object_creation(api_env):
    assert isinstance(api_env.resource_groups, ResourceGroupsAPI)


def test_resource_groups_api_get(api):
    response = api.resource_groups.get()
    assert "data" in response.keys()


def test_resource_groups_api_create(api):
    response = api.resource_groups.create(
        name=f"AWS Test {RANDOM_TEXT}",
        type="AWS",
        enabled=True,
        props={
            "description": f"Test Description {RANDOM_TEXT}",
            "accountIds": [123456789]
        }
    )

    assert "data" in response.keys()

    global RESOURCE_GROUP_GUID
    RESOURCE_GROUP_GUID = response["data"]["resourceGuid"]


def test_resource_groups_api_get_by_guid(api):
    assert RESOURCE_GROUP_GUID is not None
    if RESOURCE_GROUP_GUID:
        response = api.resource_groups.get_by_guid(guid=RESOURCE_GROUP_GUID)

        assert "data" in response.keys()
        assert response["data"]["resourceGuid"] == RESOURCE_GROUP_GUID


def test_resource_groups_api_search(api):
    response = api.resource_groups.search(query_data={
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
    })
    assert "data" in response.keys()


def test_resource_groups_api_update(api):
    assert RESOURCE_GROUP_GUID is not None
    if RESOURCE_GROUP_GUID:

        response = api.resource_groups.update(
            RESOURCE_GROUP_GUID,
            name=f"AWS Test {RANDOM_TEXT} (Updated)",
            enabled=0,
            props={
                "description": f"Test Description {RANDOM_TEXT} (Updated)",
                "accountIds": [123456789]
            }
        )

        assert "data" in response.keys()


def test_resource_groups_api_delete(api):
    assert RESOURCE_GROUP_GUID is not None
    if RESOURCE_GROUP_GUID:
        response = api.resource_groups.delete(RESOURCE_GROUP_GUID)
        assert response.status_code == 204
