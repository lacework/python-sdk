# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.agent_access_tokens import AgentAccessTokensAPI

AGENT_ACCESS_TOKEN_ID = None
AGENT_ACCESS_TOKEN_ALIAS = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_agent_access_tokens_api_object_creation(api):
    assert isinstance(api.agent_access_tokens, AgentAccessTokensAPI)


def test_agent_access_tokens_api_env_object_creation(api_env):
    assert isinstance(api_env.agent_access_tokens, AgentAccessTokensAPI)


def test_agent_access_tokens_api_get(api):
    response = api.agent_access_tokens.get()
    assert "data" in response.keys()


def test_agent_access_tokens_api_get_by_id(api):
    response = api.agent_access_tokens.get()

    if len(response) > 0:
        global AGENT_ACCESS_TOKEN_ID, AGENT_ACCESS_TOKEN_ALIAS

        # Choose a random agent access token
        agent_access_token = random.choice(response["data"])

        AGENT_ACCESS_TOKEN_ID = agent_access_token["accessToken"]
        AGENT_ACCESS_TOKEN_ALIAS = agent_access_token["tokenAlias"]

        response = api.agent_access_tokens.get_by_id(id=AGENT_ACCESS_TOKEN_ID)

        assert "data" in response.keys()


def test_agent_access_tokens_api_search(api):
    assert AGENT_ACCESS_TOKEN_ID is not None
    if AGENT_ACCESS_TOKEN_ID:

        response = api.agent_access_tokens.search(
            query_data={
                "filters": [
                    {
                        "expression": "eq",
                        "field": "accessToken",
                        "value": AGENT_ACCESS_TOKEN_ID
                    }
                ],
                "returns": [
                    "createdTime"
                ]
            }
        )

        assert "data" in response.keys()


def test_agent_access_tokens_api_update(api):
    assert AGENT_ACCESS_TOKEN_ID is not None
    if AGENT_ACCESS_TOKEN_ID:

        new_alias = f"{AGENT_ACCESS_TOKEN_ALIAS} {RANDOM_TEXT}"

        response = api.agent_access_tokens.update(
            AGENT_ACCESS_TOKEN_ID,
            alias=new_alias
        )

        assert response["data"]["tokenAlias"] == new_alias

        response = api.agent_access_tokens.update(
            AGENT_ACCESS_TOKEN_ID,
            alias=AGENT_ACCESS_TOKEN_ALIAS
        )

        assert "data" in response.keys()
        assert response["data"]["tokenAlias"] == AGENT_ACCESS_TOKEN_ALIAS
