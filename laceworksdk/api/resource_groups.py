# -*- coding: utf-8 -*-
"""
Lacework Resource Groups API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class ResourceGroupsAPI(object):
    """
    Lacework Resource Groups API.
    """

    def __init__(self, session):
        """
        Initializes the ResourceGroupsAPI object.

        :param session: An instance of the HttpSession class

        :return ResourceGroupsAPI object.
        """

        super(ResourceGroupsAPI, self).__init__()

        self._session = session

    def create(self,
               name,
               type,
               enabled,
               props,
               org=False):
        """
        A method to create a new resource group.

        :param name: A string representing the resource group name.
        :param type: A string representing the resource group type.
        :param enabled: A boolean/integer representing whether the resource group is enabled.
            (0 or 1)
        :param props: A JSON object matching the schema for the specified resource group type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating resource group in Lacework...")

        # Build the Resource Groups request URI
        api_uri = "/api/v2/ResourceGroups"

        data = {
            "resourceName": name,
            "resourceType": type,
            "enabled": int(bool(enabled)),
            "props": props
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            guid=None,
            org=False):
        """
        A method to get all resource groups.

        :param guid: A string representing the resource group GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting resource group info from Lacework...")

        # Build the Resource Groups request URI
        if guid:
            api_uri = f"/api/v2/ResourceGroups/{guid}"
        else:
            api_uri = "/api/v2/ResourceGroups"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_guid(self,
                    guid,
                    org=False):
        """
        A method to get all resource groups.

        :param guid: A string representing the resource group GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search resource groups.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching resource groups from Lacework...")

        # Build the Resource Groups request URI
        api_uri = "/api/v2/ResourceGroups/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               props=None,
               org=False):
        """
        A method to update an resource group.

        :param guid: A string representing the resource group GUID.
        :param name: A string representing the resource group name.
        :param type: A string representing the resource group type.
        :param enabled: A boolean/integer representing whether the resource group is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating resource group in Lacework...")

        # Build the Resource Groups request URI
        api_uri = f"/api/v2/ResourceGroups/{guid}"

        tmp_data = {}

        if name:
            tmp_data["resourceName"] = name
        if type:
            tmp_data["resourceType"] = type
        if enabled is not None:
            tmp_data["enabled"] = int(bool(enabled))
        if props:
            tmp_data["props"] = props

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()

    def delete(self, guid, org=False):
        """
        A method to delete a resource group.

        :param guid: A string representing the resource group GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting resource group in Lacework...")

        # Build the Resource Groups request URI
        api_uri = f"/api/v2/ResourceGroups/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
