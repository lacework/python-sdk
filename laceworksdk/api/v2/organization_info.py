# -*- coding: utf-8 -*-
"""Lacework OrganizationInfo API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class OrganizationInfoAPI(BaseEndpoint):
    """A class used to represent the `Organization Info API endpoint <https://docs.lacework.net/api/v2/docs/#tag/OrganizationInfo>`_

    Return information about whether the Lacework account is an organization account and, if it is, what the organization account URL is.
    """

    def __init__(self, session):
        """Initializes the OrganizationInfoAPI object.

        Args:
          session: An instance of the HttpSession class

        Returns:
            OrganizationInfoAPI object.

        """
        super().__init__(session, "OrganizationInfo")

    def get(self):
        """A method to get organization info.

        Returns:
            dict: Organization info

        """
        response = self._session.get(self._build_url())

        return response.json()
