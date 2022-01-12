# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from datetime import datetime, timedelta, timezone
from unittest import TestCase

from laceworksdk.api.v2.alerts import AlertsAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_alerts_api_object_creation(api):
    assert isinstance(api.alerts, AlertsAPI)


def test_alerts_api_get(api):
    response = api.alerts.get()
    assert "data" in response.keys()


def test_alerts_api_get_by_date(api):
    response = api.alerts.get(start_time=start_time, end_time=end_time)
    assert "data" in response.keys()


def test_alerts_api_get_by_date_camelcase(api):
    response = api.alerts.get(startTime=start_time, endTime=end_time)
    assert "data" in response.keys()


def test_alerts_api_get_duplicate_key(api):
    tester = TestCase()
    with tester.assertRaises(KeyError):
        api.alerts.get(start_time=start_time, startTime=start_time, endTime=end_time)


def test_alerts_api_get_details(api):
    response = api.alerts.get()
    alert_id = random.choice(response["data"])["alertId"]

    response = api.alerts.get_details(alert_id)

    assert "data" in response.keys()


def test_alerts_api_search(api):
    response = api.alerts.search(json={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters": [
            {
                "expression": "eq",
                "field": "alertModel",
                "value": "AwsApiTracker"
            }
        ],
        "returns": []
    })

    for page in response:
        assert "data" in page.keys()
