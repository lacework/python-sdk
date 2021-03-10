# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""
import json
import pytest
import random

from copy import deepcopy

from laceworksdk.api.custom_policies import CustomPoliciesAPI


LQL_QUERY = (
    '{query_id}(CloudTrailRawEvents e) {{\n'
    '    SELECT INSERT_ID\n'
    '    LIMIT 10\n'
    '}}'
)

CUSTOM_POLICY = {
    "policy_id": None,
    "title": "My Policy Title",
    "enabled": False,
    "policy_type": "AWS",
    "alert_enabled": False,
    "eval_frequency": "Hourly",
    "lql_text": None,
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


@pytest.fixture(scope='session')
def custom_policy(api):
    policy_id = f'lacework-test-{random.randint(0, 1000000)}'
    policy_json = deepcopy(CUSTOM_POLICY)
    policy_json['policy_id'] = policy_id
    policy_json['lql_text'] = LQL_QUERY.format(query_id='LQL')

    yield policy_id, policy_json

    # teardown
    try:
        api.custom_policies.delete(policy_id)
    except Exception:
        pass


class TestCustomPolicies():

    @classmethod
    @pytest.fixture(scope='class', autouse=True)
    def setup_class(cls, request):
        request.cls.created_policy_id = None

    def test_custom_policies_api_object_creation(self, api):
        assert isinstance(api.custom_policies, CustomPoliciesAPI)

    def test_custom_policies_api_env_object_creation(self, api_env):
        assert isinstance(api_env.custom_policies, CustomPoliciesAPI)

    def test_create(self, request, api, custom_policy):
        unused_policy_id, policy_json = custom_policy
        print(json.dumps(policy_json, indent=4))

        response = api.custom_policies.create(policy_json)
        data = response['data'][0]
        request.cls.created_policy_id = data['rule_id']

        assert request.cls.created_policy_id == policy_json['policy_id']
        # assert not any([x for x in list(data) if 'rule' in x])

    def test_enable_disable(self, api):
        # enable
        response = api.custom_policies.enable(self.created_policy_id)
        data = response['data'][0]

        assert data['enabled'] is True
        assert data['alert_enabled'] is False

        # enable alert
        response = api.custom_policies.enable(self.created_policy_id, alert_enabled=True)
        data = response['data'][0]
        
        assert data['enabled'] is True
        assert data['alert_enabled'] is True

        # disable
        response = api.custom_policies.disable(self.created_policy_id)
        data = response['data'][0]
        data = response['data'][0]

        assert data['enabled'] is False
        assert data['alert_enabled'] is True

        # disable alert
        response = api.custom_policies.disable(self.created_policy_id, alert_enabled=False)
        data = response['data'][0]

        assert data['enabled'] is False
        assert data['alert_enabled'] is False

    def test_get(self, api):
        response = api.custom_policies.get()
        data = response['data']

        assert data
        # assert not any([x for x in list(data[0]) if 'rule' in x])

    def test_get_id(self, request, api):
        response = api.custom_policies.get(policy_id=self.created_policy_id)

        assert len(response['data']) == 1

    def test_update(self, api):
        policy_json = {'description': 'My New Description'}

        response = api.custom_policies.update(policy_json, self.created_policy_id)
        data = response['data'][0]

        print(response)

        assert data['description'] == policy_json['description']
        # assert not any([x for x in list(data) if 'rule' in x])

    def test_delete(self, api):
        response = api.custom_policies.delete(self.created_policy_id)

        assert response['message']['ruleDeleted'] == self.created_policy_id
        # assert not any([x for x in list(response['message']) if 'rule' in x])
