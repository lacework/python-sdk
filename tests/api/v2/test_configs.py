# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.v2.configs import (
    ConfigsAPI,
    ComplianceEvaluationsAPI
)

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_configs_api_object_creation(api):
    assert isinstance(api.configs, ConfigsAPI)


def test_configs_changed_files_api_object_creation(api):
    assert isinstance(api.configs.compliance_evaluations, ComplianceEvaluationsAPI)


def test_configs_changed_files_api_search_by_date(api):
    response = api.configs.compliance_evaluations.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        },
        "dataset": "AwsCompliance"
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1
