# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v2.schemas import SchemasAPI


# Tests

def test_schemas_api_object_creation(api):
    assert isinstance(api.schemas, SchemasAPI)


def test_schemas_api_env_object_creation(api_env):
    assert isinstance(api_env.schemas, SchemasAPI)


def test_schemas_api_get(api):
    response = api.schemas.get()
    assert len(response) > 0


def test_schemas_api_get_type_schema(api):
    response = api.schemas.get()

    for schema_type in response:
        response = api.schemas.get(type=schema_type)

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


def test_schemas_api_get_subtype_schema(api):
    type = "AlertChannels"
    response = api.schemas.get(type=type)

    for subtype_schema in response["oneOf"]:

        subtype = subtype_schema["properties"]["type"]["enum"][0]

        response = api.schemas.get_by_subtype(type=type, subtype=subtype)
        assert "properties" in response.keys()
