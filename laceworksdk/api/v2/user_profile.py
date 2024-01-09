# -*- coding: utf-8 -*-
"""Lacework UserProfile API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class UserProfileAPI(BaseEndpoint):
    """A class used to represent the `User Profile API endpoint <https://docs.lacework.net/api/v2/docs/#tag/UserProfile>`_ .

    An organization can contain multiple accounts so you can also manage components such as alerts, resource groups, \
    team members, and audit logs at a more granular level inside an organization.
    """

    def __init__(self, session):
        """Initializes the UserProfileAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            UserProfileAPI: An instance of this class

        """
        super().__init__(session, "UserProfile")

    def get(self, account_name=None):
        """A method to get Lacework sub-accounts that are managed by your organization account. Using no args will get all sub-accounts.

        Args:
            account_name (str, optional): Specify which sub-account to list.

        Returns:
            dict: Details of the requested sub-account(s)

        """
        response = self._session.get(self._build_url(), params=account_name)

        return response.json()
