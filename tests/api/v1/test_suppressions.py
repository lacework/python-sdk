# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from laceworksdk.api.suppressions import SuppressionsAPI


# Tests


suppression_data = {
    "recommendationExceptions": {
        "LW_S3_1": [
            {
                "accountIds": ["ALL_ACCOUNTS"],
                "regionNames": ["ALL_REGIONS"],
                "resourceNames": ["public-*"],
                "resourceTags": [
                    {
                        "key": "DataAccess",
                        "value": "Public"
                    }
                ],
                "comments": "Suppress properly named/tagged buckets."
            }
        ]
    }
}


def test_suppressions_api_object_creation(api):
    assert isinstance(api.suppressions, SuppressionsAPI)


def test_suppressions_api_env_object_creation(api_env):
    assert isinstance(api_env.suppressions, SuppressionsAPI)


def test_suppressions_api_get_aws(api):
    response = api.suppressions.get(type="aws")
    assert response["ok"]


def test_suppressions_api_get_aws_rec(api):
    response = api.suppressions.get(type="aws", recommendation_id="LW_S3_1")
    assert response["ok"]


def test_suppressions_api_get_gcp(api):
    response = api.suppressions.get(type="gcp")
    assert response["ok"]


def test_suppressions_api_create_aws(api):
    response = api.suppressions.create(type="aws", data=suppression_data)
    assert response["ok"]


def test_suppressions_api_delete_aws(api):
    response = api.suppressions.delete(type="aws", data=suppression_data)
    assert response.status_code == 204
