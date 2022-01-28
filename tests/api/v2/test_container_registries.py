# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.container_registries import ContainerRegistriesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.container_registries


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "name": f"Docker Hub Test {random_text}",
        "type": "ContVulnCfg",
        "enabled": 1,
        "data": {
            "registryType": "INLINE_SCANNER"
        }
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "name": f"Docker Hub Test {random_text} Updated",
        "enabled": 0
    }


class TestContainerRegistries(CrudEndpoint):

    OBJECT_ID_NAME = "intgGuid"
    OBJECT_TYPE = ContainerRegistriesAPI

    def test_api_get_by_guid(self, api_object):
        self._get_object_classifier_test(api_object, "guid", self.OBJECT_ID_NAME)

    def test_api_get_by_type(self, api_object):
        self._get_object_classifier_test(api_object, "type")
