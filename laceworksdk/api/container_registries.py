# -*- coding: utf-8 -*-
"""
Lacework Container Registries API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class ContainerRegistriesAPI(object):
    """
    Lacework Container Registries API.
    """

    def __init__(self, session):
        """
        Initializes the ContainerRegistriesAPI object.

        :param session: An instance of the HttpSession class

        :return ContainerRegistriesAPI object.
        """

        super(ContainerRegistriesAPI, self).__init__()

        self._session = session

    def create(self,
               name,
               type,
               enabled,
               data,
               org=False):
        """
        A method to create a new container registry.

        :param name: A string representing the container registry name.
        :param type: A string representing the container registry type.
        :param enabled: A boolean/integer representing whether the container registry is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating container registry in Lacework...")

        # Build the Container Registries request URI
        api_uri = "/api/v2/ContainerRegistries"

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
        A method to get all container registries.

        :param guid: A string representing the container registry GUID.
        :param type: A string representing the container registry type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting container registry info from Lacework...")

        # Build the Container Registries request URI
        if guid:
            api_uri = f"/api/v2/ContainerRegistries/{guid}"
        elif type:
            api_uri = f"/api/v2/ContainerRegistries/{type}"
        else:
            api_uri = "/api/v2/ContainerRegistries"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_type(self,
                    type,
                    org=False):
        """
        A method to get all container registries by type.

        :param type: A string representing the container registry type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(type=type, org=org)

    def get_by_guid(self,
                    guid,
                    org=False):
        """
        A method to get all container registries.

        :param guid: A string representing the container registry GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search container registries.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching container registries from Lacework...")

        # Build the Container Registries request URI
        api_uri = "/api/v2/ContainerRegistries/search"

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
        A method to update an container registry.

        :param guid: A string representing the container registry GUID.
        :param name: A string representing the container registry name.
        :param type: A string representing the container registry type.
        :param enabled: A boolean/integer representing whether the container registry is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating container registry in Lacework...")

        # Build the Container Registries request URI
        api_uri = f"/api/v2/ContainerRegistries/{guid}"

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
        A method to delete an container registry.

        :param guid: A string representing the container registry GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting container registry in Lacework...")

        # Build the Container Registries request URI
        api_uri = f"/api/v2/ContainerRegistries/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
