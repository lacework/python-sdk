# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.activities import (
    ActivitiesAPI,
    ChangedFilesAPI,
    DnsAPI,
    UserLoginsAPI
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.activities


class TestActivitiesEndpoint(SearchEndpoint):

    OBJECT_TYPE = ActivitiesAPI
    OBJECT_MAP = {
        "changed_files": ChangedFilesAPI,
        "dns": DnsAPI,
        "user_logins": UserLoginsAPI
    }
