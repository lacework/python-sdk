# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.alert_profiles import AlertProfilesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.alert_profiles


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "alert_profile_id": f"Test_{random_text}_AlertProfileID",
        "alerts": [
            {
                "name": f"HE_User_NewViolation_{random_text}",
                "eventName": f"Alert Event Name {random_text}",
                "description": f"Alert Event Description {random_text}",
                "subject": f"Alert Event Subject {random_text}"
            }
        ],
        "extends": "LW_HE_USERS_DEFAULT_PROFILE"
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "alerts": [
            {
                "name": f"HE_User_NewViolation_{random_text}_Updated",
                "eventName": f"Alert Event Name {random_text} Updated",
                "description": f"Alert Event Description {random_text} Updated",
                "subject": f"Alert Event Subject {random_text} Updated"
            }
        ]
    }


class TestAlertProfiles(CrudEndpoint):

    OBJECT_ID_NAME = "alertProfileId"
    OBJECT_TYPE = AlertProfilesAPI
    OBJECT_PARAM_EXCEPTIONS = ["alerts"]

    def test_api_search(self):
        """
        Search is unavailable for this endpoint.
        """
        pass

    def test_api_get_by_id(self, api_object):
        self._get_object_classifier_test(api_object, "id", self.OBJECT_ID_NAME)
