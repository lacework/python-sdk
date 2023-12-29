# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.team_users import TeamUsersAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.team_users


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "name": "John Doe",
        "email": f"{random_text.lower()}@lacework.net",
        "company": "Lacework",
    }


@pytest.fixture(scope="module")
def api_object_update_body():
    return {
        "user_enabled": 0
    }


class TestTeamUsers(CrudEndpoint):

    OBJECT_ID_NAME = "userGuid"
    OBJECT_TYPE = TeamUsersAPI

    def test_api_search(self, api_object, request):
        "Not implemented"
        pass

    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)
