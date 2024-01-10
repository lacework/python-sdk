# -*- coding: utf-8 -*-
"""Lacework ReportDefinitions API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ReportDefinitionsAPI(CrudEndpoint):
    """A class used to represent the `Report Definition API endpoint <https://yourlacework.lacework.net/api/v2/docs-beta#tag/ReportDefinitions>`_

    A report definition contains data retrieval and layout information for a report. Lacework provides endpoints to\
    create a report definition, to list all definitions, and to update or delete a definition.
    """

    def __init__(self, session):
        """Initializes the ReportDefinitionsAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            ReportDefinitionsAPI: An instance of this class

        """

        super().__init__(session, "ReportDefinitions")

    def create(
        self,
        report_name,
        report_type,
        sub_report_type,
        report_definition,
        **request_params,
    ):
        """A method to create a new report definition.

        Args:
          report_name (str): The name of the report definition.
          report_type (str): Type of the report definition. Valid values: "COMPLIANCE"
          sub_report_type (str): The sub-type of the report definition. Valid values: "AWS", "GCP", "Azure"
          report_definition (dict): A dictionary representing the report definition. Fields are:

            - sections (list of dicts): A list of dictionaries representing the sections of the report definition. \
            Fields are:

                - category (str): The section's category.
                - title (str): The section's title.
                - policies (list of str): A list strings representing the section's policies.

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The created report definition

        """
        return super().create(
            report_name=report_name,
            report_type=report_type,
            sub_report_type=sub_report_type,
            report_definition=report_definition,
            **request_params,
        )

    def get(self, id=None):
        """A method to get report definitions. Using no args will get all report definitions.

        Args:
          id (str, optional): The report definition ID to get.

        Returns:
            dict: The requested report definition(s)

        """
        return super().get(id=id)

    def get_by_id(self, id):
        """A method to get a report definition by ID.

        Args:
          id (str): The report definition ID to get.

        Returns:
            dict: The requested report definition

        """
        return self.get(id=id)

    def search(self):
        """A method to 'pass' when attempting to search ReportDefinitions objects.

        Search functionality is not yet implemented for Alert Profiles.
        """
        pass

    def update(self, id, report_name, report_definition, **request_params):
        """A method to update a report definition.

        Args:
          id: A string representing the object ID.
          report_name (str): The name of the report definition.
          report_definition (dict): A dictionary representing the report definition. Fields are:

            - sections (list of dicts): A list of dictionaries representing the sections of the report definition. \
            Fields are:

                - category (str): The section's category.
                - title (str): The section's title.
                - policies (list of str): A list strings representing the section's policies.

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated report definition
        """
        json = self._build_dict_from_items(
            report_name=report_name,
            report_definition=report_definition,
            **request_params,
        )

        response = self._session.patch(self._build_url(id=id), json=json)

        return response.json()

    def delete(self, id):
        """A method to delete a report definition.

        Args:
          id (str): The ID of the report definition to delete.

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=id)
