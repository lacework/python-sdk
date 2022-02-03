# -*- coding: utf-8 -*-
"""
Lacework TeamMembers API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class TeamMembersAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the TeamMembersAPI object.

        :param session: An instance of the HttpSession class

        :return TeamMembersAPI object.
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
        """
        A method to create a new TeamMembers object.

        :param user_name: A string representing the email address of the user.
        :param user_enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: An object containing object configuration
            obj:
                :param firstName: The first name of the object.
                :param lastName: The last name of the team m.
                :param company: The company of the object.
                :param accountAdmin: A boolean representing if the object is an account admin.
        :param org_admin: A boolean representing if the object is an organization admin.
            (Organization-level Access Required)
        :param org_user: A boolean representing if the object is an organization user.
            (Organization-level Access Required)
        :param admin_role_accounts: A list of strings representing accounts where the object is an admin.
            (Organization-level Access Required)
        :param user_role_accounts: A list of strings representing accounts where the object is a user.
            (Organization-level Access Required)
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
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
        """
        A method to get TeamMembers objects.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().get(id=guid)

    def get_by_guid(self, guid):
        """
        A method to get a TeamMembers object by GUID.

        :param guid: A string representing the object GUID.

        :return response json
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
        """
        A method to update a TeamMembers object.

        :param guid: A string representing the object GUID.
        :param user_name: A string representing the email address of the object.
        :param user_enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param props: An object containing object configuration
            obj:
                :param firstName: The first name of the object.
                :param lastName: The last name of the team m.
                :param company: The company of the object.
                :param accountAdmin: A boolean representing if the object is an account admin.
        :param org_admin: A boolean representing if the object is an organization admin.
            (Organization-level Access Required)
        :param org_user: A boolean representing if the object is an organization user.
            (Organization-level Access Required)
        :param admin_role_accounts: A list of strings representing accounts where the object is an admin.
            (Organization-level Access Required)
        :param user_role_accounts: A list of strings representing accounts where the object is a user.
            (Organization-level Access Required)
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
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
        """
        A method to delete a TeamMembers object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)
