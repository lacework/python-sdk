# -*- coding: utf-8 -*-
"""Lacework UserProfile API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class UserProfileAPI(BaseEndpoint):

    def __init__(self, session):
        """Initializes the UserProfileAPI object.

        Args:
          session: An instance of the HttpSession class

        :return UserProfileAPI object.

        Returns:

        """
        super().__init__(session, "UserProfile")

    def get(self):
        """A method to get UserProfile object.
        
        :return response json

        Args:

        Returns:

        """
        response = self._session.get(self.build_url())

        return response.json()
