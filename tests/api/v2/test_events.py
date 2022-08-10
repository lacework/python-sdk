# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.events import EventsAPIv2 as EventsAPI
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.events


@pytest.mark.flaky_test
class TestEvidenceEndpoint(SearchEndpoint):

    OBJECT_TYPE = EventsAPI
