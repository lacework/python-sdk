# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from laceworksdk.api.cloud_accounts import CloudAccountsAPI

INTEGRATION_GUID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


# Tests

def test_cloud_accounts_api_object_creation(api):
    assert isinstance(api.cloud_accounts, CloudAccountsAPI)


def test_cloud_accounts_api_env_object_creation(api_env):
    assert isinstance(api_env.cloud_accounts, CloudAccountsAPI)


def test_cloud_accounts_api_get(api):
    response = api.cloud_accounts.get()
    assert "data" in response.keys()


def test_cloud_accounts_api_get_by_type(api):
    response = api.cloud_accounts.get()

    if len(response) > 0:
        cloud_account_type = random.choice(response["data"])["type"]

        response = api.cloud_accounts.get_by_type(type=cloud_account_type)

        assert "data" in response.keys()


""" def test_cloud_accounts_api_create(api):
    response = api.cloud_accounts.create(
        name=f"AWS Config Test {RANDOM_TEXT}",
        type="AwsCfg",
        enabled=1,
        data={
            "crossAccountCredentials": {
                "externalId": f"{RANDOM_TEXT}",
                "roleArn": f"arn:aws:iam::434813966438:role/lacework-test-{RANDOM_TEXT}"
            }
        }
    )

    assert "data" in response.keys()

    global INTEGRATION_GUID
    INTEGRATION_GUID = response["data"]["intgGuid"]


def test_cloud_accounts_api_get_by_guid(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.cloud_accounts.get_by_guid(guid=INTEGRATION_GUID)

        assert "data" in response.keys()
        assert response["data"]["intgGuid"] == INTEGRATION_GUID """


def test_cloud_accounts_api_search(api):
    response = api.cloud_accounts.search(query_data={
        "filters": [
            {
                "expression": "eq",
                "field": "type",
                "value": "AwsCfg"
            }
        ],
        "returns": [
            "intgGuid"
        ]
    })
    assert "data" in response.keys()


""" def test_cloud_accounts_api_update(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        new_name = f"AWS Config {RANDOM_TEXT} Updated"
        new_enabled = False

        response = api.cloud_accounts.update(
            INTEGRATION_GUID,
            name=new_name,
            enabled=new_enabled
        )

        assert "data" in response.keys()
        assert response["data"]["name"] == new_name
        assert response["data"]["enabled"] == int(new_enabled)


def test_cloud_accounts_api_delete(api):
    assert INTEGRATION_GUID is not None
    if INTEGRATION_GUID:
        response = api.cloud_accounts.delete(INTEGRATION_GUID)
        assert response.status_code == 204 """
