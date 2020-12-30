# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.cloudtrail import CloudTrailAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_cloud_trail_api_object_creation(api):
    assert isinstance(api.cloudtrail, CloudTrailAPI)


def test_cloud_trail_api_env_object_creation(api_env):
    assert isinstance(api_env.cloudtrail, CloudTrailAPI)


def test_cloud_trail_api_get(api):
    response = api.cloudtrail.get()
    assert 'data' in response.keys()


def test_cloud_trail_api_get_by_date(api):
    response = api.cloudtrail.get(start_time=start_time, end_time=end_time)
    assert 'data' in response.keys()


def test_cloud_trail_api_search(api):
    response = api.cloudtrail.search(query_data={
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
    assert 'data' in response.keys()
