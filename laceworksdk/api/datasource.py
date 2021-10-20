# -*- coding: utf-8 -*-
"""
Lacework DataSource API wrapper.
"""

import logging

import bleach

logger = logging.getLogger(__name__)


class DataSourceAPI:
    """
    Lacework DataSource API.
    """

    _DEFAULT_DESCRIPTION = "No description available."

    def __init__(self, session):
        """
        Initializes the DataSource object.

        :param session: An instance of the HttpSession class

        :return DataSourceAPI object.
        """

        super(DataSourceAPI, self).__init__()

        self._session = session

    def get_datasource_schema(
            self, data_source):
        """
        A method to get the schema for a particular data source.

        :param data_source: A string representing the data source to check for.

        :return response json
        """

        logger.info(
            "Getting the schema for a particular datasource from Lacework...")

        data_clean = bleach.clean(data_source)
        api_uri = f"/api/v2/Datasources/{data_clean}"

        response = self._session.get(api_uri)
        return response.json()


    def list_data_sources(self):
        """
        A method to list the data sources that are available.

        :return A list of tuples with two entries, source name and description.
        """
        logger.info("Getting list of data sources Lacework...")

        api_uri = "/api/v2/Datasources"
        response = self._session.get(api_uri)

        response_json = response.json()

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
