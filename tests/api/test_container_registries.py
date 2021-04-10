# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.container_registries import ContainerRegistriesAPI

INTEGRATION_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_container_registries_api_object_creation(api):
    assert isinstance(api.container_registries, ContainerRegistriesAPI)


def test_container_registries_api_env_object_creation(api_env):
    assert isinstance(api_env.container_registries, ContainerRegistriesAPI)


def test_container_registries_api_get(api):
    response = api.container_registries.get()
    assert "data" in response.keys()


def test_container_registries_api_get_by_type(api):
    response = api.container_registries.get()

    if len(response) > 0:
        cloud_account_type = random.choice(response["data"])["type"]

        response = api.container_registries.get_by_type(type=cloud_account_type)

        assert "data" in response.keys()


def test_container_registries_api_create(api):
    response = api.container_registries.create(
        name=f"Docker Hub Test {RANDOM_TEXT}",
        type="ContVulnCfg",
        enabled=1,
        data={
            "registryType": "INLINE_SCANNER"
        }
    )

    assert "data" in response.keys()

    global INTEGRATION_GUID
    INTEGRATION_GUID = response["data"]["intgGuid"]


def test_container_registries_api_get_by_guid(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.container_registries.get_by_guid(guid=INTEGRATION_GUID)

        assert "data" in response.keys()
        assert response["data"]["intgGuid"] == INTEGRATION_GUID


def test_container_registries_api_search(api):
    response = api.container_registries.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "type",
                "value": "ContVulnCfg"
            }
        ],
        "returns": [
            "intgGuid"
        ]
    })
    assert "data" in response.keys()


def test_container_registries_api_update(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        new_name = f"Docker Hub Test {RANDOM_TEXT} Updated"
        new_enabled = False

        response = api.container_registries.update(
            INTEGRATION_GUID,
            name=new_name,
            enabled=new_enabled
        )

        assert "data" in response.keys()
        assert response["data"]["name"] == new_name
        assert response["data"]["enabled"] == int(new_enabled)


def test_container_registries_api_delete(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.container_registries.delete(INTEGRATION_GUID)
        assert response.status_code == 204
