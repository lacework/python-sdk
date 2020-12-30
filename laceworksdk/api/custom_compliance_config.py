# -*- coding: utf-8 -*-
"""
Lacework Custom Compliance Config API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class CustomComplianceConfigAPI(object):
    """
    Lacework Custom Compliance Config API.
    """

    def __init__(self, session):
        """
        Initializes the CustomComplianceConfigAPI object.

        :param session: An instance of the HttpSession class.

        :return CustomComplianceConfigAPI object
        """

        super(CustomComplianceConfigAPI, self).__init__()

        self._session = session

    def get(self):
        """
        A method to get the custom compliance settings from Lacework.

        :return response json
        """

        logger.info("Getting custom compliance settings from Lacework...")

        # Build the Custom Compliance Config request URI
        api_uri = "/api/v1/external/CustomComplianceConfig"

        response = self._session.get(api_uri)

        return response.json()

    def set(self, data):
        """
        A method to set the custom compliance settings in Lacework.

        :param settings: A JSON object

        :return response json
        """

        logger.info("Setting custom compliance settings in Lacework...")

        # Build the Custom Compliance Config request URI
        api_uri = "/api/v1/external/CustomComplianceConfig"

        response = self._session.post(api_uri, data=data)

        return response.json()
