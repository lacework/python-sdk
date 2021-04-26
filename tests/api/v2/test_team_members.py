# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.team_members import TeamMembersAPI

TEAM_MEMBER_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_team_members_api_object_creation(api):
    assert isinstance(api.team_members, TeamMembersAPI)


def test_team_members_api_env_object_creation(api_env):
    assert isinstance(api_env.team_members, TeamMembersAPI)


def test_team_members_api_get(api):
    response = api.team_members.get()
    assert "data" in response.keys()


def test_team_members_api_create(api):
    response = api.team_members.create(
        username=f"{RANDOM_TEXT}@lacework.net",
        props={
            "firstName": "John",
            "lastName": "Doe",
            "company": "Lacework",
            "accountAdmin": True
        },
        enabled=True
    )

    assert "data" in response.keys()

    global TEAM_MEMBER_GUID
    TEAM_MEMBER_GUID = response["data"]["userGuid"]


def test_team_members_api_get_by_guid(api):
    assert TEAM_MEMBER_GUID is not None
    if TEAM_MEMBER_GUID:
        response = api.team_members.get_by_guid(guid=TEAM_MEMBER_GUID)

        assert "data" in response.keys()
        assert response["data"]["userGuid"] == TEAM_MEMBER_GUID


def test_team_members_api_search(api):
    response = api.team_members.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "userName",
                "value": f"{RANDOM_TEXT}@lacework.net"
            }
        ],
        "returns": [
            "userGuid"
        ]
    })
    assert "data" in response.keys()
    assert len(response["data"]) == 1


def test_team_members_api_update(api):
    assert TEAM_MEMBER_GUID is not None
    if TEAM_MEMBER_GUID:
        response = api.team_members.update(
            TEAM_MEMBER_GUID,
            enabled=False
        )

        assert "data" in response.keys()


def test_team_members_api_delete(api):
    assert TEAM_MEMBER_GUID is not None
    if TEAM_MEMBER_GUID:
        response = api.team_members.delete(TEAM_MEMBER_GUID)
        assert response.status_code == 204
