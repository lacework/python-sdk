# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

import pytest

from laceworksdk.api.v2.queries import QueriesAPI
from tests.api.test_crud_endpoint import CrudEndpoint


# Tests

@pytest.fixture(scope="module")
def api_object(api):
    return api.queries


@pytest.fixture(scope="module")
def api_object_create_body(random_text):
    return {
        "query_id": random_text,
        "query_text": f"""{random_text} {{
            source {{CloudTrailRawEvents e}}
            filter {{EVENT_SOURCE = 'iam.amazonaws.com' AND EVENT:userIdentity.name::String NOT LIKE '%{random_text}'}}
            return distinct {{EVENT_NAME, EVENT}}
        }}"""
    }


@pytest.fixture(scope="module")
def api_object_update_body(random_text):
    return {
        "query_text": f"""{random_text} {{
            source {{CloudTrailRawEvents e}}
            filter {{EVENT_SOURCE = 'iam.amazonaws.com' AND EVENT:userIdentity.name::String NOT LIKE '%{random_text}_updated'}}
            return distinct {{EVENT_NAME, EVENT}}
        }}"""
    }


@pytest.fixture(scope="module")
def query(api):
    queries = api.queries.get()
    queries = list(filter(lambda elem: elem["owner"] == "Lacework" and "LW_Global_AWS_CTA" in elem["queryId"], queries["data"]))
    query = random.choice(queries)
    return query


class TestQueries(CrudEndpoint):

    OBJECT_ID_NAME = "queryId"
    OBJECT_TYPE = QueriesAPI

    def test_api_get_by_id(self, api_object):
        self._get_object_classifier_test(api_object, "id", self.OBJECT_ID_NAME)

    def test_queries_api_execute_by_id(self, api_object, query):
        start_time, end_time = self._get_start_end_times()
        response = api_object.execute_by_id(
            query_id=query["queryId"],
            arguments={
                "StartTimeRange": start_time,
                "EndTimeRange": end_time,
            }
        )
        assert "data" in response.keys()

    def test_queries_api_validate(self, api_object, query):
        response = api_object.validate(query_text=query["queryText"])
        assert "data" in response.keys()

    def test_api_search(self):
        pass
