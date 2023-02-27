# -*- coding: utf-8 -*-
"""
Lacework UserGroups API wrapper (Experimental).
"""

from laceworksdk.api.base_endpoint import BaseEndpoint

class UserGroupsAPI(BaseEndpoint):
    def __init__(self, session):
        super().__init__(session, "UserGroups")

    def __modify_members(self, guid, user_guids, action):
        json = self.build_dict_from_items(
            user_guids=user_guids,
        )

        response = self._session.post(self.build_url(resource=guid, action=action), json=json, params=None)

        return response.json()

    def add_users(self, guid, user_guids):
        """
        (Experimental API) A method to add users to existing UserGroup object.

        :param guid: A string representing the GUID of the UserGroup to modify.
        :param user_guids: An array of user guids to add to the UserGroup object.

        :return response json
        """
        return self.__modify_members(guid, user_guids, "addUsers")

    def remove_users(self, guid, user_guids):
        """
        (Experimental API) A method to remove users from an existing UserGroup object.

        :param guid: A string representing the GUID of the UserGroup object to modify.
        :param user_guids: An array of user guids to add to the UserGroup object.

        :return response json
        """
        return self.__modify_members(guid, user_guids, "removeUsers")
