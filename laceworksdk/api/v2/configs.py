# -*- coding: utf-8 -*-
"""
Lacework Configs API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class ConfigsAPI:

    def __init__(self, session):
        """
        Initializes the ConfigsAPI object.

        :param session: An instance of the HttpSession class

        :return ConfigsAPI object.
        """

        super().__init__()
        self._base_path = "Configs"

        self.compliance_evaluations = ComplianceEvaluationsAPI(session, self._base_path)


class ComplianceEvaluationsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ComplianceEvaluationsAPI object.

        :param session: An instance of the HttpSession class

        :return ComplianceEvaluationsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search ComplianceEvaluations objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="ComplianceEvaluations", json=json)
