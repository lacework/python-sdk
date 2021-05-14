# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""
import pytest
import re
from copy import deepcopy

from laceworksdk.api.lql_policies import LqlPoliciesAPI


CUSTOM_POLICY = {
    "policy_id": None,
    "title": "My Policy Title",
    "enabled": False,
    "policy_type": "Violation",
    "alert_enabled": False,
    "eval_frequency": "Hourly",
    "lql_id": None,
    "limit": 100,
    "severity": "high",
    "description": "My Policy Description",
    "remediation": "Check yourself...",
    "properties": {
        "policy_tags": [
            "activity",
            "aws",
            "database"
        ]
    }
}


@pytest.fixture(scope='module')
def construct_lql_policy(create_lql_query):
    rand, query_id, unused_query_json, unused_response = create_lql_query

    policy_id = f'lacework-test-{rand}'
    policy_json = deepcopy(CUSTOM_POLICY)
    policy_json['policy_id'] = policy_id
    policy_json['lql_id'] = query_id

    yield policy_id, policy_json


@pytest.fixture(scope='module')
def create_lql_policy(api, construct_lql_policy):
    policy_id, policy_json = construct_lql_policy

    response = api.lql_policies.create(policy_json)

    yield policy_id, policy_json, response

    # teardown
    try:
        api.lql_policies.delete(policy_id)
    except Exception:
        pass


def test_lql_policies_api_object_creation(api):
    assert isinstance(api.lql_policies, LqlPoliciesAPI)


def test_lql_policies_api_env_object_creation(api_env):
    assert isinstance(api_env.lql_policies, LqlPoliciesAPI)


def test_create(request, api, create_lql_policy):
    policy_id, unused_policy_json, response = create_lql_policy

    data = response['data'][0]

    assert data['policy_id'] == policy_id
    assert not any([x for x in list(data) if 'rule' in x])


def test_create_no_id(api, construct_lql_policy):
    unused_policy_id, policy_json = construct_lql_policy
    del policy_json['policy_id']

    response = api.lql_policies.create(policy_json)
    data = response['data'][0]

    assert re.match(r'^\w+-default-\d+$', data['policy_id'])

    try:
        api.lql_policies.delete(data['policy_id'])
    except Exception:
        pass


def test_enable_disable(api, create_lql_policy):
    policy_id, unused_policy_json, unused_response = create_lql_policy

    # enable
    response = api.lql_policies.enable(policy_id)
    data = response['data'][0]

    assert data['enabled'] is True
    assert data['alert_enabled'] is False

    # enable alert
    response = api.lql_policies.enable(policy_id, alert_enabled=True)
    data = response['data'][0]

    assert data['enabled'] is True
    assert data['alert_enabled'] is True

    # disable
    response = api.lql_policies.disable(policy_id)
    data = response['data'][0]
    data = response['data'][0]

    assert data['enabled'] is False
    assert data['alert_enabled'] is True

    # disable alert
    response = api.lql_policies.disable(policy_id, alert_enabled=False)
    data = response['data'][0]

    assert data['enabled'] is False
    assert data['alert_enabled'] is False


def test_get(api):
    response = api.lql_policies.get()
    data = response['data']

    assert data
    assert not any([x for x in list(data[0]) if 'rule' in x])


def test_get_id(request, api, create_lql_policy):
    policy_id, unused_policy_json, unused_response = create_lql_policy

    response = api.lql_policies.get(policy_id=policy_id)

    assert len(response['data']) == 1


def test_update(api, create_lql_policy):
    policy_id, policy_json, unused_response = create_lql_policy

    policy_json = {'description': 'My New Description'}

    response = api.lql_policies.update(policy_json, policy_id)
    data = response['data'][0]

    print(response)

    assert data['description'] == policy_json['description']
    assert not any([x for x in list(data) if 'rule' in x])


def test_delete(api, create_lql_policy):
    policy_id, unused_policy_json, unused_response = create_lql_policy

    response = api.lql_policies.delete(policy_id)

    assert response['message']['policyDeleted'] == policy_id
    assert not any([x for x in list(response['message']) if 'rule' in x])
