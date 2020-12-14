# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from laceworksdk.api.token import TokenAPI


# Tests

def test_token_api_object_creation(api):
    assert isinstance(api.tokens, TokenAPI)


def test_token_api_get_enabled(api):
    response = api.tokens.get_enabled()
    assert response["ok"]


def test_token_api_get_token(api):
    enabled_tokens = api.tokens.get_enabled()

    if len(enabled_tokens["data"]):
        response = api.tokens.get_token(random.choice(enabled_tokens["data"])["ACCESS_TOKEN"])
        assert response["ok"]
        assert len(response["data"]) == 1
