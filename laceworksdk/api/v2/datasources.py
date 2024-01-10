# -*- coding: utf-8 -*-
"""Lacework Datasources API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class DatasourcesAPI(BaseEndpoint):
    """A class used to represent the `Datasources API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Datasources>`_

    Get schema details for all datasources that you can query using LQL.
    """

    _DEFAULT_DESCRIPTION = "No description available."

    def __init__(self, session):
        """Initializes the Datasources object.

        Args:
            session (HttpSession): An instance of the HttpSession class

        Returns:
            DatasourcesAPI: An instance of this class
        """
        super().__init__(session, "Datasources")

    def get(self):
        """A method to get Datasources.

        Returns:
            dict: All datasources
        """
        response = self._session.get(self._build_url())
        return response.json()

    def get_datasource(self, datasource):
        """A method to get the schema for a particular datasource.

        Args:
          datasource (str): The name of the datasource schema get.

        Returns:
            dict: The datasource schema.
        """
        return self._session.get(self._build_url(resource=datasource)).json()

    def list_data_sources(self):
        """A method to list the datasources that are available.

        Returns:
            list of tuples: Each tuple has two entries, source name and description.
        """
        response_json = self.get()

        return_sources = []
        data_sources = response_json.get("data", [])
        for data_source in data_sources:
            description = data_source.get("description", self._DEFAULT_DESCRIPTION)
            if description == "None":
                description = self._DEFAULT_DESCRIPTION

            return_sources.append((data_source.get("name", "No name"), description))

        return return_sources
