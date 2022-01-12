# -*- coding: utf-8 -*-
"""
Lacework Integrations API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class IntegrationsAPI:
    """
    Lacework Integrations API.
    """

    def __init__(self, session):
        """
        Initializes the IntegrationsAPI object.

        :param session: An instance of the HttpSession class

        :return IntegrationsAPI object.
        """

        super().__init__()

        self._session = session

    def create(self,
               name,
               type,
               enabled,
               data):
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

        # Build the Integrations request URI
        api_uri = "/api/v1/external/integrations"

        data = {
            "NAME": name,
            "TYPE": type,
            "ENABLED": int(bool(enabled)),
            "DATA": data
        }

        response = self._session.post(api_uri, data=data)

        return response.json()

    def get(self,
            guid=None,
            schema=None,
            type=None):
        """
        A generic method to get cloud integrations.

        :param guid: A string representing the integration GUID.
        :param schema: A string representing the schema type.
        :param type: A string representing the integration type.

        :return response json
        """

        logger.info("Getting cloud integrations from Lacework...")

        # Build the Integrations request URI
        if guid:
            api_uri = f"/api/v1/external/integrations/{guid}"
        elif type:
            api_uri = f"/api/v1/external/integrations/type/{type}"
        elif schema:
            api_uri = f"/api/v1/external/integrations/schema/{schema}"
        else:
            api_uri = "/api/v1/external/integrations"

        response = self._session.get(api_uri)

        return response.json()

    def get_all(self):
        """
        A method to get a list of all cloud integrations.

        :return response json
        """

        logger.warning("The 'get_all' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get()

    def get_by_id(self,
                  id):
        """
        A method to get the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.

        :return response json
        """

        logger.warning("The 'get_by_id' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get(guid=id)

    def get_by_type(self,
                    type):
        """
        A method to get the specified cloud integration.

        :param type: A string representing the integration type.

        :return response json
        """

        logger.warning("The 'get_by_type' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get(type=type)

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               data=None):
        """
        A method to update the specified cloud integration.

        :param guid: A string representing the Lacework integration GUID.
        :param name: A string representing the integration name.
        :param type: A string representing the integration type.
        :param enabled: An integer representing whether the integration is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.

        :return response json
        """

        logger.info("Updating cloud integration in Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/{guid}"

        tmp_data = {}

        if name:
            tmp_data["NAME"] = name
        if type:
            tmp_data["TYPE"] = type
        if enabled is not None:
            tmp_data["ENABLED"] = int(bool(enabled))
        if data:
            tmp_data["DATA"] = data

        response = self._session.patch(api_uri, data=tmp_data)

        return response.json()

    def update_by_id(self,
                     id,
                     name=None,
                     type=None,
                     enabled=None,
                     data=None):
        """
        A method to update the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.
        :param name: A string representing the integration name.
        :param type: A string representing the integration type.
        :param enabled: An integer representing whether the integration is enabled. (0 or 1)
        :param data: A JSON object matching the schema for the specified type.

        :return response json
        """

        logger.warning("The 'update_by_id' function may be deprecated shortly, please consider switching to 'update'.")

        return self.update(guid=id, name=name, type=type, enabled=enabled, data=data)

    def update_status(self,
                      id,
                      enabled):
        """
        A method to update the status of a specified cloud integration.

        :param id: A string representing the Lacework integration GUID.
        :param enabled: A boolean representing whether the integration is enabled.

        :return response json
        """

        logger.warning("The 'update_status' function may be deprecated shortly, please consider switching to 'update'.")

        return self.update(guid=id, enabled=enabled)

    def delete(self,
               guid):
        """
        A method to delete the specified cloud integration.

        :param guid: A string representing the Lacework integration GUID.

        :return response json
        """

        logger.info("Deleting cloud integration in Lacework...")

        # Build the Integrations request URI
        api_uri = f"/api/v1/external/integrations/{guid}"

        response = self._session.delete(api_uri)

        return response.json()

    def delete_by_id(self,
                     id):
        """
        A method to delete the specified cloud integration.

        :param id: A string representing the Lacework integration GUID.

        :return response json

        **** Needs to be deprecated
        """

        logger.warning("The 'delete_by_id' function may be deprecated shortly, please consider switching to 'delete'.")

        return self.delete(guid=id)

    def get_schema(self, type):
        """
        A method to get the schema for a specified cloud integration type.

        :param type: A string representing the integration type.

        :return response json
        """

        logger.info("Getting cloud integration schema from Lacework...")

        return self.get(schema=type)
