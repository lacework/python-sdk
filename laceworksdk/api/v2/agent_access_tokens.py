# -*- coding: utf-8 -*-
"""Lacework AgentAccessTokens API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AgentAccessTokensAPI(CrudEndpoint):
    """A class used to represent the `Agent Access Tokens API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AgentAccessTokens>`_

    To connect to the Lacework instance, Lacework agents require an agent access token.
    """

    def __init__(self, session):
        """Initializes the AgentAccessTokensAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            AgentAccessTokensAPI: An  AgentAccessTokensAPI object.

        """
        super().__init__(session, "AgentAccessTokens")

    def create(self, alias, enabled, props=None, **request_params):
        """A method to create a new agent access token.

        Args:
          alias (str): A string representing the name you wish to give to the created token.
          enabled (bool|int): A boolean/integer representing whether the token is enabled.
          props (dict, optional): A dict containing optional values for the following fields:
                                - description(str, optional): a description of the token
                                - os(str, optional): the operating system
                                - subscription(str, optional): The subscription level of the token. Valid values are:
                                "standard", "professional", "enterprise"
          request_params (dict): Use to pass any additional parameters the API

        Returns:
            dict: The new access token
        """
        return super().create(
            token_alias=alias,
            token_enabled=int(bool(enabled)),
            props=props,
            **request_params,
        )

    def get_by_id(self, id):
        """A method to get an agent access token by its ID.

        Args:
          id (str): A string representing the object ID.

        Returns:
            dict: a JSON object containing info regarding the requested access token

        """
        return self.get(id=id)

    def update(self, id, token_enabled=None, props=None, **request_params):
        """A method to update an agent access token.

        Args:
          id (str): A string representing the object ID.
          token_enabled (bool|int, optional): A boolean/integer representing whether the object is enabled.
          props (dict, optional): A dict containing optional values for the following fields:\n

                                - description (str, optional): a description of the token
                                - os (str, optional): the operating system
                                - subscription (str, optional): The subscription level of the token. Valid values are:
                                "standard", "professional", "enterprise"

          request_params (dict): Use to pass any additional parameters the API

        Returns:
            dict: The updated access token.

        """
        if token_enabled is not None:
            token_enabled = int(bool(token_enabled))

        return super().update(
            id=id, token_enabled=token_enabled, props=props, **request_params
        )

    def delete(self):
        """
        Lacework does not currently allow for agent access tokens to be deleted.
        """
