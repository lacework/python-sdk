# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.report_rules import ReportRulesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.report_rules


@pytest.fixture(scope="module")
def api_object_create_body(random_text, email_alert_channel_guid, aws_resource_group_guid):
    return {
        "type": "Report",
        "filters": {
            "name": f"Test Report Rule {random_text}",
            "description": f"Test Report Rule Description {random_text}",
            "enabled": 1,
            "resourceGroups": [aws_resource_group_guid],
            "severity": [1, 2, 3]
        },
        "intg_guid_list": [email_alert_channel_guid],
        "report_notification_types": {
            "awsComplianceEvents": True,
            "awsCisS3": True
        }
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "filters": {
            "name": f"Test Report Rule {random_text} (Updated)",
            "enabled": False
        }
    }


class TestAlertRules(CrudEndpoint):

    OBJECT_ID_NAME = "mcGuid"
    OBJECT_TYPE = ReportRulesAPI

    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)
