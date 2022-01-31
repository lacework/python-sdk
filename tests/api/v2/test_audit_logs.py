# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.audit_logs import AuditLogsAPI
from tests.api.test_read_endpoint import ReadEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.audit_logs


class TestAuditLogs(ReadEndpoint):

    OBJECT_TYPE = AuditLogsAPI

    def test_get_by_date(self, api_object):
        start_time, end_time = self._get_start_end_times()
        response = api_object.get(start_time=start_time, end_time=end_time)
        assert "data" in response.keys()

    def test_api_search(self, api_object):
        start_time, end_time = self._get_start_end_times()
        response = api_object.search(json={
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
        assert "data" in response.keys()
