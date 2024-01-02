# -*- coding: utf-8 -*-

from laceworksdk.api.base_endpoint import BaseEndpoint


class CrudEndpoint(BaseEndpoint):
    """A class used to implement CRUD create/read/update/delete functionality for Lacework API Endpoints."""

    def __init__(self,
                 session,
                 object_type,
                 endpoint_root="/api/v2"):
        """
        Initialize the CRUDEndpoint Class.

        Args:
            session(HttpSession): An instance of the HttpSession class.
            object_type(str): The Lacework object type to use.
            endpoint_root(str, optional): The URL endpoint root to use.
        """
        super().__init__(session, object_type, endpoint_root)

    def create(self, params=None, **request_params):
        """A method to create a new object.

        Args:

          params(any):  Parameters
          request_params(any): Request parameters.

        Returns:
            response(dict): json containing object info

        """
        json = self.build_dict_from_items(
            request_params
        )

        response = self._session.post(self.build_url(), json=json, params=params)

        return response.json()

    def get(self, id=None, resource=None, **request_params):
        """A method to get objects.

        Args:
          id(str): A string representing the object ID.
          resource(str): The Lacework API resource type to get.
          request_params(any): A dictionary of parameters to add to the request.

        Returns:
            response(dict): json containing objects
        """
        params = self.build_dict_from_items(
            request_params
        )

        response = self._session.get(self.build_url(id=id, resource=resource), params=params)

        return response.json()

    def search(self, json=None, **kwargs):
        """A method to search objects.\n

                NOTE: While the "value" and "values" fields are marked as "optional" you must use one of them,
                depending on the operation you are using.

                Args:
                  json(list of dicts): A list of dictionaries containing the desired search parameters: \n

                    - field(str): The name of the data field to which the condition applies\n
                    - expression(str): The comparison operator for the filter condition. Valid values are:\n

                        - "eq"\n
                        - "ne"\n
                        - "in"\n
                        - "not_in"\n
                        - "like"\n
                        - "ilike"\n
                        - "not_like"\n
                        - "not_ilike"\n
                        - "not_rlike"\n
                        - "rlike"\n
                        - "gt"\n
                        - "ge"\n
                        - "lt"\n
                        - "le"\n
                        - "between"\n

                    - value(str, optional):  The value that the condition checks for in the specified field. Use this attribute
                     when using an operator that requires a single value.\n
                    - values(list of str, optional): The values that the condition checks for in the specified field. Use this
                    attribute when using an operator that requires multiple values.\n

                Returns:
                    response(Generator): a generator which yields a page of objects at a time as returned by the Lacework API.
                """
        response = self._session.post(self.build_url(action="search"), json=json)

        return response.json()

    def update(self, id=None, params=None, **request_params):
        """A method to update an object.

        Args:
          id(str): A string representing the object ID.
          params(any):  parameters
          request_params(any): request parameters

        Returns:
            response(dict):JSON containing the updated object info

        """
        json = self.build_dict_from_items(
            request_params
        )

        response = self._session.patch(self.build_url(id=id), json=json, params=params)

        return response.json()

    def delete(self, id, params=None):
        """A method to delete an object.

        Args:
          id(str): A string representing the object GUID.
          params(any):  parameters

        Returns:
            response(requests.models.Response): a Requests response object containing the response code
        """
        response = self._session.delete(self.build_url(id=id), params=params)

        return response

    def _format_filters(self,
                        filters):
        """A method to properly format the filters object.

        Args:
          filters(dict): A dict of filters to be properly formatted (boolean conversion).

        Returns:
            response(dict): json

        """
        if "enabled" in filters.keys():
            filters["enabled"] = int(bool(filters["enabled"]))

        return filters
