# -*- coding: utf-8 -*-
"""Lacework AuditLogs API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class AuditLogsAPI(BaseEndpoint):
    """A class used to represent the `Audit Log API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AuditLogs>`_

    Get audit logs.
    """

    def __init__(self, session):
        """Initializes the AuditLogsAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            AuditLogsAPI: An instance of this class.
        """
        super().__init__(session, "AuditLogs")

    def get(self, start_time=None, end_time=None, **request_params):
        """A method to get audit logs.

        Args:
          start_time (str): A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
          end_time (str): A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The audit logs for the requested time period.
        """
        params = self._build_dict_from_items(
            request_params, start_time=start_time, end_time=end_time
        )

        response = self._session.get(self._build_url(), params=params)

        return response.json()

    def search(self, json=None):
        """A method to search audit logs.

        See the API documentation for this API endpoint for valid fields to search against.

        NOTE: While the "value" and "values" fields are marked as "optional" you must use one of them,
        depending on the operation you are using.

        Args:
          json (list of dicts): A list of dictionaries containing the desired search parameters: \n
            - field (str): The name of the data field to which the condition applies\n
            - expression (str): The comparison operator for the filter condition. Valid values are:\n
                "eq", "ne", "in", "not_in", "like", "ilike", "not_like", "not_ilike", "not_rlike", "rlike", "gt", "ge", \
                "lt", "le", "between"
            - value (str, optional):  The value that the condition checks for in the specified field. Use this attribute \
             when using an operator that requires a single value.
            - values (list of str, optional): The values that the condition checks for in the specified field. Use this \
            attribute when using an operator that requires multiple values.

        Yields:
            dict: returns a generator which yields a page of objects at a time as returned by the Lacework API.
        """

        response = self._session.post(self._build_url(action="search"), json=json)
        return response.json()
