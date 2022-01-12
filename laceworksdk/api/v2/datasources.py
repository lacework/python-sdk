# -*- coding: utf-8 -*-
"""
Lacework Datasources API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class DatasourcesAPI(BaseEndpoint):

    _DEFAULT_DESCRIPTION = "No description available."

    def __init__(self, session):
        """
        Initializes the Datasources object.

        :param session: An instance of the HttpSession class

        :return DatasourcesAPI object.
        """

        super().__init__(session, "Datasources")

    def get(self,
            type=None):
        """
        A method to get Datasources objects.

        :param type: A string representing the object type.

        :return response json
        """

        response = self._session.get(self.build_url(resource=type))

        return response.json()

    def get_by_type(self,
                    type):
        """
        A method to get a Datasources object by type.

        :param type: A string representing the object type.

        :return response json
        """

        return self.get(type=type)

    def get_datasource(self,
                       datasource):
        """
        A method to get the schema for a particular datasource.

        :param datasource: A string representing the datasource to check for.

        :return response json
        """

        return self.get(type=datasource)

    def list_data_sources(self):
        """
        A method to list the datasources that are available.

        :return A list of tuples with two entries, source name and description.
        """

        response_json = self.get()

        return_sources = []
        data_sources = response_json.get("data", [])
        for data_source in data_sources:
            description = data_source.get(
                "description", self._DEFAULT_DESCRIPTION)
            if description == "None":
                description = self._DEFAULT_DESCRIPTION

            return_sources.append(
                (data_source.get("name", "No name"), description))

        return return_sources
