# -*- coding: utf-8 -*-
"""
Lacework Alert Channels API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class AlertChannelsAPI(object):
    """
    Lacework Alert Channels API.
    """

    def __init__(self, session):
        """
        Initializes the AlertChannelsAPI object.

        :param session: An instance of the HttpSession class

        :return AlertChannelsAPI object.
        """

        super(AlertChannelsAPI, self).__init__()

        self._session = session

    def create(self, name, type, enabled, data, org=False):
        """
        A method to create a new alert channel.

        :param name: A string representing the alert channel name.
        :param type: A string representing the alert channel type.
        :param enabled: An integer representing whether the integration is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating alert channel in Lacework...")

        # Build the Alert Channels request URI
        api_uri = "/api/v2/AlertChannels"

        data = {
            "name": name,
            "type": type,
            "enabled": enabled,
            "data": data
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self, guid=None, type=None, org=False):
        """
        A method to get all alert channels.

        :param guid: A string representing the alert channel GUID.
        :param type: A string representing the alert channel type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting alert channel info from Lacework...")

        # Build the Alert Channels request URI
        if guid:
            api_uri = f"/api/v2/AlertChannels/{guid}"
        elif type:
            api_uri = f"/api/v2/AlertChannels/{type}"
        else:
            api_uri = "/api/v2/AlertChannels"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_type(self, type, org=False):
        """
        A method to get all alert channels by type.

        :param type: A string representing the alert channel type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(type=type, org=org)

    def get_by_guid(self, guid, org=False):
        """
        A method to get all alert channels.

        :param guid: A string representing the alert channel GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self, query_data=None, org=False):
        """
        A method to search alert channels.

        :param query_data: A dictionary containing the necessary search parameters
            (filters, returns)

        :return response json
        """

        logger.info("Searching alert channels from Lacework...")

        # Build the Alert Channels request URI
        api_uri = "/api/v2/AlertChannels/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self, guid, name=None, type=None, enabled=None, data=None, org=False):
        """
        A method to update an alert channel.

        :param guid: A string representing the alert channel GUID.
        :param name: A string representing the alert channel name.
        :param type: A string representing the alert channel type.
        :param enabled: An integer representing whether the integration is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating alert channel in Lacework...")

        # Build the Alert Channels request URI
        api_uri = f"/api/v2/AlertChannels/{guid}"

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

    def delete(self, guid, org=False):
        """
        A method to delete an alert channel.

        :param guid: A string representing the alert channel GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting alert channel in Lacework...")

        # Build the Alert Channels request URI
        api_uri = f"/api/v2/AlertChannels/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
