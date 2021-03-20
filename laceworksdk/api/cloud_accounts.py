# -*- coding: utf-8 -*-
"""
Lacework Cloud Accounts API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class CloudAccountsAPI(object):
    """
    Lacework Cloud Accounts API.
    """

    def __init__(self, session):
        """
        Initializes the CloudAccountsAPI object.

        :param session: An instance of the HttpSession class

        :return CloudAccountsAPI object.
        """

        super(CloudAccountsAPI, self).__init__()

        self._session = session

    def create(self,
               name,
               type,
               enabled,
               data,
               org=False):
        """
        A method to create a new cloud account.

        :param name: A string representing the cloud account name.
        :param type: A string representing the cloud account type.
        :param enabled: A boolean/integer representing whether the cloud account is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating cloud account in Lacework...")

        # Build the Cloud Accounts request URI
        api_uri = "/api/v2/CloudAccounts"

        data = {
            "name": name,
            "type": type,
            "enabled": int(bool(enabled)),
            "data": data
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            guid=None,
            type=None,
            org=False):
        """
        A method to get all cloud accounts.

        :param guid: A string representing the cloud account GUID.
        :param type: A string representing the cloud account type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting cloud account info from Lacework...")

        # Build the Cloud Accounts request URI
        if guid:
            api_uri = f"/api/v2/CloudAccounts/{guid}"
        elif type:
            api_uri = f"/api/v2/CloudAccounts/{type}"
        else:
            api_uri = "/api/v2/CloudAccounts"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_type(self,
                    type,
                    org=False):
        """
        A method to get all cloud accounts by type.

        :param type: A string representing the cloud account type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(type=type, org=org)

    def get_by_guid(self,
                    guid,
                    org=False):
        """
        A method to get all cloud accounts.

        :param guid: A string representing the cloud account GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search cloud accounts.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching cloud accounts from Lacework...")

        # Build the Cloud Accounts request URI
        api_uri = "/api/v2/CloudAccounts/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               data=None,
               org=False):
        """
        A method to update an cloud account.

        :param guid: A string representing the cloud account GUID.
        :param name: A string representing the cloud account name.
        :param type: A string representing the cloud account type.
        :param enabled: A boolean/integer representing whether the cloud account is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating cloud account in Lacework...")

        # Build the Cloud Accounts request URI
        api_uri = f"/api/v2/CloudAccounts/{guid}"

        tmp_data = {}

        if name:
            tmp_data["name"] = name
        if type:
            tmp_data["type"] = type
        if enabled is not None:
            tmp_data["enabled"] = int(bool(enabled))
        if data:
            tmp_data["data"] = data

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()

    def delete(self,
               guid,
               org=False):
        """
        A method to delete an cloud account.

        :param guid: A string representing the cloud account GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting cloud account in Lacework...")

        # Build the Cloud Accounts request URI
        api_uri = f"/api/v2/CloudAccounts/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
