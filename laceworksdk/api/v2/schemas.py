# -*- coding: utf-8 -*-
"""Lacework Schemas API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class SchemasAPI(BaseEndpoint):
    """A class used to represent the `Schemas API endpoint <https://docs.lacework.net/api/v2/docs/#tag/SCHEMAS>`_

    Get details about the available Lacework schemas.
    """

    def __init__(self, session):
        """Initializes the SchemasAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            SchemasAPI: An instance of this class
        """
        super().__init__(session, "schemas")

    def get(self, type=None, subtype=None):
        """A method to get schema objects. Using no args will get all schemas.

        Args:
          type (str, optional): The schema type to retrieve. Valid values are any API resource listed in the Lacework API\
          `documentation <https://docs.lacework.net/api/v2/docs/>`_ .Examples include "AlertChannels", "CloudAccounts", \
          "AgentAccessTokens", etc..
          subtype (str, optional): The subtype to retrieve. Subtypes are only available for API resources that have \
          "type" like fields. For instance the "AlertChannels" resource has subtypes such as "AwsS3", "SlackChannel", \
          etc. See the Lacework API `documentation <https://docs.lacework.net/api/v2/docs/>`_ for more info.

        Returns:
            dict: The requested schema

        """
        response = self._session.get(self._build_url(id=subtype, resource=type))

        return response.json()

    def get_by_subtype(self, type, subtype):
        """A method to fetch a specific subtype schema.
        
        Args:
          type (str): The schema type to retrieve. Valid values are any API resource listed in the Lacework API\
          `documentation <https://docs.lacework.net/api/v2/docs/>`_ .Examples include "AlertChannels", "CloudAccounts", \
          "AgentAccessTokens", etc..
          subtype (str): The subtype to retrieve. Subtypes are only available for API resources that have \
          "type" like fields. For instance the "AlertChannels" resource has subtypes such as "AwsS3", "SlackChannel", \
          etc. See the Lacework API `documentation <https://docs.lacework.net/api/v2/docs/>`_ for more info.

        Returns:
            dict: The requested schema
        """
        return self.get(type=type, subtype=subtype)
