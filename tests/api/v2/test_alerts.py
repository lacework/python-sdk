# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from unittest import TestCase

from laceworksdk.api.v2.alerts import AlertsAPI
from tests.api.test_read_endpoint import ReadEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.alerts


@pytest.fixture(scope="module")
def open_alerts_filter():
    return {
        "filters": [
            {"field": "status", "expression": "eq", "value": "Open"}
        ]
    }


@pytest.mark.flaky_test
class TestAlerts(ReadEndpoint):

    OBJECT_ID_NAME = "alertId"
    OBJECT_TYPE = AlertsAPI

    OBJECT_SCOPES = [
        "Details",
        "Investigation",
        "Events",
        "RelatedAlerts",
        "Integrations",
        "Timeline"
    ]

    def test_get_by_date(self, api_object):
        start_time, end_time = self._get_start_end_times()
        response = api_object.get(start_time=start_time, end_time=end_time)
        assert "data" in response.keys()

    def test_get_by_date_camelcase(self, api_object):
        start_time, end_time = self._get_start_end_times()
        response = api_object.get(startTime=start_time, endTime=end_time)
        assert "data" in response.keys()

    def test_get_duplicate_key(self, api_object):
        start_time, end_time = self._get_start_end_times()
        tester = TestCase()
        with tester.assertRaises(KeyError):
            api_object.get(start_time=start_time, startTime=start_time, endTime=end_time)

    @pytest.mark.parametrize("scope", OBJECT_SCOPES)
    def test_get_details(self, api_object, scope):
        guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)
        response = api_object.get_details(guid, scope)
        assert "data" in response.keys()

    def test_comment(self, api_object):
        guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)
        response = api_object.comment(guid, "Test Comment")
        assert "data" in response.keys()

    def test_close_fp(self, api_object, open_alerts_filter):
        guid = self._search_random_object(api_object, self.OBJECT_ID_NAME, open_alerts_filter)
        response = api_object.close(guid, 1)
        assert "data" in response.keys()

    def test_close_other(self, api_object, open_alerts_filter):
        guid = self._search_random_object(api_object, self.OBJECT_ID_NAME, open_alerts_filter)
        response = api_object.close(guid, 0, "Test Reason")
        assert "data" in response.keys()
