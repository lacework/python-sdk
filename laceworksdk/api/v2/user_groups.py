# -*- coding: utf-8 -*-
"""Lacework UserGroups API wrapper (Experimental)."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class UserGroupsAPI(BaseEndpoint):
    """A class used to represent the `User Groups API endpoint <https://docs.lacework.net/api/v2/docs/#tag/UserGroups>`_ .

    A user group associates Lacework service and standard users with specific permissions in Lacework.
    """

    def __init__(self, session):
        """Initialize the UserGroupsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            UserGroupsAPI: An instance of this class
        """
        super().__init__(session, "UserGroups")

    def __modify_members(self, guid, user_guids, action):
        json = self._build_dict_from_items(
            user_guids=user_guids,
        )

        response = self._session.post(
            self._build_url(resource=guid, action=action), json=json, params=None
        )

        return response.json()

    def add_users(self, guid, user_guids):
        """A method to add users to existing UserGroup object.

        Args:
          guid (str): The GUID of the UserGroup to modify
          user_guids (list of str): An array of user guids to add to the user group

        Returns:
            dict: The modified results
        """
        return self.__modify_members(guid, user_guids, "addUsers")

    def remove_users(self, guid, user_guids):
        """A method to remove users from an existing UserGroup object.

        Args:
          guid (str): The GUID of the UserGroup object to modify.
          user_guids (list of str): An array of user guids to remove from the user group

        Returns:
            dict: The modified results

        """
        return self.__modify_members(guid, user_guids, "removeUsers")
