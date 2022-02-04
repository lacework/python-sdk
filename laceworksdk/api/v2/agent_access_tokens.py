# -*- coding: utf-8 -*-
"""
Lacework AgentAccessTokens API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AgentAccessTokensAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the AgentAccessTokensAPI object.

        :param session: An instance of the HttpSession class

        :return AgentAccessTokensAPI object.
        """

        super().__init__(session, "AgentAccessTokens")

    def create(self,
               alias=None,
               enabled=True,
               **request_params):
        """
        A method to create a new AgentAccessTokens object.

        :param alias: A string representing the object alias.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            token_alias=alias,
            token_enabled=int(bool(enabled)),
            **request_params
        )

    def get_by_id(self,
                  id):
        """
        A method to get an AgentAccessTokens object by ID.

        :param id: A string representing the object ID.

        :return response json
        """

        return self.get(id=id)

    def update(self,
               id,
               token_enabled=None,
               **request_params):
        """
        A method to update an AgentAccessTokens object.

        :param id: A string representing the object ID.
        :param alias: A string representing the object alias.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        if token_enabled is not None:
            token_enabled = int(bool(token_enabled))

        return super().update(
            id=id,
            token_enabled=token_enabled,
            **request_params
        )

    def delete(self):
        """
        A method to 'pass' when attempting to delete an AgentAccessToken object.

        Lacework does not currently allow for agent access tokens to be deleted.
        """
