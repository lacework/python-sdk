# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from datetime import datetime, timedelta, timezone

from laceworksdk.api.queries import QueriesAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase) for _ in range(8))

# Tests


def test_queries_api_object_creation(api):
    assert isinstance(api.queries, QueriesAPI)


def test_cloud_accounts_api_env_object_creation(api_env):
    assert isinstance(api_env.queries, QueriesAPI)


def test_queries_api_get(api):
    response = api.queries.get()
    assert "data" in response.keys()


def test_queries_api_create(api):
    response = api.queries.create(
        evaluator_id="Cloudtrail",
        query_id=RANDOM_TEXT,
        query_text=f"""{RANDOM_TEXT} {{
            source {{CloudTrailRawEvents e}}
            filter {{EVENT_SOURCE = 'iam.amazonaws.com' AND EVENT:userIdentity.name::String NOT LIKE '%{RANDOM_TEXT}'}}
            return distinct {{EVENT_NAME, EVENT}}
            }}"""
    )

    assert "data" in response.keys()


def test_queries_api_get_by_id(api):
    response = api.queries.get_by_id(query_id=RANDOM_TEXT)

    assert "data" in response.keys()


def test_queries_api_update(api):
    response = api.queries.update(
        query_id=RANDOM_TEXT,
        query_text=f"""{RANDOM_TEXT} {{
            source {{CloudTrailRawEvents e}}
            filter {{EVENT_SOURCE = 'iam.amazonaws.com' AND EVENT:userIdentity.name::String NOT LIKE '%{RANDOM_TEXT}_updated'}}
            return distinct {{EVENT_NAME, EVENT}}
            }}"""
    )

    assert "data" in response.keys()


def test_queries_api_execute_by_id(api):
    response = api.queries.execute_by_id(
        query_id=RANDOM_TEXT,
        arguments={
            "StartTimeRange": start_time,
            "EndTimeRange": end_time,
        }
    )

    assert "data" in response.keys()


def test_queries_api_validate(api):
    response = api.queries.get()

    if len(response) > 0:
        query = random.choice(response["data"])

        response = api.queries.validate(evaluator_id=query["evaluatorId"],
                                        query_text=query["queryText"])

        assert "data" in response.keys()


def test_queries_api_delete(api):
    response = api.queries.delete(query_id=RANDOM_TEXT)

    assert response.status_code == 204
