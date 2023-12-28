
# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.user_groups import UserGroupsAPI
from laceworksdk.exceptions import ApiError
from tests.api.test_base_endpoint import BaseEndpoint
from laceworksdk import LaceworkClient


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.user_groups

@pytest.fixture(scope="module")
def test_user(api, random_text):
    res = api.team_users.create(f"test{random_text}", f"noreply+{random_text}@lacework.com", "test")
    guid = res["data"]["userGuid"]
    yield guid
    api.team_users.delete(guid)


class TestUserGroups(BaseEndpoint):

    OBJECT_TYPE = UserGroupsAPI

    def test_add_user(self, api_object, test_user):
        response = api_object.add_users("LACEWORK_USER_GROUP_POWER_USER", [test_user])
        assert "data" in response.keys()

    def test_remove_user(self, api_object, test_user):
        response = api_object.remove_users("LACEWORK_USER_GROUP_POWER_USER", [test_user])
        assert "data" in response.keys()

    def test_add_user_should_fail_with_invalid_data(self, api_object):
        with pytest.raises(ApiError) as e:
            api_object.add_users("LACEWORK_USER_GROUP_POWER_USER", ["fake"])
        assert "400" in str(e.value)

    def test_remove_user_should_fail_with_invalid_data(self, api_object):
        with pytest.raises(ApiError) as e:
            api_object.remove_users("LACEWORK_USER_GROUP_POWER_USER", ["fake"])
        assert "400" in str(e.value)
