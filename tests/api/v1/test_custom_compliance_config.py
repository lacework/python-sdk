# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v1.custom_compliance_config import CustomComplianceConfigAPI


# Tests

def test_custom_compliance_api_object_creation(api):
    assert isinstance(api.compliance.config, CustomComplianceConfigAPI)


def test_custom_compliance_api_get(api):
    response = api.compliance.config.get()
    assert response["ok"]
