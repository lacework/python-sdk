# -*- coding: utf-8 -*-
"""The base search class for the Lacework Python SDK"""
from laceworksdk.api.base_endpoint import BaseEndpoint


class SearchEndpoint(BaseEndpoint):
    """A class used to implement Search functionality for Lacework API Endpoints."""

    # If defined, this is the resource used in the URL path
    RESOURCE = ""

    def __init__(self, session, object_type, endpoint_root="/api/v2"):
        """
        Initialize the SearchEndpoint class.

        Args:
            session (HttpSession): An instance of the HttpSession class.
            object_type (str): The Lacework object type to use.
            endpoint_root (str, optional): The URL endpoint root to use.
        """
        super().__init__(session, object_type, endpoint_root)

    def search(self, json=None, resource=None):
        """A method to search objects.

        See the API documentation for this API endpoint for valid fields to search against.

        NOTE: While the "value" and "values" fields are marked as "optional" you must use one of them,
        depending on the operation you are using.

        Args:
          json (dict): The desired search parameters: \n
            - timeFilter (dict, optional): A dict containing the time frame for the search:\n
                - startTime (str): The start time for the search
                - endTime (str): The end time for the search

            - filters (list of dict, optional): Filters based on field contents:\n
                - field (str): The name of the data field to which the condition applies\n
                - expression (str): The comparison operator for the filter condition. Valid values are:\n

                "eq", "ne", "in", "not_in", "like", "ilike", "not_like", "not_ilike", "not_rlike", "rlike", "gt", "ge", \
                "lt", "le", "between"\n

                - value (str, optional):  The value that the condition checks for in the specified field. Use this attribute \
                when using an operator that requires a single value.
                - values (list of str, optional): The values that the condition checks for in the specified field. Use this \
                attribute when using an operator that requires multiple values.
            - returns (list of str, optional): The fields to return
          resource (str): The Lacework API resource to search (Example: "AlertChannels")

        Yields:
            dict: returns a generator which yields a page of objects at a time as returned by the Lacework API.
        """

        if not resource and self.RESOURCE:
            resource = self.RESOURCE

        response = self._session.post(
            self._build_url(resource=resource, action="search"), json=json
        )

        while True:
            response_json = response.json()
            yield response_json

            try:
                next_page = (
                    response_json.get("paging", {}).get("urls", {}).get("nextPage")
                )
            except Exception:
                next_page = None

            if next_page:
                response = self._session.get(next_page)
            else:
                break
