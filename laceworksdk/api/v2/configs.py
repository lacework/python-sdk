# -*- coding: utf-8 -*-
"""Lacework Configs API wrapper."""

from laceworksdk.api.read_endpoint import ReadEndpoint
from laceworksdk.api.search_endpoint import SearchEndpoint


class ConfigsAPI:
    """A class used to represent the `Configs API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Configs>`_

    Get information about compliance configurations.

    The Configs API endpoint is a parent for different types of configs that can be queried.

    Attributes:
        compliance_evaluations (ComplianceEvaluationsAPI):  A ComplianceEvaluationsAPI instance.
        azure_subscriptions (AzureSubscriptions): An AzureSubscriptions instance.
        gcp_projects (GcpProjects): A GcpProjects instance.
    """

    def __init__(self, session):
        """Initializes the ConfigsAPI object.

        Args:
            session (HttpSession): An instance of the HttpSession class

        Returns:
            ConfigsAPI: An instance of this class..
        """
        super().__init__()
        self._base_path = "Configs"

        self.azure_subscriptions = self.AzureSubscriptions(session, self._base_path)
        self.compliance_evaluations = self.ComplianceEvaluationsAPI(session, self._base_path)
        self.gcp_projects = self.GcpProjects(session, self._base_path)


    class AzureSubscriptions(ReadEndpoint):
        """A class used to represent the Azure Subscriptions API endpoint.

        Get a list of Azure subscription IDs for an entire account or for a specific Azure tenant.

        """

        RESOURCE = "AzureSubscriptions"


    class GcpProjects(ReadEndpoint):
        """A class used to represent the GCP Projects API endpoint."""

        RESOURCE = "GcpProjects"


    class ComplianceEvaluationsAPI(SearchEndpoint):
        """A class used to represent the Compliance Evaluations API endpoint."""

        RESOURCE = "ComplianceEvaluations"
