# -*- coding: utf-8 -*-
"""
Lacework API wrappers.
"""

import os

from dotenv import load_dotenv
import configparser

from laceworksdk.http_session import HttpSession

from .v1.account import AccountAPI
from .v1.compliance import ComplianceAPI
from .v1.custom_compliance_config import CustomComplianceConfigAPI
from .v1.download_file import DownloadFileAPI
from .v1.events import EventsAPI
from .v1.integrations import IntegrationsAPI
from .v1.recommendations import RecommendationsAPI
from .v1.run_reports import RunReportsAPI
from .v1.suppressions import SuppressionsAPI
from .v1.token import TokenAPI

from .v2.activities import ActivitiesAPI
from .v2.agent_access_tokens import AgentAccessTokensAPI
from .v2.alert_channels import AlertChannelsAPI
from .v2.alert_profiles import AlertProfilesAPI
from .v2.alert_rules import AlertRulesAPI
from .v2.alerts import AlertsAPI
from .v2.audit_logs import AuditLogsAPI
from .v2.cloud_accounts import CloudAccountsAPI
from .v2.cloud_activities import CloudActivitiesAPI
from .v2.configs import ConfigsAPI
from .v2.container_registries import ContainerRegistriesAPI
from .v2.contract_info import ContractInfoAPI
from .v2.datasources import DatasourcesAPI
from .v2.entities import EntitiesAPI
from .v2.evidence import EvidenceAPI
from .v2.organization_info import OrganizationInfoAPI
from .v2.policies import PoliciesAPI
from .v2.queries import QueriesAPI
from .v2.report_rules import ReportRulesAPI
from .v2.resource_groups import ResourceGroupsAPI
from .v2.schemas import SchemasAPI
from .v2.team_members import TeamMembersAPI
from .v2.user_profile import UserProfileAPI
from .v2.vulnerabilities import VulnerabilitiesAPI
from .v2.vulnerability_exceptions import VulnerabilityExceptionsAPI
from .v2.vulnerability_policies import VulnerabilityPoliciesAPI

from laceworksdk.config import (
    LACEWORK_ACCOUNT_ENVIRONMENT_VARIABLE,
    LACEWORK_SUBACCOUNT_ENVIRONMENT_VARIABLE,
    LACEWORK_API_KEY_ENVIRONMENT_VARIABLE,
    LACEWORK_API_SECRET_ENVIRONMENT_VARIABLE,
    LACEWORK_API_BASE_DOMAIN_ENVIRONMENT_VARIABLE,
    LACEWORK_API_CONFIG_SECTION_ENVIRONMENT_VARIABLE,
    LACEWORK_CLI_CONFIG_RELATIVE_PATH
)

load_dotenv()


class LaceworkClient:
    """
    Lacework API wrapper for Python.
    """

    def __init__(self,
                 account=None,
                 subaccount=None,
                 api_key=None,
                 api_secret=None,
                 instance=None,
                 base_domain=None,
                 profile=None):
        """
        Initializes the Lacework Client object.

        Order of operation is:
            1. Parameters passed in via the init function (flags).
            2. Environmental variables.
            3. Configuration file, located in ~/.lacework.toml

        :return LaceworkClient object.
        """

        # Attempt to use Environment Variables
        self._account = account or instance or os.getenv(
            LACEWORK_ACCOUNT_ENVIRONMENT_VARIABLE)
        self._subaccount = subaccount or os.getenv(
            LACEWORK_SUBACCOUNT_ENVIRONMENT_VARIABLE)
        self._api_key = api_key or os.getenv(
            LACEWORK_API_KEY_ENVIRONMENT_VARIABLE)
        self._api_secret = api_secret or os.getenv(
            LACEWORK_API_SECRET_ENVIRONMENT_VARIABLE)
        self._base_domain = base_domain or os.getenv(
            LACEWORK_API_BASE_DOMAIN_ENVIRONMENT_VARIABLE)

        config_file_path = os.path.join(
            os.path.expanduser("~"), LACEWORK_CLI_CONFIG_RELATIVE_PATH)

        if os.path.isfile(config_file_path):
            profile = profile or os.getenv(
                LACEWORK_API_CONFIG_SECTION_ENVIRONMENT_VARIABLE, "default")
            config_obj = configparser.ConfigParser()
            config_obj.read([config_file_path])
            if config_obj.has_section(profile):
                config_section = config_obj[profile]
                api_key = config_section.get("api_key", "").strip('""')
                if not self._api_key and api_key:
                    self._api_key = api_key

                api_secret = config_section.get("api_secret", "").strip('""')
                if not self._api_secret and api_secret:
                    self._api_secret = api_secret

                account = config_section.get("account", "").strip('""')
                if not self._account and account:
                    self._account = account

                subaccount = config_section.get("subaccount", "").strip('""')
                if not self._subaccount and subaccount:
                    self._subaccount = subaccount

        # Create an HttpSession instance
        self._session = HttpSession(
            self._account,
            self._subaccount,
            self._api_key,
            self._api_secret,
            self._base_domain
        )

        # API Wrappers
        self.account = AccountAPI(self._session)
        self.activities = ActivitiesAPI(self._session)
        self.agent_access_tokens = AgentAccessTokensAPI(self._session)
        self.alert_channels = AlertChannelsAPI(self._session)
        self.alert_profiles = AlertProfilesAPI(self._session)
        self.alert_rules = AlertRulesAPI(self._session)
        self.alerts = AlertsAPI(self._session)
        self.audit_logs = AuditLogsAPI(self._session)
        self.cloud_accounts = CloudAccountsAPI(self._session)
        self.cloud_activities = CloudActivitiesAPI(self._session)
        self.compliance = ComplianceAPI(self._session)
        self.compliance.config = CustomComplianceConfigAPI(self._session)
        self.configs = ConfigsAPI(self._session)
        self.container_registries = ContainerRegistriesAPI(self._session)
        self.contract_info = ContractInfoAPI(self._session)
        self.datasources = DatasourcesAPI(self._session)
        self.entities = EntitiesAPI(self._session)
        self.events = EventsAPI(self._session)
        self.evidence = EvidenceAPI(self._session)
        self.files = DownloadFileAPI(self._session)
        self.integrations = IntegrationsAPI(self._session)
        self.organization_info = OrganizationInfoAPI(self._session)
        self.policies = PoliciesAPI(self._session)
        self.queries = QueriesAPI(self._session)
        self.recommendations = RecommendationsAPI(self._session)
        self.report_rules = ReportRulesAPI(self._session)
        self.resource_groups = ResourceGroupsAPI(self._session)
        self.run_reports = RunReportsAPI(self._session)
        self.schemas = SchemasAPI(self._session)
        self.suppressions = SuppressionsAPI(self._session)
        self.team_members = TeamMembersAPI(self._session)
        self.tokens = TokenAPI(self._session)
        self.user_profile = UserProfileAPI(self._session)
        self.vulnerabilities = VulnerabilitiesAPI(self._session)
        self.vulnerability_exceptions = VulnerabilityExceptionsAPI(self._session)
        self.vulnerability_policies = VulnerabilityPoliciesAPI(self._session)

    def set_org_level_access(self, org_level_access):
        """
        A method to set whether the client should use organization-level API calls.
        """

        if org_level_access is True:
            self._session._org_level_access = True
        else:
            self._session._org_level_access = False

    def set_subaccount(self, subaccount):
        """
        A method to update the subaccount the client should use for API calls.
        """

        self._session._subaccount = subaccount
