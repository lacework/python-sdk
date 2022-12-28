# -*- coding: utf-8 -*-

from laceworksdk.api.base_endpoint import BaseEndpoint


class ReadEndpoint(BaseEndpoint):
    """
    A class used to implement Read functionality for Lacework API Endpoints
    """

    # If defined, this is the resource used in the URL path
    RESOURCE = ""

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

    def get(self, id=None, resource=None, **request_params):
        """
        A method to get objects.

        :param guid: A string representing the object ID.
        :param type: A string representing the object resource type.
        :param request_params: A dictionary of parameters to add to the request.

        :return response json
        """

        if not resource and self.RESOURCE:
            resource = self.RESOURCE

        params = self.build_dict_from_items(
            request_params
        )

        response = self._session.get(self.build_url(id=id, resource=resource), params=params)

        return response.json()
