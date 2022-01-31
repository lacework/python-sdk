# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from unittest import TestCase

from laceworksdk.api.v2.cloud_activities import CloudActivitiesAPI
from tests.api.test_read_endpoint import ReadEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.cloud_activities


class TestCloudActivities(ReadEndpoint):

    OBJECT_ID_NAME = "eventId"
    OBJECT_TYPE = CloudActivitiesAPI

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

    def test_get_pages(self, api_object):
        response = api_object.get_pages()

        for page in response:
            assert "data" in page.keys()

    def test_get_data_items(self, api_object):
        start_time, end_time = self._get_start_end_times()
        response = api_object.get_data_items(start_time=start_time, end_time=end_time)

        event_keys = set([
            "endTime",
            "entityMap",
            "eventActor",
            "eventId",
            "eventModel",
            "eventType",
            "startTime"
        ])

        for item in response:
            assert event_keys.issubset(item.keys())
