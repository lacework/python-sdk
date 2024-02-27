# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest
import random
from laceworksdk.api.v2.policy_exceptions import PolicyExceptionsAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.policy_exceptions


@pytest.fixture(scope="module")
def policy_id():
    return "lacework-global-100"


@pytest.fixture(scope="module")
def policy_exception_id(api_object, policy_id):
    response = api_object.get(policy_id=policy_id)
    return random.choice(response["data"])['exceptionId']


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "description": f"Test Policy Exception {random_text}",
        "constraints": [
            {
                "fieldKey": "resourceTags",
                "fieldValues": [
                    {"key": "TestKey", "value": "TestValue"}
                ]
            }
        ]
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "description": f"Test Policy Exception {random_text} (Updated)",
        "constraints": [
            {
                "fieldKey": "resourceTags",
                "fieldValues": [
                    {"key": "TestKey", "value": "UpdatedTestValue"}
                ]
            }
        ]
    }


class TestPolicyExceptions(CrudEndpoint):

    OBJECT_ID_NAME = "exceptionId"
    OBJECT_TYPE = PolicyExceptionsAPI

    def test_api_get(self, api_object, policy_id):
        response = api_object.get(policy_id=policy_id)

        assert "data" in response.keys()

    def test_api_create(self, api_object, policy_id, api_object_create_body, request):
        response = api_object.create(policy_id, **api_object_create_body)

        assert "data" in response.keys()
        self._check_object_values(api_object_create_body, response)

        request.config.cache.set(self.OBJECT_ID_NAME, response["data"][self.OBJECT_ID_NAME])

    @pytest.mark.quarantine_test  # Stopped working around 2/27/2024. API bug or change?
    @pytest.mark.flaky(reruns=10)   # Because sometimes this attempts to get an object that has just been deleted
    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object, policy_id, policy_exception_id):
        response = api_object.get(policy_exception_id, policy_id)
        assert "data" in response.keys()

    def test_api_search(self):
        pass

    @pytest.mark.quarantine_test  # Stopped working around 2/27/2024. API bug or change?
    def test_api_update(self, api_object, policy_id, api_object_update_body, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)

        if guid is None:
            guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)

        assert guid is not None
        if guid:
            response = api_object.update(guid, policy_id, **api_object_update_body)

            assert "data" in response.keys()

            self._check_object_values(api_object_update_body, response)

    @pytest.mark.quarantine_test  # Stopped working around 2/27/2024. API bug or change?
    def test_api_delete(self, api_object, policy_id, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)
        assert guid is not None
        if guid:
            response = api_object.delete(guid, policy_id)
            assert response.status_code == 204
