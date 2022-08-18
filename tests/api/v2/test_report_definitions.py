# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

import pytest

from laceworksdk.api.v2.report_definitions import ReportDefinitionsAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.report_definitions


@pytest.fixture(scope="module")
def aws_account(api):
    cloud_accounts = api.cloud_accounts.get_by_type("AwsCfg")

    if len(cloud_accounts["data"]):
        aws_role = random.choice(cloud_accounts["data"])["data"]["crossAccountCredentials"]["roleArn"]
        aws_account = aws_role.split(":")[4]
        return aws_account


@pytest.fixture(scope="module")
def api_object_create_body(random_text, aws_resource_group_guid, email_alert_channel_guid):
    return {
        "report_name": f"Test_{random_text}_Report",
        "report_type": "COMPLIANCE",
        "sub_report_type": "AWS",
        "report_definition": {
            "sections": [
                {
                    "category": "1",
                    "title": "Critical policies collection",
                    "policies": [
                        "AWS_CIS_1_1"
                    ]
                }
            ],
            "overrides": [
                {
                    "title": "Non `root` user authentication violation",
                    "policy": "AWS_CIS_1_1"
                }
            ]
        },
        "props": {
            "resourceGroups": [
                aws_resource_group_guid
            ]
        },
        "alert_channels": [
            email_alert_channel_guid
        ],
        "distribution_type": "pdf",
        "frequency": "daily"
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "report_name": f"Test_{random_text}_Report",
        "report_type": "COMPLIANCE",
        "sub_report_type": "AWS",
        "report_definition": {
            "sections": [
                {
                    "category": "1",
                    "title": "Critical policies collection",
                    "policies": [
                        "AWS_CIS_1_1"
                    ]
                }
            ],
            "overrides": [
                {
                    "title": "Non `root` user authentication violation",
                    "policy": "AWS_CIS_1_1"
                }
            ]
        },
        "frequency": "weekly",
        "update_type": "Update"
    }


@pytest.mark.flaky_test
class TestAlertProfiles(CrudEndpoint):

    OBJECT_ID_NAME = "reportDefinitionGuid"
    OBJECT_TYPE = ReportDefinitionsAPI
    OBJECT_PARAM_EXCEPTIONS = ["alerts"]

    def test_api_search(self):
        """
        Search is unavailable for this endpoint.
        """
        pass

    def test_api_get_by_id(self, api_object):
        self._get_object_classifier_test(api_object, "id", self.OBJECT_ID_NAME)
