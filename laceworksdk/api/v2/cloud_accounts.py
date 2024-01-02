# -*- coding: utf-8 -*-
"""Lacework CloudAccounts API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class CloudAccountsAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the CloudAccountsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return CloudAccountsAPI object.

        Returns:

        """
        super().__init__(session, "CloudAccounts")

    def create(self,
               name,
               type,
               enabled,
               data,
               **request_params):
        """A method to create a new CloudAccounts object.

        Args:
          name: A string representing the object name.
          type: A string representing the object type.
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1)
          data: A JSON object matching the schema for the specified type.
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        return super().create(
            name=name,
            type=type,
            enabled=int(bool(enabled)),
            data=data,
            **request_params
        )

    def get(self,
            guid=None,
            type=None):
        """A method to get CloudAccounts objects.

        Args:
          guid: A string representing the object GUID. (Default value = None)
          type: A string representing the object type.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=guid, resource=type)

    def get_by_guid(self,
                    guid):
        """A method to get CloudAccounts objects by GUID.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return self.get(guid=guid)

    def get_by_type(self,
                    type):
        """A method to get CloudAccounts objects by type.

        Args:
          type: A string representing the object type.
        
        :return response json

        Returns:

        """
        return self.get(type=type)

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               data=None,
               **request_params):
        """A method to update an CloudAccounts object.

        Args:
          guid: A string representing the object GUID.
          name: A string representing the object name. (Default value = None)
          type: A string representing the object type. (Default value = None)
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1) (Default value = None)
          data: A JSON object matching the schema for the specified type. (Default value = None)
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
            name=name,
            type=type,
            enabled=enabled,
            data=data,
            **request_params
        )

    def delete(self,
               guid):
        """A method to delete an CloudAccounts object.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return super().delete(id=guid)
