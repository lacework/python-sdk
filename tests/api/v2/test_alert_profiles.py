# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

import pytest

from laceworksdk.api.v2.alert_profiles import AlertProfilesAPI

ALERT_PROFILE_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_alert_profiles_api_object_creation(api):
    assert isinstance(api.alert_profiles, AlertProfilesAPI)


def test_alert_profiles_api_get(api):
    response = api.alert_profiles.get()
    assert "data" in response.keys()


# TODO: Remove ci_exempt for all tests once v4.50 ships
@pytest.mark.ci_exempt
def test_alert_profiles_api_create(api):
    response = api.alert_profiles.create(
        alert_profile_id=f"Test_{RANDOM_TEXT}_AlertProfileID",
        alerts=[
            {
                "name": f"HE_User_NewViolation_{RANDOM_TEXT}",
                "eventName": f"Alert Event Name {RANDOM_TEXT}",
                "description": f"Alert Event Description {RANDOM_TEXT}",
                "subject": f"Alert Event Subject {RANDOM_TEXT}"
            }
        ],
        extends="LW_HE_USERS_DEFAULT_PROFILE"
    )

    assert "data" in response.keys()

    global ALERT_PROFILE_GUID
    ALERT_PROFILE_GUID = response["data"]["alertProfileId"]


@pytest.mark.ci_exempt
def test_alert_profiles_api_get_by_guid(api):
    assert ALERT_PROFILE_GUID is not None
    if ALERT_PROFILE_GUID:
        response = api.alert_profiles.get_by_id(id=ALERT_PROFILE_GUID)

        assert "data" in response.keys()
        assert response["data"]["alertProfileId"] == ALERT_PROFILE_GUID


@pytest.mark.ci_exempt
def test_alert_profiles_api_update(api):
    assert ALERT_PROFILE_GUID is not None
    if ALERT_PROFILE_GUID:
        response = api.alert_profiles.update(
            ALERT_PROFILE_GUID,
            alerts=[
                {
                    "name": f"HE_User_NewViolation_{RANDOM_TEXT}_Updated",
                    "eventName": f"Alert Event Name {RANDOM_TEXT} (Updated)",
                    "description": f"Alert Event Description {RANDOM_TEXT} (Updated)",
                    "subject": f"Alert Event Subject {RANDOM_TEXT} (Updated)"
                }
            ]
        )

        assert "data" in response.keys()


@pytest.mark.ci_exempt
def test_alert_profiles_api_delete(api):
    assert ALERT_PROFILE_GUID is not None
    if ALERT_PROFILE_GUID:
        response = api.alert_profiles.delete(ALERT_PROFILE_GUID)
        assert response.status_code == 204
