# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.vulnerabilities import (
    ContainerVulnerabilitiesAPI,
    HostVulnerabilitiesAPI,
    SoftwarePackagesAPI,
    VulnerabilitiesAPI
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.vulnerabilities


class TestVulnerabilitesEndpoint(SearchEndpoint):

    OBJECT_TYPE = VulnerabilitiesAPI
    OBJECT_MAP = {
        "containers": ContainerVulnerabilitiesAPI,
        "hosts": HostVulnerabilitiesAPI
    }

    def test_vulnerabilities_containers_api_scan(self, api_object, request):
        response = api_object.containers.scan("index.docker.io",
                                              "alannix/vulnerable-struts",
                                              "latest")

        assert "data" in response.keys()
        if isinstance(response["data"], list):
            scan_request_id = response["data"][0].get("requestId")
        elif isinstance(response["data"], dict):
            scan_request_id = response["data"].get("requestId")

        request.config.cache.set("scan_request_id", scan_request_id)

    def test_vulnerabilities_containers_api_scan_status(self, api_object, request):
        scan_request_id = request.config.cache.get("scan_request_id", None)
        assert scan_request_id is not None
        if scan_request_id:
            response = api_object.containers.status(request_id=scan_request_id)
            assert "data" in response.keys()

            if isinstance(response["data"], list):
                assert "status" in response["data"][0].keys()
            elif isinstance(response["data"], dict):
                assert "status" in response["data"].keys()

    def test_vulnerabilities_packages_api_object_creation(api, api_object):
        assert isinstance(api_object.packages, SoftwarePackagesAPI)

    def test_vulnerabilities_packages_api_scan(api, api_object):
        response = api_object.packages.scan(os_pkg_info_list=[{
            "os": "Ubuntu",
            "osVer": "18.04",
            "pkg": "openssl",
            "pkgVer": "1.1.1-1ubuntu2.1~18.04.5"
        }, {
            "os": "Ubuntu",
            "osVer": "20.04",
            "pkg": "openssl",
            "pkgVer": "1.1.1-1ubuntu2.1~20.04"
        }])
        assert "data" in response.keys()
