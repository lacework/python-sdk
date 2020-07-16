# -*- coding: utf-8 -*-
"""
Lacework Integrations API wrapper.
"""

import json
import logging

logger = logging.getLogger(__name__)


class IntegrationsAPI(object):
    """
    Lacework Integrations API.
    """

    def __init__(self, session):
        """
        Initializes the IntegrationsAPI object.

        :param session: An instance of the HttpSession class

        :return IntegrationsAPI object.
        """

        super(IntegrationsAPI, self).__init__()

        self._session = session

    def create(self, name, type, enabled, data):
        """
        A method to create a new cloud integration.

        :param name: A string representing the integration name.
        :param type: A string representing the integration type.
        :param enabled: An integer representing whether the integration is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.

        :return response json
        """

        logger.info("Creating cloud integration in Lacework...")

        # Build the Host Vulnerabilities request URI
        api_uri = f"/api/v1/external/integrations"

        data = {
            "NAME": name,
            "TYPE": type,
            "ENABLED": enabled,
            "DATA": data
        }

        response = self._session.post(api_uri, data=data)

        return response.json()

    def get_all(self):
        """
        A method to get a list of all cloud integrations.

        :return response json
        """

        logger.info("Getting cloud integrations from Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations"

        response = self._session.get(api_uri)

        return response.json()

    def get_by_id(self, id):
        """
        A method to get the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.

        :return response json
        """

        logger.info("Getting cloud integration by ID from Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/{id}"

        response = self._session.get(api_uri)

        return response.json()

    def get_by_type(self, type):
        """
        A method to get the specified cloud integration.

        :param type: A string representing the integration type.

        :return response json
        """

        logger.info("Getting cloud integrations by type from Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/type/{type}"

        response = self._session.get(api_uri)

        return response.json()

    def update_by_id(self, id, name, type, enabled, data):
        """
        A method to update the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.
        :param name: A string representing the integration name.
        :param type: A string representing the integration type.
        :param enabled: An integer representing whether the integration is enabled. (0 or 1)
        :param data: A JSON object matching the schema for the specified type.

        :return response json
        """

        logger.info("Updating cloud integration in Lacework...")

        # Build the Host Vulnerabilities request URI
        api_uri = f"/api/v1/external/integrations/{id}"

        data = {
            "NAME": name,
            "TYPE": type,
            "ENABLED": enabled,
            "DATA": data
        }

        response = self._session.patch(api_uri, data=data)

        return response.json()

    def update_status(self, id, enabled):
        """
        A method to update the status of a specified cloud integration.

        :param id: A string representing the Lacework integration GUID.
        :param enabled: A boolean representing whether the integration is enabled.

        :return response json
        """

        logger.info("Updating cloud integration status in Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/updateStatus/{id}"

        data = {
            "ENABLED": enabled
        }

        response = self._session.put(api_uri, data=data)

        return response.json()

    def delete_by_id(self, id):
        """
        A method to delete the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.

        :return response json
        """

        logger.info("Deleting cloud integration by ID from Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/{id}"

        response = self._session.delete(api_uri)

        return response.json()

    def get_schema(self, type):
        """
        A method to get the schema for a specified cloud integration type.

        :param type: A string representing the integration type.

        :return response json
        """

        logger.info("Getting cloud integration schema by type from Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/schema/{type}"

        response = self._session.get(api_uri)

        return response.json()
