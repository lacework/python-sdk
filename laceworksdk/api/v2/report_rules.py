# -*- coding: utf-8 -*-
"""Lacework ReportRules API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ReportRulesAPI(CrudEndpoint):
    """A class used to represent the `Report Rules API endpoint <https://docs.lacework.net/api/v2/docs/#tag/ReportRules>`_

    Lacework combines alert channels and report rules to provide a flexible method for routing reports. For report\
    rules, you define information about which reports to send. For alert channels, you define where to send reports\
    such as to Jira, Slack, or email.
    """

    def __init__(self, session):
        """Initializes the ReportRulesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            ReportRulesAPI: An instance of this class

        """
        super().__init__(session, "ReportRules")

    def create(
        self, type, filters, intg_guid_list, report_notification_types, **request_params
    ):
        """A method to create a new report rule.

        Args:
          type (str): The type of report rule. Valid values: 'Report'
          intg_guid_list (list of str): A list of integration GUIDs representing the report channels to use.
          filters (dict): A dictionary containing the definition of the new rule. Fields are:

              - name (str): The report rule name
              - description (str, optional): The report rule description
              - enabled (bool|int): Whether the report rule is enabled
              - resourceGroups (list of str): A list of resource groups to apply the rule to
              - severity (list of ints): A list severities to apply the rule to. Valid values: \
              1=Critical 2=High 3=Medium 4=Low 5=Info


          report_notification_types (dict): A dict of booleans for the report types that you want the rule to apply\
          to. Fields are:

              "agentEvents", "awsCis14", "awsCisS3", "awsCloudtrailEvents", "awsComplianceEvents", "awsCis14IsoIec270022022",
              "awsCyberEssentials22", "awsCsaCcm405", "azureActivityLogEvents", "azureCis", "azureCis131", "azureComplianceEvents",
              "azurePci", "azurePciRev2", "azureSoc", "azureSocRev2", "azureIso27001", "azureHipaa", "azureNistCsf", "azureNist80053Rev5",
              "azureNist800171Rev2", "gcpAuditTrailEvents", "gcpCis", "gcpComplianceEvents", "gcpHipaa", "gcpHipaaRev2", "gcpIso27001",
              "gcpCis12", "gcpCis13", "gcpK8s", "gcpPci", "gcpPciRev2", "gcpSoc", "gcpSocRev2", "gcpNistCsf", "gcpNist80053Rev4",
              "gcpNist800171Rev2", "hipaa", "iso2700", "k8sAuditLogEvents", "nist800"-"53Rev4", "nist800"-"171Rev2", "openShiftCompliance",
              "openShiftComplianceEvents", "pci", "platformEvents", "soc", "awsSocRev2", "trendReport", "awsPciDss321", "awsNist80053Rev5",
              "awsSoc2", "awsNist800171Rev2", "awsNistCsf", "awsCmmc102", "awsHipaa", "awsIso270012013"

          request_params (dict, optional): Use to pass any additional parameters the API


        Returns:
            dict: The created report rule
        """
        return super().create(
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            report_notification_types=report_notification_types,
            **request_params,
        )

    def get(self, guid=None):
        """A method to get ReportRules objects. Using no args will get all report rules.

        Args:
          guid (str, optional): The GUID of the report rule to get

        Returns:
            dict: The requested report rule(s)

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get a report rule by GUID.

        Args:
          guid (str): The GUID of the report rule to get

        Returns:
            dict: The requested report rule(s)


        """
        return self.get(guid=guid)

    def update(
        self,
        guid,
        filters=None,
        intg_guid_list=None,
        report_notification_types=None,
        **request_params,
    ):
        """A method to update a ReportRules object.

        Args:
          guid (str): The GUID of the report rule to update
          intg_guid_list (list of str, optional): A list of integration GUIDs representing the report channels to use
          filters (dict, optional): A dictionary containing the definition of the new rule. Fields are:

              - name (str): The report rule name
              - description (str, optional): The report rule description
              - enabled (bool|int, optional): Whether the report rule is enabled
              - resourceGroups (list of str, optional): A list of resource groups to apply the rule to
              - severity (list of ints, optional): A list severities to apply the rule to. Valid values: \
              1=Critical 2=High 3=Medium 4=Low 5=Info


          report_notification_types (dict): A dict of booleans for the report types that you want the rule to apply\
          to. Fields are:

              "agentEvents", "awsCis14", "awsCisS3", "awsCloudtrailEvents", "awsComplianceEvents", "awsCis14IsoIec270022022",
              "awsCyberEssentials22", "awsCsaCcm405", "azureActivityLogEvents", "azureCis", "azureCis131", "azureComplianceEvents",
              "azurePci", "azurePciRev2", "azureSoc", "azureSocRev2", "azureIso27001", "azureHipaa", "azureNistCsf", "azureNist80053Rev5",
              "azureNist800171Rev2", "gcpAuditTrailEvents", "gcpCis", "gcpComplianceEvents", "gcpHipaa", "gcpHipaaRev2", "gcpIso27001",
              "gcpCis12", "gcpCis13", "gcpK8s", "gcpPci", "gcpPciRev2", "gcpSoc", "gcpSocRev2", "gcpNistCsf", "gcpNist80053Rev4",
              "gcpNist800171Rev2", "hipaa", "iso2700", "k8sAuditLogEvents", "nist800"-"53Rev4", "nist800"-"171Rev2", "openShiftCompliance",
              "openShiftComplianceEvents", "pci", "platformEvents", "soc", "awsSocRev2", "trendReport", "awsPciDss321", "awsNist80053Rev5",
              "awsSoc2", "awsNist800171Rev2", "awsNistCsf", "awsCmmc102", "awsHipaa", "awsIso270012013"

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The created report rule
        """
        return super().update(
            id=guid,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            report_notification_types=report_notification_types,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete a report rule.

        Args:
          guid (str): The GUID of the report rule to delete.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        return super().delete(id=guid)
