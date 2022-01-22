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

    def search(self,
               json=None,
               query_data=None):
        """
        A method to search AgentAccessTokens objects.

        :param json: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        return super().search(json=json, query_data=query_data)

    def update(self,
               id,
               alias=None,
               enabled=None,
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

        return super().update(
            id=id,
            token_alias=alias,
            token_enabled=int(bool(enabled)),
            **request_params
        )

    def delete(self):
        pass
