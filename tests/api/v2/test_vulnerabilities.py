# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.v2.vulnerabilities import (
    ContainerVulnerabilitiesAPI,
    HostVulnerabilitiesAPI,
    SoftwarePackagesAPI,
    VulnerabilitiesAPI
)


SCAN_REQUEST_ID = None

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_vulnerabilities_api_object_creation(api):
    assert isinstance(api.vulnerabilities, VulnerabilitiesAPI)


def test_vulnerabilities_containers_api_object_creation(api):
    assert isinstance(api.vulnerabilities.containers, ContainerVulnerabilitiesAPI)


def test_vulnerabilities_containers_api_search_by_date(api):
    response = api.vulnerabilities.containers.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1


def test_vulnerabilities_containers_api_scan(api):
    global SCAN_REQUEST_ID
    response = api.vulnerabilities.containers.scan("index.docker.io",
                                                   "alannix/vulnerable-struts",
                                                   "latest")
    assert "data" in response.keys()
    if isinstance(response["data"], list):
        SCAN_REQUEST_ID = response["data"][0].get("requestId")
    elif isinstance(response["data"], dict):
        SCAN_REQUEST_ID = response["data"].get("requestId")


def test_vulnerabilities_containers_api_scan_status(api):
    if SCAN_REQUEST_ID:
        response = api.vulnerabilities.containers.status(request_id=SCAN_REQUEST_ID)
        assert "data" in response.keys()

        if isinstance(response["data"], list):
            assert "status" in response["data"][0].keys()
        elif isinstance(response["data"], dict):
            assert "status" in response["data"].keys()


def test_vulnerabilities_hosts_api_object_creation(api):
    assert isinstance(api.vulnerabilities.hosts, HostVulnerabilitiesAPI)


def test_vulnerabilities_hosts_api_search_by_date(api):
    response = api.vulnerabilities.hosts.search(json={
        "timeFilters": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    page_count = 0
    for page in response:
        if page_count > 1:
            return
        assert len(page["data"]) == page.get("paging", {}).get("rows")
        page_count += 1


def test_vulnerabilities_packages_api_object_creation(api):
    assert isinstance(api.vulnerabilities.packages, SoftwarePackagesAPI)


def test_vulnerabilities_packages_api_scan(api):
    response = api.vulnerabilities.packages.scan(os_pkg_info_list=[{
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
