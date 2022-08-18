# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

import pytest

from laceworksdk.api.v2.reports import ReportsAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.reports


@pytest.fixture(scope="module")
def aws_account(api):
    cloud_accounts = api.cloud_accounts.get_by_type("AwsCfg")

    if len(cloud_accounts["data"]):
        aws_role = random.choice(cloud_accounts["data"])["data"]["crossAccountCredentials"]["roleArn"]
        aws_account = aws_role.split(":")[4]
        return aws_account


class TestReports(BaseEndpoint):

    OBJECT_TYPE = ReportsAPI

    def test_api_get_aws_soc2_json(self, api_object, aws_account):
        if aws_account:
            response = api_object.get(
                primary_query_id=aws_account,
                format="json",
                type="COMPLIANCE",
                report_type="AWS_SOC_Rev2",
                template_name="DEFAULT",
                latest=True
            )
            assert "data" in response.keys()

    @pytest.mark.flaky_test
    def test_api_get_aws_soc2_html(self, api_object, aws_account):
        if aws_account:
            response = api_object.get(
                primary_query_id=aws_account,
                format="html",
                type="COMPLIANCE",
                report_type="AWS_SOC_Rev2",
                template_name="DEFAULT",
                latest=True
            )
            assert "<!DOCTYPE html>".encode("utf-8") in response
