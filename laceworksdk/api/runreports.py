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


    def run_aws_report(self, aws_account_id):
        """
        A method to run a compliance report for an AWS account.

        : param aws_account_id: A string representing which AWS Account to query.

        :return response json
        """

        # Build the Run Report request URI
        
        api_uri = f"/api/v1/external/runReport/aws/{aws_account_id}"

        response = self._session.post(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()


    def run_azure_report(self, azure_tenant_id):
        """
        A method to run a compliance report for an Azure Tenant account.

        : param azure_tenant_id: A string representing which Azure Tenant account to query.

        :return response json
        """

        # Build the Run Report request URI
        
        api_uri = f"/api/v1/external/runReport/azure/{azure_tenant_id}"

        response = self._session.post(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()

    def run_gcp_report(self, gcp_project_id):
        """
        A method to run a compliance report for a GCP Project.

        : param gcp_project_id: A string representing which GCP Project to query.

        :return response json
        """

        # Build the Run Report request URI
        
        api_uri = f"/api/v1/external/runReport/gcp/{gcp_project_id}"

        response = self._session.post(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()