# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.alert_rules import AlertRulesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.alert_rules


@pytest.fixture(scope="module")
def api_object_create_body(random_text, email_alert_channel_guid):
    return {
        "type": "Event",
        "filters": {
            "name": f"Test Alert Rule {random_text}",
            "description": f"Test Alert Rule Description {random_text}",
            "enabled": 1,
            "severity": [1, 2, 3]
        },
        "intg_guid_list": [email_alert_channel_guid]
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "filters": {
            "name": f"Test Alert Rule {random_text} Updated",
            "enabled": 0
        }
    }


class TestAlertRules(CrudEndpoint):

    OBJECT_ID_NAME = "mcGuid"
    OBJECT_TYPE = AlertRulesAPI

    @pytest.mark.flaky(reruns=10)   # Because sometimes this attempts to get an object that has just been deleted
    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)

    # Ovveriding test due to API bug with "returns": ["mcGuid"]
    def test_api_search(self, api_object, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)

        if guid is None:
            guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)

        assert guid is not None
        if guid:
            response = api_object.search(json={
                "filters": [
                    {
                        "expression": "eq",
                        "field": self.OBJECT_ID_NAME,
                        "value": guid
                    }
                ],
                "returns": [
                    "filters"
                ]
            })
