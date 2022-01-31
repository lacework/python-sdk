# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.team_members import TeamMembersAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.team_members


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "user_name": f"{random_text.lower()}@lacework.net",
        "props": {
            "firstName": "John",
            "lastName": "Doe",
            "company": "Lacework",
            "accountAdmin": True
        },
        "user_enabled": True
    }


@pytest.fixture(scope="module")
def api_object_update_body():
    return {
        "user_enabled": False
    }


class TestTeamMembers(CrudEndpoint):

    OBJECT_ID_NAME = "userGuid"
    OBJECT_TYPE = TeamMembersAPI

    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)
