# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.organization_info import OrganizationInfoAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.organization_info


class TestDatasources(BaseEndpoint):

    OBJECT_ID_NAME = "name"
    OBJECT_TYPE = OrganizationInfoAPI

    def test_api_get(self, api_object):
        response = api_object.get()
        keys = set([
            "orgAccount",
            "orgAccountUrl"
        ])

        for item in response["data"]:
            assert keys.issubset(item.keys())
