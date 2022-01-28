# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.agent_access_tokens import AgentAccessTokensAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.agent_access_tokens


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "token_enabled": 1
    }


class TestAgentAccessTokens(CrudEndpoint):

    OBJECT_ID_NAME = "accessToken"
    OBJECT_TYPE = AgentAccessTokensAPI

    def test_api_create(self):
        """
        Agent Access Tokens shouldn't be created with tests
        """

    def test_api_get_by_id(self, api_object):
        self._get_object_classifier_test(api_object, "id", self.OBJECT_ID_NAME)

    def test_api_delete(self):
        """
        Agent Access Tokens cannot currently be deleted
        """
