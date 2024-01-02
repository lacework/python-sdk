# -*- coding: utf-8 -*-
"""Lacework AlertRules API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertRulesAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the AlertRulesAPI object.

        Args:
          session: An instance of the HttpSession class

        :return AlertRulesAPI object.

        Returns:

        """
        super().__init__(session, "AlertRules")

    def create(self,
               type,
               filters,
               intg_guid_list,
               **request_params):
        """A method to create a new AlertRules object.

        Args:
          type: A string representing the type of the object.
        ('Event')
          filters: A filter object for the object configuration.
        obj:
          name: A string representing the object name.
          description: A string representing the object description.
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1)
          resourceGroups: A list of resource groups to define for the object.
          eventCategory: A list of event categories to define for the object.
        ("Compliance", "App", "Cloud", "File", "Machine", "User", "Platform", "K8sActivity")
          severity: A list of alert severities to define for the object.
        (1, 2, 3, 4, 5)
          intg_guid_list: A list of integration GUIDs representing the alert channels to use.
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        return super().create(
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            **request_params
        )

    def get(self,
            guid=None):
        """A method to get AlertRules objects.

        Args:
          guid: A string representing the object GUID.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """A method to get an AlertRules object by GUID.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return self.get(guid=guid)

    def update(self,
               guid,
               type=None,
               filters=None,
               intg_guid_list=None,
               **request_params):
        """A method to update an AlertRules object.

        Args:
          guid: A string representing the object GUID.
          type: A string representing the type of the object.
        ('Event') (Default value = None)
          filters: A filter object for the object configuration.
        obj: (Default value = None)
          name: A string representing the object name.
          description: A string representing the object description.
          enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1)
          resourceGroups: A list of resource groups to define for the object.
          eventCategory: A list of event categories to define for the object.
        ("Compliance", "App", "Cloud", "File", "Machine", "User", "Platform", "K8sActivity")
          severity: A list of alert severities to define for the object.
        (1, 2, 3, 4, 5)
          intg_guid_list: A list of integration GUIDs representing the alert channels to use. (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        return super().update(
            id=guid,
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            **request_params
        )

    def delete(self,
               guid):
        """A method to delete an AlertRules object.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return super().delete(id=guid)
