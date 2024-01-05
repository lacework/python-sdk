# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.entities import (
    EntitiesAPI,
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.entities


class TestEntitiesEndpoint(SearchEndpoint):

    OBJECT_TYPE = EntitiesAPI
    OBJECT_MAP = {
        "applications": EntitiesAPI.ApplicationsAPI,
        "command_lines": EntitiesAPI.CommandLinesAPI,
        "containers": EntitiesAPI.ContainersAPI,
        "files": EntitiesAPI.FilesAPI,
        "images": EntitiesAPI.ImagesAPI,
        "internal_ip_addresses": EntitiesAPI.InternalIPAddressesAPI,
        "k8s_pods": EntitiesAPI.K8sPodsAPI,
        "machines": EntitiesAPI.MachinesAPI,
        "machine_details": EntitiesAPI.MachineDetailsAPI,
        "network_interfaces": EntitiesAPI.NetworkInterfacesAPI,
        "new_file_hashes": EntitiesAPI.NewFileHashesAPI,
        "packages": EntitiesAPI.PackagesAPI,
        "processes": EntitiesAPI.ProcessesAPI,
        "users": EntitiesAPI.UsersAPI
    }
