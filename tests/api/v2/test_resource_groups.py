# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest
from laceworksdk.api.v2.resource_groups import ResourceGroupsAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.resource_groups


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "resource_name": f"AWS Test {random_text}",
        "resource_type": "AWS",
        "enabled": True,
        "props": {
            "description": f"Test Description {random_text}",
            "accountIds": ["123456789012"]
        }
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "resource_name": f"AWS Test {random_text} (Updated)",
        "enabled": 0,
        "props": {
            "description": f"Test Description {random_text} (Updated)",
            "accountIds": ["123456789012"]
        }
    }


class TestResourceGroups(CrudEndpoint):

    OBJECT_ID_NAME = "resourceGuid"
    OBJECT_TYPE = ResourceGroupsAPI
    OBJECT_PARAM_EXCEPTIONS = ["props"]

    @pytest.mark.flaky(reruns=10)   # Because sometimes this attempts to get an object that has just been deleted
    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        response = api_object.get()
        guid = None
        if len(response["data"]) > 0:
            for entry in response['data']:
                if self.OBJECT_ID_NAME in entry:
                    guid = entry[self.OBJECT_ID_NAME]
        if guid:
            response = api_object.get_by_guid(guid)
            assert "data" in response.keys()
            assert response["data"]['resourceGuid'] == guid
