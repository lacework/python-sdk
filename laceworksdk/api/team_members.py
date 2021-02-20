# -*- coding: utf-8 -*-
"""
Lacework Team Members API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class TeamMembersAPI(object):
    """
    Lacework Team Members API.
    """

    def __init__(self, session):
        """
        Initializes the TeamMembersAPI object.

        :param session: An instance of the HttpSession class

        :return TeamMembersAPI object.
        """

        super(TeamMembersAPI, self).__init__()

        self._session = session

    def create(self,
               username,
               props,
               enabled,
               org=False):
        """
        A method to create a new team member.

        :param username: A string representing the email address of the user.
        :param props: An object containing team member configuration
            obj:
                :param firstName: The first name of the team member.
                :param lastName: The last name of the team member.
                :param company: The company of the team member.
                :param accountAdmin: A boolean representing if the team member is an account admin.
                :param orgAdmin: A boolean representing if the team member is an organization admin.
                :param orgUser: A boolean representing if the team member is an organization user.
                :param adminRoleAccounts: A list of strings representing accounts where the team member is an admin.
                :param userRoleAccounts: A list of strings representing accounts where the team member is a user.
        :param enabled: A boolean/integer representing whether the team member is enabled.
            (0 or 1)
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating team member in Lacework...")

        # Build the Team Members request URI
        api_uri = "/api/v2/TeamMembers"

        data = {
            "userName": username,
            "props": self._build_props(props),
            "userEnabled": int(bool(enabled))
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self, guid=None, org=False):
        """
        A method to get team members.

        :param guid: A string representing the team member GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting team member info from Lacework...")

        # Build the Team Members request URI
        if guid:
            api_uri = f"/api/v2/TeamMembers/{guid}"
        else:
            api_uri = "/api/v2/TeamMembers"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_guid(self, guid, org=False):
        """
        A method to get an team member by GUID.

        :param guid: A string representing the team member GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self, query_data=None, org=False):
        """
        A method to search team members.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching team members from Lacework...")

        # Build the Team Members request URI
        api_uri = "/api/v2/TeamMembers/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               guid,
               username=None,
               props=None,
               enabled=None,
               org=False):
        """
        A method to update a team member.

        :param guid: A string representing the team member GUID.
        :param username: A string representing the email address of the user.
        :param props: An object containing team member configuration
            obj:
                :param firstName: The first name of the team member.
                :param lastName: The last name of the team member.
                :param company: The company of the team member.
                :param accountAdmin: A boolean representing if the team member is an account admin.
                :param orgAdmin: A boolean representing if the team member is an organization admin.
                :param orgUser: A boolean representing if the team member is an organization user.
                :param adminRoleAccounts: A list of strings representing accounts where the team member is an admin.
                :param userRoleAccounts: A list of strings representing accounts where the team member is a user.
        :param enabled: A boolean/integer representing whether the team member is enabled.
            (0 or 1)
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating team member in Lacework...")

        # Build the Team Members request URI
        api_uri = f"/api/v2/TeamMembers/{guid}"

        tmp_data = {}

        if username:
            tmp_data["userName"] = username
        if props:
            tmp_data["props"] = self._build_props(props)
        if enabled is not None:
            tmp_data["userEnabled"] = int(bool(enabled))

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()

    def delete(self,
               guid,
               org=False):
        """
        A method to delete an team member.

        :param guid: A string representing the team member GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting team member in Lacework...")

        # Build the Team Members request URI
        api_uri = f"/api/v2/TeamMembers/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()

    def _build_props(self,
                     props):
        """
        A method to properly structure the props object.
        """

        keys = props.keys()

        response = {}

        if "firstName" in keys:
            response["firstName"] = props["firstName"]
        if "lastName" in keys:
            response["lastName"] = props["lastName"]
        if "company" in keys:
            response["company"] = props["company"]
        if "accountAdmin" in keys:
            response["accountAdmin"] = int(bool(props["accountAdmin"]))
        if "orgAdmin" in keys:
            response["orgAdmin"] = int(bool(props["orgAdmin"]))
        if "orgUser" in keys:
            response["orgUser"] = int(bool(props["orgUser"]))
        if "adminRoleAccounts" in keys:
            response["adminRoleAccounts"] = props["adminRoleAccounts"]
        if "userRoleAccounts" in keys:
            response["userRoleAccounts"] = props["userRoleAccounts"]

        return response
