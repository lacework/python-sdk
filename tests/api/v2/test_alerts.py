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


@pytest.mark.flaky_test
class TestAlerts(ReadEndpoint):

    OBJECT_ID_NAME = "alertId"
    OBJECT_TYPE = AlertsAPI

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

    def test_get_details(self, api_object):
        guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)
        response = api_object.get_details(guid)
        assert "data" in response.keys()
