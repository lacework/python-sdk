# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v2.organization_info import OrganizationInfoAPI


# Tests

def test_organization_info_api_object_creation(api):
    assert isinstance(api.organization_info, OrganizationInfoAPI)


def test_organization_info_api_get(api):
    response = api.organization_info.get()
    assert len(response) > 0
