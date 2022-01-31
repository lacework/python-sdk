# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v1.run_reports import RunReportsAPI


# Tests

def test_run_reports_api_object_creation(api):
    assert isinstance(api.run_reports, RunReportsAPI)


@pytest.mark.ci_exempt
def test_run_reports_api_aws(api):
    aws_integrations = api.integrations.get_by_type("AWS_CFG")

    for integration in aws_integrations["data"]:
        if integration["ENABLED"]:
            aws_account_id = integration["DATA"]["AWS_ACCOUNT_ID"]
            response = api.run_reports.aws(aws_account_id)
            assert response


@pytest.mark.ci_exempt
def test_run_reports_api_gcp(api):
    gcp_integrations = api.integrations.get_by_type("GCP_CFG")

    for integration in gcp_integrations["data"]:
        if integration["ENABLED"]:
            gcp_project_id = integration["DATA"]["ID"]
            response = api.run_reports.gcp(gcp_project_id)
            assert response


@pytest.mark.ci_exempt
def test_run_reports_api_integration(api):
    integrations = api.integrations.get_by_type("AZURE_CFG")

    for integration in integrations["data"]:
        if integration["ENABLED"]:
            integration_id = integration["INTG_GUID"]
            response = api.run_reports.integration(integration_id)
            assert response
