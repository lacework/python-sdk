# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.v1.recommendations import RecommendationsAPI


# Tests

def test_recommendations_api_object_creation(api):
    assert isinstance(api.recommendations, RecommendationsAPI)


def test_recommendations_api_env_object_creation(api_env):
    assert isinstance(api_env.recommendations, RecommendationsAPI)


def test_recommendations_api_get_aws(api):
    response = api.recommendations.get(type="aws")
    assert response["ok"]


def test_recommendations_api_get_gcp(api):
    response = api.recommendations.get(type="gcp")
    assert response["ok"]


def test_recommendations_api_update_aws(api):
    data = {
        "LW_S3_1": "disable"
    }
    response = api.recommendations.update(type="aws", data=data)
    assert response["ok"]
    data = {
        "LW_S3_1": "enable"
    }
    response = api.recommendations.update(type="aws", data=data)
    assert response["ok"]
