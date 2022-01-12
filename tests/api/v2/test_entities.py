# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from datetime import datetime, timedelta, timezone

from laceworksdk.api.v2.entities import (
    EntitiesAPI,
    ApplicationsAPI,
    CommandLinesAPI,
    ContainersAPI,
    FilesAPI,
    ImagesAPI,
    InternalIPAddressesAPI,
    K8sPodsAPI,
    MachinesAPI,
    MachineDetailsAPI,
    NetworkInterfacesAPI,
    NewFileHashesAPI,
    PackagesAPI,
    ProcessesAPI,
    UsersAPI
)


SCAN_REQUEST_ID = None

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_entities_api_object_creation(api):
    assert isinstance(api.entities, EntitiesAPI)


def test_entities_applications_api_object_creation(api):
    assert isinstance(api.entities.applications, ApplicationsAPI)


def test_entities_applications_api_search_by_date(api):
    response = api.entities.applications.search(json={
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


def test_entities_command_lines_api_object_creation(api):
    assert isinstance(api.entities.command_lines, CommandLinesAPI)


def test_entities_command_lines_api_search_by_date(api):
    response = api.entities.command_lines.search(json={
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


def test_entities_containers_api_object_creation(api):
    assert isinstance(api.entities.containers, ContainersAPI)


def test_entities_containers_api_search_by_date(api):
    response = api.entities.containers.search(json={
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


def test_entities_files_api_object_creation(api):
    assert isinstance(api.entities.files, FilesAPI)


def test_entities_files_api_search_by_date(api):
    response = api.entities.files.search(json={
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


def test_entities_images_api_object_creation(api):
    assert isinstance(api.entities.images, ImagesAPI)


def test_entities_images_api_search_by_date(api):
    response = api.entities.images.search(json={
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


def test_entities_internal_ip_addresses_api_object_creation(api):
    assert isinstance(api.entities.internal_ip_addresses, InternalIPAddressesAPI)


def test_entities_internal_ip_addresses_api_search_by_date(api):
    response = api.entities.internal_ip_addresses.search(json={
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


def test_entities_k8s_pods_api_object_creation(api):
    assert isinstance(api.entities.k8s_pods, K8sPodsAPI)


def test_entities_k8s_pods_api_search_by_date(api):
    response = api.entities.k8s_pods.search(json={
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


def test_entities_machines_api_object_creation(api):
    assert isinstance(api.entities.machines, MachinesAPI)


def test_entities_machines_api_search_by_date(api):
    response = api.entities.machines.search(json={
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


def test_entities_machine_details_api_object_creation(api):
    assert isinstance(api.entities.machine_details, MachineDetailsAPI)


def test_entities_machine_details_api_search_by_date(api):
    response = api.entities.machine_details.search(json={
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


def test_entities_network_interfaces_api_object_creation(api):
    assert isinstance(api.entities.network_interfaces, NetworkInterfacesAPI)


def test_entities_network_interfaces_api_search_by_date(api):
    response = api.entities.network_interfaces.search(json={
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


def test_entities_new_file_hashes_api_object_creation(api):
    assert isinstance(api.entities.new_file_hashes, NewFileHashesAPI)


def test_entities_new_file_hashes_api_search_by_date(api):
    response = api.entities.new_file_hashes.search(json={
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


def test_entities_packages_api_object_creation(api):
    assert isinstance(api.entities.packages, PackagesAPI)


def test_entities_packages_api_search_by_date(api):
    response = api.entities.packages.search(json={
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


def test_entities_processes_api_object_creation(api):
    assert isinstance(api.entities.processes, ProcessesAPI)


def test_entities_processes_api_search_by_date(api):
    response = api.entities.processes.search(json={
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


def test_entities_users_api_object_creation(api):
    assert isinstance(api.entities.users, UsersAPI)


def test_entities_users_api_search_by_date(api):
    response = api.entities.users.search(json={
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
