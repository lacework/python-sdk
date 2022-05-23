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

    @pytest.mark.parametrize("dataset", ["AwsCompliance", "GcpCompliance"])
    def test_api_search_by_date(self, api_object, dataset):
        start_time, end_time = self._get_start_end_times(self.DAY_DELTA)

        for attribute in self.OBJECT_MAP.keys():
            response = getattr(api_object, attribute).search(json={
                "timeFilters": {
                    "startTime": start_time,
                    "endTime": end_time
                },
                "dataset": dataset
            })

            self._assert_pages(response, self.MAX_PAGES)
