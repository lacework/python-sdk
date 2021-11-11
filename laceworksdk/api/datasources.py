# -*- coding: utf-8 -*-
"""
Lacework Datasources API wrapper.
"""

import logging

import bleach

logger = logging.getLogger(__name__)


class DatasourcesAPI:
    """
    Lacework Datasources API.
    """

    _DEFAULT_DESCRIPTION = "No description available."

    def __init__(self, session):
        """
        Initializes the Datasources object.

        :param session: An instance of the HttpSession class

        :return DatasourcesAPI object.
        """

        super(DatasourcesAPI, self).__init__()

        self._session = session

    def get(self,
            type=None,
            org=False):
        """
        A method to get datasources.

        :param type: A string representing the type of Datasource.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        # Build the Datasources request URI
        if type:
            type_clean = bleach.clean(type)
            logger.info(f"Getting datasource info for '{type_clean}' from Lacework...")
            api_uri = f"/api/v2/Datasources/{type_clean}"
        else:
            logger.info("Getting datasource info from Lacework...")
            api_uri = "/api/v2/Datasources"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_type(self,
                    type,
                    org=False):
        """
        A method to get a datasource by type.

        :param type: A string representing the type of Datasource.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(type=type, org=org)

    def get_datasource_schema(self,
                              data_source):
        """
        A method to get the schema for a particular datasource.

        :param data_source: A string representing the datasource to check for.

        :return response json
        """

        return self.get(type=data_source)

    def list_data_sources(self):
        """
        A method to list the datasources that are available.

        :return A list of tuples with two entries, source name and description.
        """

        logger.info("Getting list of data sources Lacework...")

        response_json = self.get()

        return_sources = []
        data_sources = response_json.get("data", [])
        for data_source in data_sources:
            description = data_source.get(
                "description", self._DEFAULT_DESCRIPTION)
            if description == 'None':
                description = self._DEFAULT_DESCRIPTION

            return_sources.append(
                (data_source.get("name", "No name"), description))

        return return_sources
