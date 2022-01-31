# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.contract_info import ContractInfoAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.contract_info


class TestContractInfo(BaseEndpoint):

    OBJECT_ID_NAME = "alertId"
    OBJECT_TYPE = ContractInfoAPI

    def test_api_get(self, api_object):
        response = api_object.get()
        assert "data" in response.keys()
