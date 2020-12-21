# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from datetime import datetime, timedelta, timezone

from laceworksdk.api.events import EventsAPI


# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=7)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")


# Tests

def test_events_api_object_creation(api):
    assert isinstance(api.events, EventsAPI)


def test_events_api_old_object_creation(api_old):
    assert isinstance(api_old.events, EventsAPI)


def test_events_api_env_object_creation(api_env):
    assert isinstance(api_env.events, EventsAPI)


def test_events_api_get(api):
    response = api.events.get(start_time=start_time, end_time=end_time)
    assert 'data' in response.keys()


def test_events_api_get_for_date_range(api):
    response = api.events.get_for_date_range(start_time=start_time, end_time=end_time)
    assert 'data' in response.keys()


def test_events_api_get_details(api):
    events = api.events.get(start_time=start_time, end_time=end_time)

    if len(events["data"]):
        event_id = random.choice(events["data"])["EVENT_ID"]
        response = api.events.get(id=event_id)
        assert len(response['data']) == 1
        assert response["data"][0]["EVENT_ID"] == event_id
