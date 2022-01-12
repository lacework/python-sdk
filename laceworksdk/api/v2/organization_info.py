# -*- coding: utf-8 -*-
"""
Lacework OrganizationInfo API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class OrganizationInfoAPI(BaseEndpoint):

    def __init__(self, session):
        """
        Initializes the OrganizationInfoAPI object.

        :param session: An instance of the HttpSession class

        :return OrganizationInfoAPI object.
        """

        super().__init__(session, "OrganizationInfo")

    def get(self):
        """
        A method to get OrganizationInfo object.

        :return response json
        """

        response = self._session.get(self.build_url())

        return response.json()
