# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.user_profile import UserProfileAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.user_profile


class TestUserProfile(BaseEndpoint):

    OBJECT_TYPE = UserProfileAPI

    def test_api_get(self, api_object):
        response = api_object.get()
        keys = set([
            "username",
            "orgAccount",
            "url",
            "orgAdmin",
            "orgUser",
            "accounts"
        ])

        for item in response["data"]:
            assert keys.issubset(item.keys())
