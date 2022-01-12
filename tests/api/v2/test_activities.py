# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.v2.activities import (
    ActivitiesAPI,
    ChangedFilesAPI,
    ConnectionsAPI,
    DnsAPI,
    UserLoginsAPI
)


SCAN_REQUEST_ID = None

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_activities_api_object_creation(api):
    assert isinstance(api.activities, ActivitiesAPI)


def test_activities_changed_files_api_object_creation(api):
    assert isinstance(api.activities.changed_files, ChangedFilesAPI)


def test_activities_changed_files_api_search_by_date(api):
    response = api.activities.changed_files.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1


def test_activities_connections_api_object_creation(api):
    assert isinstance(api.activities.connections, ConnectionsAPI)


def test_activities_connections_api_search_by_date(api):
    response = api.activities.connections.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1


def test_activities_dns_api_object_creation(api):
    assert isinstance(api.activities.dns, DnsAPI)


def test_activities_dns_api_search_by_date(api):
    response = api.activities.dns.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1


def test_activities_user_logins_api_object_creation(api):
    assert isinstance(api.activities.user_logins, UserLoginsAPI)


def test_activities_user_logins_api_search_by_date(api):
    response = api.activities.user_logins.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1
