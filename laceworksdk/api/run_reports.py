"""
Lacework Run Reports API wrapper.
"""

import json
import logging

logger = logging.getLogger(__name__)


class RunReportsAPI(object):
    """
    Lacework RunReports API.
    """

    def __init__(self, session):
        """
        Initializes the RunReportsAPI object.

        :param session: An instance of the HttpSession class

        :return RunReportsAPI object.
        """

        super(RunReportsAPI, self).__init__()

        self._session = session

    def aws(self, aws_account_id):
        """
        A method to initiate a compliance assessment for an AWS account.

        :param aws_account_id: A string representing which AWS account to assess.

        :return response json
        """

        logger.info("Initiating AWS compliance assessment in Lacework...")

        # Build the Run Report request URI
        api_uri = f"/api/v1/external/runReport/aws/{aws_account_id}"

        response = self._session.post(api_uri)

        return response.json()

    def azure(self, azure_tenant_id):
        """
        A method to initiate a compliance assessment for an Azure tenant.

        :param azure_tenant_id: A string representing which Azure tenant to assess.

        :return response json
        """

        logger.info("Initiating Azure compliance assessment in Lacework...")

        # Build the Run Report request URI
        api_uri = f"/api/v1/external/runReport/azure/{azure_tenant_id}"

        response = self._session.post(api_uri)

        return response.json()

    def gcp(self, gcp_project_id):
        """
        A method to initiate a compliance assessment for a GCP project.

        :param gcp_project_id: A string representing which GCP project to assess.

        :return response json
        """

        logger.info("Initiating GCP compliance assessment in Lacework...")

        # Build the Run Report request URI
        api_uri = f"/api/v1/external/runReport/gcp/{gcp_project_id}"

        response = self._session.post(api_uri)

        return response.json()

    def integration(self, integration_guid):
        """
        A method to run a compliance report based on a Lacework integration GUID.

        :param integration_guid: A string representing the Lacework integration ID to query.

        :return response json
        """

        logger.info("Initiating compliance assessment for a Lacework integration ID...")

        # Build the Run Report request URI
        api_uri = f"/api/v1/external/runReport/integration/{integration_guid}"

        response = self._session.post(api_uri)

        return response.json()
