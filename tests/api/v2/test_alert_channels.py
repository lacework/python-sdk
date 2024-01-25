# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.alert_channels import AlertChannelsAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.alert_channels


@pytest.fixture(scope="module")
def api_object_org(api):
    api.set_org_level_access(True)
    yield api.alert_channels
    api.set_org_level_access(False)


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "name": f"Slack Test {random_text}",
        "type": "SlackChannel",
        "enabled": 1,
        "data": {
            "slackUrl": f"https://hooks.slack.com/services/TEST/WEBHOOK/{random_text}"
        }
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "name": f"Slack Test {random_text} Updated",
        "enabled": 0
    }


class TestAlertChannels(CrudEndpoint):

    OBJECT_ID_NAME = "intgGuid"
    OBJECT_TYPE = AlertChannelsAPI

    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)

    @pytest.mark.order("second")
    def test_api_get_by_type(self, api_object):
        self._get_object_classifier_test(api_object, "type")

    def test_api_test(self, api_object):
        response = api_object.search(json={
            "filters": [
                {
                    "expression": "ilike",
                    "field": "name",
                    "value": "default email"
                }
            ],
            "returns": [
                "intgGuid"
            ]
        })

        if len(response["data"]) > 0:
            default_email_guid = response["data"][0]["intgGuid"]
            response = api_object.test(guid=default_email_guid)
            assert response.status_code == 204


@pytest.mark.parametrize("api_object", [pytest.lazy_fixture("api_object_org")])
class TestAlertChannelsOrg(TestAlertChannels):

    @pytest.mark.flaky(reruns=10)   # Because sometimes it tries to get deets for the test object that was just deleted
                                    # by the TestAlertChannels class
    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)

    @pytest.mark.order("second")
    def test_api_get_by_type(self, api_object):
        self._get_object_classifier_test(api_object, "type")
