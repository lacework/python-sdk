# -*- coding: utf-8 -*-
"""
Lacework ResourceGroups API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ResourceGroupsAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the ResourceGroupsAPI object.

        :param session: An instance of the HttpSession class

        :return ResourceGroupsAPI object.
        """

        super().__init__(session, "ResourceGroups")

    def create(self,
               resource_name,
               resource_type,
               enabled,
               props,
               **request_params):
        """
        A method to create a new ResourceGroups object.

        :param resource_name: A string representing the object name.
        :param resource_type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
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
        """
        A method to get ResourceGroups objects.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """
        A method to get ResourceGroups objects by GUID.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return self.get(guid=guid)

    def update(self,
               guid,
               resource_name=None,
               resource_type=None,
               enabled=None,
               props=None,
               **request_params):
        """
        A method to update an ResourceGroups object.

        :param guid: A string representing the object GUID.
        :param resource_name: A string representing the object name.
        :param resource_type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
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
        """
        A method to delete a ResourceGroups object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)
