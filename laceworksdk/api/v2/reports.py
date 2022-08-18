# -*- coding: utf-8 -*-
"""
Lacework Reports API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class ReportsAPI(BaseEndpoint):

    def __init__(self, session):
        """
        Initializes the ReportsAPI object.

        :param session: An instance of the HttpSession class

        :return ReportsAPI object.
        """

        super().__init__(session, "Reports")

    def get(self,
            primary_query_id=None,
            secondary_query_id=None,
            format=None,
            type=None,
            report_name=None,
            report_type=None,
            template_name=None,
            latest=None,
            **request_params):
        """
        A method to get Reports objects.

        :param primary_query_id: The primary ID that is used to fetch the report.
            (AWS Account ID or Azure Tenant ID)
        :param secondary_query_id: The secondary ID that is used to fetch the report.
            (GCP Project ID or Azure Subscription ID)
        :param format: The format of the report.
            ("csv", "html", "json", "pdf")
        :param type: The type of the report.
        :param report_name: The name of the report definition to use when generating the report.
        :param report_type: The type of the report definition to use when generating the report.
        :param template_name: The name of the template to be used for the report.
        :param latest: A boolean representing whether to retreive the latest report.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            primary_query_id=primary_query_id,
            secondary_query_id=secondary_query_id,
            format=format,
            type=type,
            report_name=report_name,
            report_type=report_type,
            template_name=template_name,
            latest=latest,
            **request_params
        )

        response = self._session.get(self.build_url(), params=params)

        if format == "json":
            return response.json()
        else:
            return response.content
