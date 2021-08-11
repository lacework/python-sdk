# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random
import string

from datetime import datetime, timedelta, timezone

from laceworksdk.api.policies import PoliciesAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=6)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

POLICY_ID = None
RANDOM_TEXT = "".join(random.choice(string.ascii_uppercase) for _ in range(8))

# Tests


def test_policies_api_object_creation(api):
    assert isinstance(api.policies, PoliciesAPI)


def test_cloud_accounts_api_env_object_creation(api_env):
    assert isinstance(api_env.policies, PoliciesAPI)


def test_policies_api_get(api):
    response = api.policies.get()
    assert "data" in response.keys()


def test_policies_api_create(api):
    queries = api.queries.get()

    if len(queries) > 0:
        query = random.choice(queries["data"])

        response = api.policies.create(
            policy_type="Violation",
            query_id=query["queryId"],
            enabled=True,
            title=RANDOM_TEXT,
            description=f"{RANDOM_TEXT} description",
            remediation="Policy remediation",
            severity="high",
            alert_enabled=True,
            alert_profile="LW_CloudTrail_Alerts",
            evaluator_id=query["evaluatorId"]
        )

        global POLICY_ID
        POLICY_ID = response["data"]["policyId"]

        assert "data" in response.keys()


def test_policies_api_get_by_id(api):
    assert POLICY_ID is not None
    if POLICY_ID:
        response = api.policies.get_by_id(policy_id=POLICY_ID)

        assert "data" in response.keys()


def test_policies_api_update(api):
    assert POLICY_ID is not None
    if POLICY_ID:
        response = api.policies.update(
            policy_id=POLICY_ID,
            enabled=False
        )

        assert "data" in response.keys()
        assert response["data"]["enabled"] is False


def test_policies_api_delete(api):
    assert POLICY_ID is not None
    if POLICY_ID:
        response = api.policies.delete(policy_id=POLICY_ID)

        assert response.status_code == 204
