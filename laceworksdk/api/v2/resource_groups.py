# -*- coding: utf-8 -*-
"""Lacework ResourceGroups API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ResourceGroupsAPI(CrudEndpoint):
    """A class used to represent the `Resource Groups API endpoint <https://docs.lacework.net/api/v2/docs/#tag/ResourceGroups>`_

    Resource groups provide a way to categorize Lacework-identifiable assets.
    """

    def __init__(self, session):
        """Initializes the ResourceGroupsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            ResourceGroupsAPI: An instance of this class
        """
        super().__init__(session, "ResourceGroups")

    def create(self, resource_name, resource_type, enabled, props, **request_params):
        """A method to create a new ResourceGroups object.

        Args:
          resource_name (str): The resource group name.
          resource_type (str): The resource group type. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ResourceGroups/paths/~1api~1v2~1ResourceGroups/post>`_ \
          for a list of types.
          enabled (bool|int): Whether the object is enabled.
          props (dict): The new resource group's properties. The format varies based on the value of the type arg. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ResourceGroups/paths/~1api~1v2~1ResourceGroups/post>`_ \
          for valid fields.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The newly created resource group

        """

        return super().create(
            resource_name=resource_name,
            resource_type=resource_type,
            enabled=int(bool(enabled)),
            props=props,
            **request_params,
        )

    def get(self, guid=None):
        """A method to get resource groups. Using no args will get all resource groups.

        Args:
          guid (str, optional): The GUID of the resource group to get.

        Returns:
            dict: The requested resource group(s)

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get resource groups by GUID.

        Args:
          guid (str): The GUID of the resource group to get.

        Returns:
            dict: The requested resource group(s)

        """
        return self.get(guid=guid)

    def update(
        self,
        guid,
        resource_name=None,
        resource_type=None,
        enabled=None,
        props=None,
        **request_params,
    ):
        """A method to update an ResourceGroups object.

        Args:
          guid (str): A string representing the object GUID.
          resource_name (str, optional): The resource group name.
          resource_type (str, optional): The resource group type. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ResourceGroups/paths/~1api~1v2~1ResourceGroups~1%7BresourceGuid%7D/patch>`_ \
          for a list of types.
          enabled (bool|int, optional): Whether the object is enabled.
          props (dict, optional): The new resource group's properties. The format varies based on the value of the type arg. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ResourceGroups/paths/~1api~1v2~1ResourceGroups~1%7BresourceGuid%7D/patch>`_ \
          for valid fields.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The newly created resource group

        """
        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid,
            resource_name=resource_name,
            resource_type=resource_type,
            enabled=enabled,
            props=props,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete a resource groups.

        Args:
          guid (str): The GUID of the resource group to delete.

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
