# -*- coding: utf-8 -*-
"""
Lacework Account API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class AccountAPI:
    """
    Lacework Account API.
    """

    def __init__(self, session):
        """
        Initializes the AccountAPI object.

        :param session: An instance of the HttpSession class.

        :return AccountAPI object
        """

        super().__init__()

        self._session = session

    def get_org_info(self):
        """
        A method to get Account's organization info

        :return response json
        """

        logger.info("Getting Account information from Lacework...")

        # Build the Account request URI
        api_uri = "/api/v1/external/account/organizationInfo"

        response = self._session.get(api_uri)

        return response.json()
