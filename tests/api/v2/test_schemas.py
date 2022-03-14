# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.schemas import SchemasAPI
from tests.api.test_base_endpoint import BaseEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.schemas


class TestSchemas(BaseEndpoint):

    OBJECT_ID_NAME = "name"
    OBJECT_TYPE = SchemasAPI

    def test_schemas_api_get(self, api_object):
        response = api_object.get()
        assert len(response) > 0

    def test_schemas_api_get_type_schema(self, api_object):
        response = api_object.get()

        exempt_schemas = [
            "Activities",
            "Configs",
            "Entities",
            "Vulnerabilities"
        ]

        for schema_type in response:
            if schema_type in exempt_schemas:
                continue

            response = api_object.get(type=schema_type)

            if type(response) is dict:
                if len(response) > 0:
                    if "oneOf" in response.keys():
                        for schema in response["oneOf"]:
                            assert "properties" in schema.keys()
                    else:
                        assert "properties" in response.keys()
                else:
                    assert True
            elif type(response) is list:
                assert True
            else:
                assert False

    def test_schemas_api_get_subtype_schema(self, api_object):
        type = "AlertChannels"
        response = api_object.get(type=type)

        for subtype_schema in response["oneOf"]:

            subtype = subtype_schema["properties"]["type"]["enum"][0]

            response = api_object.get_by_subtype(type=type, subtype=subtype)
            assert "properties" in response.keys()
