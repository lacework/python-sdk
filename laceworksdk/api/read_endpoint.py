# -*- coding: utf-8 -*-
"""The base read class for the Lacework Python SDK"""
from laceworksdk.api.base_endpoint import BaseEndpoint


class ReadEndpoint(BaseEndpoint):
    """A class used to implement Read functionality for Lacework API Endpoints."""

    # If defined, this is the resource used in the URL path
    RESOURCE = ""

    def __init__(self, session, object_type, endpoint_root="/api/v2"):
        """
        Initialize the ReadEndpoint Class.

        Args:
            session (HttpSession): An instance of the HttpSession class.
            object_type (str): The Lacework object type to use.
            endpoint_root (str, optional): The URL endpoint root to use.
        """
        super().__init__(session, object_type, endpoint_root)

    def get(self, id=None, resource=None, **request_params):
        """A method to get objects.

        Args:
          id (str): A string representing the object ID.
          resource (str): The Lacework API resource type to get.
          request_params (dict): Use to pass any additional parameters the API

        Returns:
            dict: the requested o
        """

        if not resource and self.RESOURCE:
            resource = self.RESOURCE

        params = self._build_dict_from_items(request_params)

        response = self._session.get(
            self._build_url(id=id, resource=resource), params=params
        )

        return response.json()
