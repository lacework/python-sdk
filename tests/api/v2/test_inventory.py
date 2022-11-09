# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.inventory import (
    InventoryAPI
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.inventory


class TestConfigsEndpoint(SearchEndpoint):

    OBJECT_TYPE = InventoryAPI

    @pytest.mark.parametrize("csp", ["AWS", "Azure", "GCP"])
    def test_api_search_by_date(self, api_object, csp):

        return super().test_api_search_by_date(api_object=api_object, filters={"csp": csp})

    @pytest.mark.parametrize("dataset", ["AwsCompliance", "GcpCompliance"])
    def test_api_search_by_date_deprecated(self, api_object, dataset):

        return super().test_api_search_by_date(api_object=api_object, filters={"dataset": dataset})
