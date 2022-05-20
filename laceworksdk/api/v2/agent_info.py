# -*- coding: utf-8 -*-
"""
Lacework AgentInfo API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class AgentInfoAPI(SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the AgentInfo API object.

        :param session: An instance of the HttpSession class

        :return AgentInfoAPI object.
        """

        super().__init__(session, "AgentInfo")
