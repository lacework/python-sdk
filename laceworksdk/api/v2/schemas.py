# -*- coding: utf-8 -*-
"""
Lacework Schemas API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class SchemasAPI(BaseEndpoint):
    """
    Lacework Schemas API.
    """

    def __init__(self, session):
        """
        Initializes the SchemasAPI object.

        :param session: An instance of the HttpSession class

        :return SchemasAPI object.
        """

        super().__init__(session, "schemas")

    def get(self,
            type=None,
            subtype=None):
        """
        A method to get schema objects.

        :param guid: A string representing the object type.
        :param type: A string representing the object subtype.

        :return response json
        """

        response = self._session.get(self.build_url(id=subtype, resource=type))

        return response.json()

    def get_by_subtype(self,
                       type,
                       subtype):
        """
        A method to fetch a specific subtype schema

        :return response json
        """

        return self.get(type=type, subtype=subtype)
