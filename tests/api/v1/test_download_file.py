# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v1.download_file import DownloadFileAPI


# Tests

def test_download_file_api_object_creation(api):
    assert isinstance(api.files, DownloadFileAPI)


def test_download_file_api_get(api):
    response = api.files.get("aws-cloudtrail")
    assert response["Metadata"]
