# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.user_profile import UserProfileAPI


# Tests

def test_user_profile_api_object_creation(api):
    assert isinstance(api.user_profile, UserProfileAPI)


def test_user_profile_api_env_object_creation(api_env):
    assert isinstance(api_env.user_profile, UserProfileAPI)


def test_user_profile_api_get(api):
    response = api.schemas.get()
    assert len(response) > 0
