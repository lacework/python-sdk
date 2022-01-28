# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

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
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.entities


class TestEntitiesEndpoint(SearchEndpoint):

    OBJECT_TYPE = EntitiesAPI
    OBJECT_MAP = {
        "applications": ApplicationsAPI,
        "command_lines": CommandLinesAPI,
        "containers": ContainersAPI,
        "files": FilesAPI,
        "images": ImagesAPI,
        "internal_ip_addresses": InternalIPAddressesAPI,
        "k8s_pods": K8sPodsAPI,
        "machines": MachinesAPI,
        "machine_details": MachineDetailsAPI,
        "network_interfaces": NetworkInterfacesAPI,
        "new_file_hashes": NewFileHashesAPI,
        "packages": PackagesAPI,
        "processes": ProcessesAPI,
        "users": UsersAPI
    }
