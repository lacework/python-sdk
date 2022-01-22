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
               name,
               type,
               enabled,
               props,
               **request_params):
        """
        A method to create a new ResourceGroups object.

        :param name: A string representing the object name.
        :param type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            resource_name=name,
            resource_type=type,
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

    def search(self,
               json=None,
               query_data=None):
        """
        A method to search ResourceGroups objects.

        :param json: A dictionary containing the desired search parameters.
            (filters, returns)
        :param query_data: (DEPRECATED: Use 'json' moving forward)
            A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        return super().search(json=json, query_data=query_data)

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               props=None,
               **request_params):
        """
        A method to update an ResourceGroups object.

        :param guid: A string representing the object GUID.
        :param name: A string representing the object name.
        :param type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().update(
            id=guid,
            resource_name=name,
            resource_type=type,
            enabled=int(bool(enabled)),
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
