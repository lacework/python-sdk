# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone


class SearchEndpoint:

    OBJECT_TYPE = None
    OBJECT_MAP = {}

    DAY_DELTA = 1
    MAX_PAGES = 2

    def test_object_creation(self, api_object):

        assert isinstance(api_object, self.OBJECT_TYPE)

        for attribute, object_type in self.OBJECT_MAP.items():
            assert isinstance(getattr(api_object, attribute), object_type)

    def test_api_search_by_date(self, api_object):
        start_time, end_time = self._get_start_end_times(self.DAY_DELTA)

        for attribute in self.OBJECT_MAP.keys():
            response = getattr(api_object, attribute).search(json={
                "timeFilters": {
                    "startTime": start_time,
                    "endTime": end_time
                }
            })

            self._assert_pages(response, self.MAX_PAGES)

    def _assert_pages(self, response, max_pages):
        page_count = 0
        for page in response:
            if page_count >= max_pages:
                return
            assert len(page["data"]) == page.get("paging", {}).get("rows", 0)
            page_count += 1

    def _get_start_end_times(self, day_delta):
        current_time = datetime.now(timezone.utc)
        start_time = current_time - timedelta(days=day_delta)
        start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        return start_time, end_time
