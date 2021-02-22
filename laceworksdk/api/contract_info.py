# -*- coding: utf-8 -*-
"""
Lacework Contract Info API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class ContractInfoAPI(object):
    """
    Lacework Contract Info API.
    """

    def __init__(self, session):
        """
        Initializes the ContractInfoAPI object.

        :param session: An instance of the HttpSession class

        :return ContractInfoAPI object.
        """

        super(ContractInfoAPI, self).__init__()

        self._session = session

    def get(self,
            start_time=None,
            end_time=None,
            org=False):
        """
        A method to get contract info.

        :param start_time: A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting contract info from Lacework...")

        # Build the Contract Info request URI
        api_uri = "/api/v2/ContractInfo"

        if start_time and end_time:
            api_uri += f"?startTime={start_time}&endTime={end_time}"

        response = self._session.get(api_uri, org=org)

        return response.json()
