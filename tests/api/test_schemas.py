# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.schemas import SchemasAPI


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
            assert 'oneOf' in response.keys()
        elif type(response) is list:
            assert len(response) > 0


def test_schemas_api_get_subtype_schema(api):
    type = "AlertChannels"
    response = api.schemas.get(type=type)

    for subtype in response["oneOf"][0]["properties"]["type"]["enum"]:
        response = api.schemas.get_by_subtype(type=type, subtype=subtype)
        assert 'required' in response.keys()
