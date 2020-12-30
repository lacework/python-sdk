# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.audit_logs import AuditLogsAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_audit_logs_api_object_creation(api):
    assert isinstance(api.audit_logs, AuditLogsAPI)


def test_audit_logs_api_env_object_creation(api_env):
    assert isinstance(api_env.audit_logs, AuditLogsAPI)


def test_audit_logs_api_get(api):
    response = api.audit_logs.get()
    assert 'data' in response.keys()


def test_audit_logs_api_get_by_date(api):
    response = api.audit_logs.get(start_time=start_time, end_time=end_time)
    assert 'data' in response.keys()


def test_audit_logs_api_search(api):
    response = api.audit_logs.search(query_data={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters": [
            {
                "expression": "rlike",
                "field": "userName",
                "value": "lacework.net"
            }
        ],
        "returns": [
            "accountName",
            "userAction",
            "userName"
        ]
    })
    assert 'data' in response.keys()
