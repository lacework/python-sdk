# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from laceworksdk.api.v2.datasources import DatasourcesAPI


# Tests

def test_datasources_api_object_creation(api):
    assert isinstance(api.datasources, DatasourcesAPI)


def test_datasources_api_get(api):
    response = api.datasources.get()
    assert "data" in response.keys()


def test_datasources_api_get_type(api):
    response = api.datasources.get()

    if len(response) > 0:
        datasource_type = random.choice(response["data"])["name"]

        response = api.datasources.get_by_type(type=datasource_type)

        assert "data" in response.keys()
