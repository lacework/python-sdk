# -*- coding: utf-8 -*-
"""
Lacework Agent Access Token API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class TokenAPI:
    """
    Lacework Agent Access Token API.
    """

    def __init__(self, session):
        """
        Initializes the TokenAPI object.

        :param session: An instance of the HttpSession class

        :return TokenAPI object.
        """

        super().__init__()

        self._session = session

    def create(self,
               alias=None,
               enabled=True,
               description=None):
        """
        A method to create a new agent access token.

        :param alias: A string representing the alias for the agent access token.
        :param enabled: A boolean representing whether the agent access token should be enabled.
        :param description: A string representing a description for the agent access token.

        :return response json
        """

        logger.info("Creating agent access token in Lacework...")

        data = {}

        if alias:
            data["TOKEN_ALIAS"] = alias
        if enabled is not None:
            data["TOKEN_ENABLED"] = int(bool(enabled))
        if description:
            data["PROPS"]["DESCRIPTION"]: description

        # Build the Token API URI
        api_uri = "/api/v1/external/tokens"

        response = self._session.post(api_uri, data=data)

        return response.json()

    def get(self,
            access_token=None):
        """
        A method to get a list of enabled agent access tokens.

        :return response json
        """

        logger.info("Getting agent access tokens from Lacework...")

        # Build the Token API URI
        api_uri = "/api/v1/external/tokens"

        if access_token:
            api_uri += f"/{access_token}"

        response = self._session.get(api_uri)

        return response.json()

    def get_enabled(self):
        """
        A method to get a list of enabled agent access tokens.

        :return response json
        """

        logger.warning("The 'get_enabled' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get()

    def get_token(self,
                  access_token):
        """
        A method to get details about an agent access token.

        :param access_token: A string representing the agent access token to get.

        :return response json
        """

        logger.warning("The 'get_enabled' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get(access_token=access_token)

    def update(self,
               access_token,
               alias=None,
               enabled=True,
               description=None):
        """
        A method to update the details about an agent access token.

        :param access_token: A string representing the agent access token to update.
        :param alias: A string representing the alias for the agent access token.
        :param enabled: A boolean representing whether the agent access token should be enabled.
        :param description: A string representing a description for the agent access token.

        :return response json
        """

        logger.info("Updating agent access token details in Lacework...")

        data = {}

        if alias:
            data["TOKEN_ALIAS"] = alias
        if enabled is not None:
            data["TOKEN_ENABLED"] = int(bool(enabled))
        if description:
            data["PROPS"]["DESCRIPTION"]: description

        # Build the Token API URI
        api_uri = f"/api/v1/external/tokens/{access_token}"

        response = self._session.put(api_uri, data=data)

        return response.json()

    def update_token(self,
                     access_token,
                     token_alias=None,
                     token_enabled=False,
                     token_description=None):
        """
        A method to update the details about an agent access token.

        :param access_token: A string representing the agent access token to update.
        :param token_alias: A string representing the alias for the agent access token.
        :param token_enalbed: A boolean representing whether the agent access token should be enabled.
        :param token_description: A string representing a description for the agent access token.

        :return response json
        """

        logger.warning("The 'update_token' function may be deprecated shortly, please consider switching to 'update'.")

        return self.update(access_token=access_token,
                           alias=token_alias,
                           enabled=token_enabled,
                           description=token_description)
