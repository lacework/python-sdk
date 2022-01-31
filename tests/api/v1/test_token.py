# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from laceworksdk.api.v1.token import TokenAPI


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


def test_token_api_update(api):
    enabled_tokens = api.tokens.get()

    if len(enabled_tokens["data"]):
        access_token = random.choice(enabled_tokens["data"])["ACCESS_TOKEN"]
        token_enabled = True
        response = api.tokens.update(access_token, enabled=token_enabled)
        assert response["ok"]
        assert len(response["data"]) == 1
        assert bool(response["data"][0]["TOKEN_ENABLED"]) == token_enabled
