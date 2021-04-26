# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.contract_info import ContractInfoAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

# Tests


def test_contract_info_api_object_creation(api):
    assert isinstance(api.contract_info, ContractInfoAPI)


def test_contract_info_api_env_object_creation(api_env):
    assert isinstance(api_env.contract_info, ContractInfoAPI)


def test_contract_info_api_get(api):
    response = api.contract_info.get()
    assert "data" in response.keys()


def test_contract_info_api_get_by_date(api):
    response = api.contract_info.get(start_time=start_time, end_time=end_time)
    assert "data" in response.keys()
