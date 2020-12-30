# -*- coding: utf-8 -*-
"""
Lacework Audit Logs API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class AuditLogsAPI(object):
    """
    Lacework Audit Logs API.
    """

    def __init__(self, session):
        """
        Initializes the AuditLogsAPI object.

        :param session: An instance of the HttpSession class

        :return AuditLogsAPI object.
        """

        super(AuditLogsAPI, self).__init__()

        self._session = session

    def get(self, start_time=None, end_time=None, org=False):
        """
        A method to get audit logs.

        :param start_time: A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting audit logs from Lacework...")

        # Build the Audit Logs request URI
        api_uri = "/api/v2/AuditLogs"

        if start_time and end_time:
            api_uri += f"?startTime={start_time}&endTime={end_time}"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def search(self, query_data=None, org=False):
        """
        A method to search audit logs.

        :param query_data: A dictionary containing the necessary search parameters
            (timeFilter, filters, returns)

        :return response json
        """

        logger.info("Searching audit logs from Lacework...")

        # Build the Audit Logs request URI
        api_uri = "/api/v2/AuditLogs/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()
