# -*- coding: utf-8 -*-
"""
Lacework Schemas API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class SchemasAPI(object):
    """
    Lacework Schemas API.
    """

    def __init__(self, session):
        """
        Initializes the SchemasAPI object.

        :param session: An instance of the HttpSession class

        :return SchemasAPI object.
        """

        super(SchemasAPI, self).__init__()

        self._session = session

    def get(self, type=None, subtype=None):
        """
        A method to list all schema types, or fetch a specific schema

        :return response json
        """

        logger.info("Fetching schema info from Lacework...")

        # Build the Schema request URI
        if type and subtype:
            api_uri = f"/api/v2/schemas/{type}/{subtype}"
        elif type:
            api_uri = f"/api/v2/schemas/{type}"
        else:
            api_uri = "/api/v2/schemas"

        response = self._session.get(api_uri)

        return response.json()

    def get_by_subtype(self, type, subtype):
        """
        A method to fetch a specific subtype schema

        :return response json
        """

        return self.get(type=type, subtype=subtype)
