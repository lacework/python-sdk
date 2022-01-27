# -*- coding: utf-8 -*-

from laceworksdk.api.base_endpoint import BaseEndpoint


class CrudEndpoint(BaseEndpoint):
    """
    A class used to implement CRUD create/read/update/delete functionality for Lacework API Endpoints
    """

    def __init__(self,
                 session,
                 object_type,
                 endpoint_root="/api/v2"):
        """
        :param session: An instance of the HttpSession class.
        :param object_type: The Lacework object type to use.
        :param endpoint_root: The URL endpoint root to use.
        """

        super().__init__(session, object_type, endpoint_root)

    def create(self, **request_params):
        """
        A method to create a new object.

        :param request_params: Request parameters.

        :return response json
        """

        json = self.build_dict_from_items(
            request_params
        )

        response = self._session.post(self.build_url(), json=json)

        return response.json()

    def get(self, id=None, resource=None, **request_params):
        """
        A method to get objects.

        :param guid: A string representing the object ID.
        :param type: A string representing the object resource type.
        :param request_params: A dictionary of parameters to add to the request.

        :return response json
        """

        params = self.build_dict_from_items(
            request_params
        )

        response = self._session.get(self.build_url(id=id, resource=resource), params=params)

        return response.json()

    def search(self, json=None, **kwargs):
        """
        A method to search objects.

        :param json: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        response = self._session.post(self.build_url(action="search"), json=json)

        return response.json()

    def update(self, id=None, **request_params):
        """
        A method to update an object.

        :param guid: A string representing the object ID.
        :param request_params: Request parameters.

        :return response json
        """

        json = self.build_dict_from_items(
            request_params
        )

        response = self._session.patch(self.build_url(id=id), json=json)

        return response.json()

    def delete(self, id):
        """
        A method to delete an object.

        :param guid: A string representing the alert channel GUID.

        :return response json
        """

        response = self._session.delete(self.build_url(id=id))

        return response

    def _format_filters(self,
                        filters):
        """
        A method to properly format the filters object.

        :param filters: A dict of filters to be properly formatted (boolean conversion).

        :return json
        """

        if "enabled" in filters.keys():
            filters["enabled"] = int(bool(filters["enabled"]))

        return filters
