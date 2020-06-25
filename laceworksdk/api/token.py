# -*- coding: utf-8 -*-
"""
Lacework Token API wrapper.
"""

import json
import logging

logger = logging.getLogger(__name__)


class TokenAPI(object):
    """
    Lacework Token API.
    """

    def __init__(self, session):
        """
        Initializes the TokenAPI object.

        :param session: An instance of the HttpSession class

        :return TokenAPI object.
        """

        super(TokenAPI, self).__init__()

        self._session = session

    def get_enabled(self):
        """
        A method to get a list of enabled API credentials.

        :return response json
        """

        logger.info("Getting enabled API credentials from Lacework...")

        # Build the Token API URI
        api_uri = f"/api/v1/external/tokens"

        # GET to retreieve the enabled API credentials
        response = self._session.get(api_uri)

        return response.json()

    def create(self,
               token_alias=None,
               token_enabled=False,
               token_description=None):
        """
        A method to create a new set of API credentials.

        :param token_alias: A string representing the alias for the credentials.
        :param token_enabled: A boolean representing whether the credentials should be enabled.
        :param token_description: A string representing a description for the credentials.

        :return response json
        """

        logger.info("Creating API credential in Lacework...")

        data = {}

        if token_alias:
            data["TOKEN_ALIAS"] = token_alias

        if token_enabled:
            data["TOKEN_ENABLED"] = 1
        else:
            data["TOKEN_ENABLED"] = 0

        if token_description:
            data["PROPS"]["DESCRIPTION"]: token_description

        # Build the Token API URI
        api_uri = f"/api/v1/external/tokens"

        # POST to create an API credential
        response = self._session.post(api_uri, data=data)

        return response.json()

    def get_token(self, access_token):
        """
        A method to get details about an API credential.

        :param access_token: A string representing the access token to get.

        :return response json
        """

        logger.info("Getting API credential details from Lacework...")

        # Build the Token API URI
        api_uri = f"/api/v1/external/tokens/{access_token}"

        # GET to retreieve the API credential
        response = self._session.get(api_uri)

        return response.json()

    def update_token(self,
                     access_token,
                     token_alias=None,
                     token_enabled=False,
                     token_description=None):
        """
        A method to update the details about an API credential.

        :param access_token: A string representing the access token to update.
        :param token_alias: A string representing the alias for the credentials.
        :param token_enalbed: A boolean representing whether the credentials should be enabled.
        :param token_description: A string representing a description for the credentials.

        :return response json
        """

        logger.info("Updating API credential details in Lacework...")

        data = {}

        if token_alias:
            data["TOKEN_ALIAS"] = token_alias

        if token_enabled:
            data["TOKEN_ENABLED"] = 1
        else:
            data["TOKEN_ENABLED"] = 0

        if token_description:
            data["PROPS"]["DESCRIPTION"]: token_description

        # Build the Token API URI
        api_uri = f"/api/v1/external/tokens/{access_token}"

        # PUT to update an API credential
        response = self._session.put(api_uri, data=data)

        return response.json()
