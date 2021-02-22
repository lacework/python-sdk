# -*- coding: utf-8 -*-
"""
Lacework Agent Access Tokens API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class AgentAccessTokensAPI(object):
    """
    Lacework Agent Access Tokens API.
    """

    def __init__(self, session):
        """
        Initializes the AgentAccessTokensAPI object.

        :param session: An instance of the HttpSession class

        :return AgentAccessTokensAPI object.
        """

        super(AgentAccessTokensAPI, self).__init__()

        self._session = session

    def create(self,
               alias,
               enabled=True,
               org=False):
        """
        A method to create a new agent access token.

        :param alias: A string representing the alias of the agent access token.
        :param enabled: A boolean/integer representing whether the agent access token is enabled.
            (0 or 1)
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating agent access token in Lacework...")

        # Build the Agent Access Tokens request URI
        api_uri = "/api/v2/AgentAccessTokens"

        data = {
            "tokenAlias": alias,
            "tokenEnabled": int(bool(enabled))
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            id=None,
            org=False):
        """
        A method to get agent access tokens.

        :param id: A string representing the agent access token ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting agent access token info from Lacework...")

        # Build the Agent Access Tokens request URI
        if id:
            api_uri = f"/api/v2/AgentAccessTokens/{id}"
        else:
            api_uri = "/api/v2/AgentAccessTokens"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_id(self,
                  id,
                  org=False):
        """
        A method to get an agent access token by ID.

        :param id: A string representing the agent access token ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(id=id, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search agent access tokens.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching agent access tokens from Lacework...")

        # Build the Agent Access Tokens request URI
        api_uri = "/api/v2/AgentAccessTokens/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               id,
               alias=None,
               enabled=None,
               org=False):
        """
        A method to update an agent access token.

        :param id: A string representing the agent access token ID.
        :param alias: A string representing the alias of the agent access token.
        :param enabled: A boolean/integer representing whether the agent access token is enabled.
            (0 or 1)
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating agent access token in Lacework...")

        # Build the Agent Access Tokens request URI
        api_uri = f"/api/v2/AgentAccessTokens/{id}"

        tmp_data = {}

        if alias:
            tmp_data["tokenAlias"] = alias
        if enabled is not None:
            tmp_data["tokenEnabled"] = int(bool(enabled))

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()
