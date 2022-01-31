# -*- coding: utf-8 -*-
"""
Lacework Configs API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class ConfigsAPI:
    """A class used to represent the Configs API endpoint.

    The Configs API endpoint is simply a parent for different types of
    configs that can be queried.

    Attributes
    ----------
    compliance_evaluations:
        A ComplianceEvaluationsAPI instance.
    """

    def __init__(self, session):
        """Initializes the ConfigsAPI object.

        :param session: An instance of the HttpSession class

        :return ConfigsAPI object.
        """

        super().__init__()
        self._base_path = "Configs"

        self.compliance_evaluations = ComplianceEvaluationsAPI(session, self._base_path)


class ComplianceEvaluationsAPI(SearchEndpoint):
    """A class used to represent the Compliance Evaluations API endpoint.

    Methods
    -------
    search(json=None)
        A method to search ComplianceEvaluations objects.
    """
    RESOURCE = "ComplianceEvaluations"
