# -*- coding: utf-8 -*-
"""Lacework ResourceGroups API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ResourceGroupsAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the ResourceGroupsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return ResourceGroupsAPI object.

        Returns:

        """
        super().__init__(session, "ResourceGroups")

    def create(self,
               resource_name,
               resource_type,
               enabled,
               props,
               **request_params):
        """A method to create a new ResourceGroups object.

        Args:
          resource_name: A string representing the object name.
          resource_type: A string representing the object type.
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1)
          props: A JSON object matching the schema for the specified type.
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        return super().create(
            resource_name=resource_name,
            resource_type=resource_type,
            enabled=int(bool(enabled)),
            props=props,
            **request_params
        )

    def get(self,
            guid=None):
        """A method to get ResourceGroups objects.

        Args:
          guid: A string representing the object GUID.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """A method to get ResourceGroups objects by GUID.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return self.get(guid=guid)

    def update(self,
               guid,
               resource_name=None,
               resource_type=None,
               enabled=None,
               props=None,
               **request_params):
        """A method to update an ResourceGroups object.

        Args:
          guid: A string representing the object GUID.
          resource_name: A string representing the object name. (Default value = None)
          resource_type: A string representing the object type. (Default value = None)
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1) (Default value = None)
          props: A JSON object matching the schema for the specified type. (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid,
            resource_name=resource_name,
            resource_type=resource_type,
            enabled=enabled,
            props=props,
            **request_params
        )

    def delete(self,
               guid):
        """A method to delete a ResourceGroups object.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return super().delete(id=guid)
