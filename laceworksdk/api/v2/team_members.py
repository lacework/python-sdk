# -*- coding: utf-8 -*-
"""Lacework TeamMembers API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class TeamMembersAPI(CrudEndpoint):
    """A class used to represent the `Team Members API endpoint <https://docs.lacework.net/api/v2/docs/#tag/TeamMembers>`_

    DEPRECATED. Please use the TeamUsersAPI class instead.

    Team members can be granted access to multiple Lacework accounts and have different roles for each account. Team \
    members can also be granted organization-level roles.

    Note: The TeamMembers API is deprecated and is unavailable if you have migrated to the new RBAC model in your \
    Lacework Console.
    """

    def __init__(self, session):
        """Initializes the TeamMembersAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            TeamMembersAPI: An instance of this class
        """
        super().__init__(session, "TeamMembers")

    def create(
        self,
        user_name,
        user_enabled,
        props,
        org_admin=None,
        org_user=None,
        admin_role_accounts=None,
        user_role_accounts=None,
        **request_params,
    ):
        """A method to create a new team member.

        Args:
          user_name (str): The email address of the user.
          user_enabled (bool|int): Whether the object is enabled.

          props (dict): The user configuration. Fields are: \

              - firstName (str): The first name of the team member.
              - lastName (str): The last name of the team member.
              - company (str): The company of the team member.
              - accountAdmin (bool, optional): A boolean representing if the team member is an account admin.

          org_admin (bool, optional): Is the user an organization admin. (Organization-level Access Required)
          org_user (bool, optional): Is the user is an organization user. (Organization-level Access Required)
          admin_role_accounts (list of str): A list accounts where the user is an admin. (Organization-level Access \
          Required)
          user_role_accounts (list of str): A list of where the team member is a user. (Organization-level \
          Access Required)
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The newly created team member.

        """

        return super().create(
            user_name=user_name,
            user_enabled=int(bool(user_enabled)),
            props=props,
            org_admin=org_admin,
            org_user=org_user,
            admin_role_accounts=admin_role_accounts,
            user_role_accounts=user_role_accounts,
            **request_params,
        )

    def get(self, guid=None):
        """A method to get team members. Using no args will get all team members.

        Args:
          guid (str, optional): The GUID of the team member to get.

        Returns:
            dict: The requested team member
        """

        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get a team member by GUID.

        Args:
          guid (str): The GUID of the team member to get.

        Returns:
            dict: The requested team member

        """
        return self.get(guid=guid)

    def update(
        self,
        guid,
        user_name=None,
        user_enabled=None,
        props=None,
        org_admin=None,
        org_user=None,
        admin_role_accounts=None,
        user_role_accounts=None,
        **request_params,
    ):
        """A method to update a TeamMembers object.

        Args:
          guid: A string representing the object GUID.
          user_name (str): The email address of the user.
          user_enabled (bool|int): Whether the object is enabled.

          props (dict): The user configuration. Fields are: \

              - firstName (str): The first name of the team member.
              - lastName (str): The last name of the team member.
              - company (str): The company of the team member.
              - accountAdmin (bool, optional): A boolean representing if the team member is an account admin.

          org_admin (bool, optional): Is the user an organization admin. (Organization-level Access Required)
          org_user (bool, optional): Is the user is an organization user. (Organization-level Access Required)
          admin_role_accounts (list of str): A list accounts where the user is an admin. (Organization-level Access \
          Required)
          user_role_accounts (list of str): A list of where the team member is a user. (Organization-level \
          Access Required)
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated team member.

        """
        if user_enabled is not None:
            user_enabled = int(bool(user_enabled))

        return super().update(
            id=guid,
            user_name=user_name,
            user_enabled=user_enabled,
            props=props,
            org_admin=org_admin,
            org_user=org_user,
            admin_role_accounts=admin_role_accounts,
            user_role_accounts=user_role_accounts,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete a team member.

        Args:
          guid (str): The GUID of the team member to delete

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
