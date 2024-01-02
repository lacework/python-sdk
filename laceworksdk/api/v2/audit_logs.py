# -*- coding: utf-8 -*-
"""Lacework AuditLogs API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class AuditLogsAPI(BaseEndpoint):

    def __init__(self, session):
        """Initializes the AuditLogsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return AuditLogsAPI object.

        Returns:

        """
        super().__init__(session, "AuditLogs")

    def get(self,
            start_time=None,
            end_time=None,
            **request_params):
        """A method to get AuditLogs objects.

        Args:
          start_time: A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from. (Default value = None)
          end_time: A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at. (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time
        )

        response = self._session.get(self.build_url(), params=params)

        return response.json()

    def search(self,
               json=None):
        """A method to search AuditLogs objects.

        Args:
          json: A dictionary containing the necessary search parameters.
        (timeFilter, filters, returns)
        
        :return response json (Default value = None)

        Returns:

        """
        response = self._session.post(self.build_url(action="search"), json=json)

        return response.json()
