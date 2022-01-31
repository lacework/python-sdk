"""
Lacework Run Reports API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class RunReportsAPI:
    """
    Lacework RunReports API.
    """

    def __init__(self, session):
        """
        Initializes the RunReportsAPI object.

        :param session: An instance of the HttpSession class

        :return RunReportsAPI object.
        """

        super().__init__()

        self._session = session

    def run_report(self,
                   type,
                   account_id):
        """
        A method to initiate a compliance assessment.

        :param type: A string representing the type of compliance assessment to initiate.
        :param account_id: A string representing the account identifier for which to initiate a compliance assessment.

        :return response json
        """

        logger.info(f"Initiating '{type}' compliance assessment in Lacework...")

        # Build the Run Report request URI
        api_uri = f"/api/v1/external/runReport/{type}/{account_id}"

        response = self._session.post(api_uri)

        return response.json()

    def aws(self,
            aws_account_id):
        """
        A method to initiate a compliance assessment for an AWS account.

        :param aws_account_id: A string representing which AWS account to assess.

        :return response json
        """

        return self.run_report("aws", aws_account_id)

    def azure(self,
              azure_tenant_id):
        """
        A method to initiate a compliance assessment for an Azure tenant.

        :param azure_tenant_id: A string representing which Azure tenant to assess.

        :return response json
        """

        return self.run_report("azure", azure_tenant_id)

    def gcp(self,
            gcp_project_id):
        """
        A method to initiate a compliance assessment for a GCP project.

        :param gcp_project_id: A string representing which GCP project to assess.

        :return response json
        """

        return self.run_report("gcp", gcp_project_id)

    def integration(self,
                    integration_guid):
        """
        A method to run a compliance report based on a Lacework integration GUID.

        :param integration_guid: A string representing the Lacework integration ID to query.

        :return response json
        """

        return self.run_report("integration", integration_guid)
