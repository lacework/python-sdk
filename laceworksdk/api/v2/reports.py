# -*- coding: utf-8 -*-
"""Lacework Reports API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class ReportsAPI(BaseEndpoint):
    """A class used to represent the `Reports API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Reports>`_

    Lacework combines details about non-compliant resources that are in violation into reports. You must configure at
    least one cloud integration with AWS, Azure, or GCP to receive these reports.
    """

    def __init__(self, session):
        """Initializes the ReportsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            ReportsAPI: An instance of this class
        """
        super().__init__(session, "Reports")

    def get(
        self,
        primary_query_id=None,
        secondary_query_id=None,
        format=None,
        report_type=None,
        **request_params,
    ):
        """A method to get Reports objects.

        Args:
          primary_query_id (str): The primary ID that is used to fetch the report. (AWS Account ID or Azure Tenant ID)
          secondary_query_id (str): The secondary ID that is used to fetch the report. (GCP Project ID or Azure Subscription ID)
          format (str, optional): The format of the report. Valid values: "csv", "html", "json", "pdf"
          report_type (str): The type of the report. See `available reports <https://docs.lacework.net/console/compliance-frameworks>`_ for a list of report types.\
          Valid values are in the "API Format" column.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The details of the report
        """

        params = self._build_dict_from_items(
            primary_query_id=primary_query_id,
            secondary_query_id=secondary_query_id,
            format=format,
            report_type=report_type,
            **request_params,
        )

        response = self._session.get(self._build_url(), params=params)

        if format == "json":
            return response.json()
        else:
            return response.content
