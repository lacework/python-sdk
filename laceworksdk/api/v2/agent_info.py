# -*- coding: utf-8 -*-
"""Lacework AgentInfo API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class AgentInfoAPI(SearchEndpoint):
    """A class used to represent the `Agent Info API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AgentInfo>`_

    View and verify information about all agents.
    """

    def __init__(self, session):
        """Initializes the AgentInfo API object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            AgentInfoAPI: an AgentInfoAPI object.
        """
        super().__init__(session, "AgentInfo")
