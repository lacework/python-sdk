# -*- coding: utf-8 -*-
"""
Lacework User Profile API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class UserProfileAPI(object):
    """
    Lacework User Profile API.
    """

    def __init__(self, session):
        """
        Initializes the UserProfileAPI object.

        :param session: An instance of the HttpSession class

        :return UserProfileAPI object.
        """

        super(UserProfileAPI, self).__init__()

        self._session = session

    def get(self,
            type=None,
            subtype=None):
        """
        A method to list all info in the user profile

        :return response json
        """

        logger.info("Fetching user profile info from Lacework...")

        # Build the User Profile request URI
        api_uri = "/api/v2/UserProfile"

        response = self._session.get(api_uri)

        return response.json()
