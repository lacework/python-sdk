# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

import pytest

from laceworksdk.api.v2.policies import PoliciesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.policies


@pytest.fixture(scope="module")
def api_object_create_body(random_text, query):
    return {
        "policy_type": "Violation",
        "query_id": query["queryId"],
        "enabled": True,
        "title": random_text,
        "description": f"{random_text} description",
        "remediation": "Policy remediation",
        "severity": "high",
        "alert_enabled": True,
        "alert_profile": "LW_CloudTrail_Alerts"
    }


@pytest.fixture(scope="module")
def api_object_update_body():
    return {
        "enabled": False
    }


@pytest.fixture(scope="module")
def query(api):
    queries = api.queries.get()
    queries = list(filter(lambda elem: elem["owner"] == "Lacework" and "LW_Global_AWS_CTA" in elem["queryId"], queries["data"]))
    query = random.choice(queries)
    return query


class TestPolicies(CrudEndpoint):

    OBJECT_ID_NAME = "policyId"
    OBJECT_TYPE = PoliciesAPI

    def test_api_get_by_id(self, api_object):
        self._get_object_classifier_test(api_object, "id", self.OBJECT_ID_NAME)

    def test_api_search(self):
        pass
