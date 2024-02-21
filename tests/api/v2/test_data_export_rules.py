# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.data_export_rules import DataExportRulesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.data_export_rules


@pytest.fixture(scope="module")
def api_object_create_body(random_text, s3_alert_channel_guid):
    return {
        "type": "Dataexport",
        "filters": {
            "name": f"Test Data Export Rule {random_text}",
            "description": f"Test Data Export Rule Description {random_text}",
            "enabled": 1
        },
        "intg_guid_list": [s3_alert_channel_guid]
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "filters": {
            "name": f"Test Data Export Rule {random_text} (Updated)",
            "enabled": False
        }
    }


class TestDataExportRules(CrudEndpoint):

    OBJECT_ID_NAME = "mcGuid"
    OBJECT_TYPE = DataExportRulesAPI

    @pytest.mark.flaky(reruns=10)   # Because sometimes this attempts to get an object that has just been deleted
    @pytest.mark.order("first")
    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)
