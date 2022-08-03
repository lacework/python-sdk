# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.configs import (
    ConfigsAPI,
    ComplianceEvaluationsAPI
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.configs


class TestConfigsEndpoint(SearchEndpoint):

    OBJECT_TYPE = ConfigsAPI
    OBJECT_MAP = {
        "compliance_evaluations": ComplianceEvaluationsAPI,
    }

    @pytest.mark.parametrize("dataset", ["AwsCompliance", "AzureCompliance", "GcpCompliance"])
    def test_api_search_by_date(self, api_object, dataset):

        return super().test_api_search_by_date(api_object=api_object, filters={"dataset": dataset})
