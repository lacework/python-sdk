# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from laceworksdk.api.v2.agent_info import (
    AgentInfoAPI
)
from tests.api.test_search_endpoint import SearchEndpoint

# Tests


@pytest.fixture(scope="module")
def api_object(api):
    return api.agent_info


class TestConfigsEndpoint(SearchEndpoint):

    OBJECT_TYPE = AgentInfoAPI
