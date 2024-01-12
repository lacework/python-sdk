# -*- coding: utf-8 -*-
"""Lacework API wrapper."""
from laceworksdk.api.base_endpoint import BaseEndpoint


class CrudEndpoint(BaseEndpoint):
    """A class used to implement CRUD create/read/update/delete functionality for Lacework API Endpoints."""

    def __init__(self, session, object_type, endpoint_root="/api/v2"):
        """
        Initialize the CRUDEndpoint Class.

        Args:
            session (HttpSession): An instance of the HttpSession class.
            object_type (str): The Lacework object type to use.
            endpoint_root (str, optional): The URL endpoint root to use.
        """
        super().__init__(session, object_type, endpoint_root)

    def create(self, params=None, **request_params):
        """A method to create a new object.

        Args:
          params (any):  Parameters
          request_params (any): Request parameters.

        Returns:
            dict: JSON containing the new object info

        """
        json = self._build_dict_from_items(request_params)

        response = self._session.post(self._build_url(), json=json, params=params)

        return response.json()

    def get(self, id=None, resource=None, **request_params):
        """A method to get objects.

        Args:
          id (str): A string representing the object ID.
          resource (str): The Lacework API resource type to get.
          request_params (any): A dictionary of parameters to add to the request.

        Returns:
            dict: JSON containing the retrieved object(s)
        """
        params = self._build_dict_from_items(request_params)

        response = self._session.get(
            self._build_url(id=id, resource=resource), params=params
        )

        return response.json()

    def search(self, json=None):
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

        Returns:
            dict: returns a dict containing the search results
        """
        response = self._session.post(self._build_url(action="search"), json=json)

        return response.json()

    def update(self, id=None, params=None, **request_params):
        """A method to update an object.

        Args:
          id (str): A string representing the object ID.
          params (any):  parameters
          request_params (dict): Use to pass any additional parameters the API

        Returns:
            dict: JSON containing the updated object info

        """
        json = self._build_dict_from_items(request_params)

        response = self._session.patch(self._build_url(id=id), json=json, params=params)

        return response.json()

    def delete(self, id, params=None):
        """A method to delete an object.

        Args:
          id (str): A string representing the object GUID.
          params (any):  parameters

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        response = self._session.delete(self._build_url(id=id), params=params)

        return response

    def _format_filters(self, filters):
        """A method to properly format the filters object.

        Args:
          filters (dict): A dict of filters to be properly formatted (boolean conversion).

        Returns:
            dict: formatted filters object

        """
        if "enabled" in filters.keys():
            filters["enabled"] = int(bool(filters["enabled"]))

        return filters
