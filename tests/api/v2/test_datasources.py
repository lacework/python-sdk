# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.datasources import DatasourcesAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.datasources


class TestDatasources(BaseEndpoint):

    OBJECT_ID_NAME = "name"
    OBJECT_TYPE = DatasourcesAPI

    def test_api_get(self, api_object):
        response = api_object.get()
        assert "data" in response.keys()

    def test_get_datasource(self, api_object):
        response = api_object.get_datasource("LW_CFG_AZURE_NETWORK_APPLICATIONGATEWAYS")
        assert "data" in response.keys()

    def test_list_data_sources(self, api_object):
        response = api_object.list_data_sources()
        assert isinstance(response[0], tuple)