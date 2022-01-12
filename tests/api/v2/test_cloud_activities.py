# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone
from unittest import TestCase

from laceworksdk.api.v2.cloud_activities import CloudActivitiesAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_cloud_activities_api_object_creation(api):
    assert isinstance(api.cloud_activities, CloudActivitiesAPI)


def test_cloud_activities_api_env_object_creation(api_env):
    assert isinstance(api_env.cloud_activities, CloudActivitiesAPI)


def test_cloud_activities_api_get(api):
    response = api.cloud_activities.get()
    assert "data" in response.keys()


def test_cloud_activities_api_get_by_date(api):
    response = api.cloud_activities.get(start_time=start_time, end_time=end_time)
    assert "data" in response.keys()


def test_cloud_activities_api_get_by_date_camelcase(api):
    response = api.cloud_activities.get(startTime=start_time, endTime=end_time)
    assert "data" in response.keys()


def test_cloud_activities_api_get_duplicate_key(api):
    tester = TestCase()
    with tester.assertRaises(KeyError):
        api.cloud_activities.get(start_time=start_time, startTime=start_time, endTime=end_time)


def test_cloud_activities_api_get_pages(api):
    response = api.cloud_activities.get_pages()

    for page in response:
        assert "data" in page.keys()


def test_cloud_activities_api_get_data_items(api):
    response = api.cloud_activities.get_data_items(start_time=start_time, end_time=end_time)

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


def test_cloud_activities_api_search(api):
    response = api.cloud_activities.search(query_data={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters": [
            {
                "expression": "eq",
                "field": "eventModel",
                "value": "CloudTrailCep"
            }
        ],
        "returns": [
            "eventType",
            "eventActor"
        ]
    })
    assert "data" in response.keys()
