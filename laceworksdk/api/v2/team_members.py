# -*- coding: utf-8 -*-
"""Lacework TeamMembers API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class TeamMembersAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the TeamMembersAPI object.

        Args:
          session: An instance of the HttpSession class

        :return TeamMembersAPI object.

        Returns:

        """
        super().__init__(session, "TeamMembers")

    def create(self,
               user_name,
               user_enabled,
               props,
               org_admin=None,
               org_user=None,
               admin_role_accounts=None,
               user_role_accounts=None,
               **request_params):
        """A method to create a new TeamMembers object.

        Args:
          user_name: A string representing the email address of the user.
          user_enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1)
          props: An object containing object configuration
        obj:
          firstName: The first name of the team member.
          lastName: The last name of the team member.
          company: The company of the team member.
          accountAdmin: A boolean representing if the team member is an account admin.
          org_admin: A boolean representing if the object is an organization admin.
        (Organization-level Access Required) (Default value = None)
          org_user: A boolean representing if the object is an organization user.
        (Organization-level Access Required) (Default value = None)
          admin_role_accounts: A list of strings representing accounts where the object is an admin.
        (Organization-level Access Required) (Default value = None)
          user_role_accounts: A list of strings representing accounts where the object is a user.
        (Organization-level Access Required) (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        return super().create(
            user_name=user_name,
            user_enabled=int(bool(user_enabled)),
            props=props,
            org_admin=org_admin,
            org_user=org_user,
            admin_role_accounts=admin_role_accounts,
            user_role_accounts=user_role_accounts,
            **request_params
        )

    def get(self, guid=None):
        """A method to get TeamMembers objects.

        Args:
          guid: A string representing the object GUID.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get a TeamMembers object by GUID.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return self.get(guid=guid)

    def update(self,
               guid,
               user_name=None,
               user_enabled=None,
               props=None,
               org_admin=None,
               org_user=None,
               admin_role_accounts=None,
               user_role_accounts=None,
               **request_params):
        """A method to update a TeamMembers object.

        Args:
          guid: A string representing the object GUID.
          user_name: A string representing the email address of the object. (Default value = None)
          user_enabled: A boolean/integer representing whether the object is enabled.
        (0 or 1) (Default value = None)
          props: An object containing object configuration
        obj: (Default value = None)
          firstName: The first name of the team member.
          lastName: The last name of the team member.
          company: The company of the team member.
          accountAdmin: A boolean representing if the team member is an account admin.
          org_admin: A boolean representing if the object is an organization admin.
        (Organization-level Access Required) (Default value = None)
          org_user: A boolean representing if the object is an organization user.
        (Organization-level Access Required) (Default value = None)
          admin_role_accounts: A list of strings representing accounts where the object is an admin.
        (Organization-level Access Required) (Default value = None)
          user_role_accounts: A list of strings representing accounts where the object is a user.
        (Organization-level Access Required) (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

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
            **request_params
        )

    def delete(self,
               guid):
        """A method to delete a TeamMembers object.

        Args:
          guid: A string representing the object GUID.
        
        :return response json

        Returns:

        """
        return super().delete(id=guid)
