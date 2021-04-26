# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import os
import random

import pytest

from dotenv import load_dotenv
from laceworksdk.api.compliance import ComplianceAPI

load_dotenv()


# Fixtures

@pytest.fixture()
def gcp_org():
    return os.getenv("GCP_ORG")


# Tests

def test_compliance_api_object_creation(api):
    assert isinstance(api.compliance, ComplianceAPI)


def test_compliance_api_list_gcp_projects(api, gcp_org):
    if gcp_org:
        response = api.compliance.list_gcp_projects(gcp_org)
        assert response["ok"]


def test_compliance_api_get_latest_aws_report(api):
    integrations = api.integrations.get_by_type("AWS_CFG")

    if len(integrations["data"]):
        aws_account = random.choice(integrations["data"])["DATA"]["AWS_ACCOUNT_ID"]
        response = api.compliance.get_latest_aws_report(aws_account_id=aws_account, file_format="json")
        assert response["ok"]


def test_compliance_api_get_latest_gcp_report(api, gcp_org):
    if gcp_org:
        gcp_projects = api.compliance.list_gcp_projects(gcp_org)

        if len(gcp_projects["data"]):
            project_id = random.choice(gcp_projects["data"])
            project_id = random.choice(project_id["projects"]).split()[0]
            response = api.compliance.get_latest_gcp_report(gcp_org, project_id, file_format="json")
            assert response["ok"]
