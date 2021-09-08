# -*- coding: utf-8 -*-
"""
Lacework API wrappers.
"""

import os

from dotenv import load_dotenv
import configparser

from laceworksdk.http_session import HttpSession
from .account import AccountAPI
from .agent_access_tokens import AgentAccessTokensAPI
from .alert_channels import AlertChannelsAPI
from .alert_rules import AlertRulesAPI
from .audit_logs import AuditLogsAPI
from .cloud_accounts import CloudAccountsAPI
from .cloud_activities import CloudActivitiesAPI
from .compliance import ComplianceAPI
from .container_registries import ContainerRegistriesAPI
from .contract_info import ContractInfoAPI
from .custom_compliance_config import CustomComplianceConfigAPI
from .download_file import DownloadFileAPI
from .events import EventsAPI
from .integrations import IntegrationsAPI
from .policies import PoliciesAPI
from .queries import QueriesAPI
from .recommendations import RecommendationsAPI
from .report_rules import ReportRulesAPI
from .resource_groups import ResourceGroupsAPI
from .run_reports import RunReportsAPI
from .schemas import SchemasAPI
from .suppressions import SuppressionsAPI
from .team_members import TeamMembersAPI
from .token import TokenAPI
from .user_profile import UserProfileAPI
from .vulnerability import VulnerabilityAPI

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


class LaceworkClient(object):
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
            os.path.expanduser('~'), LACEWORK_CLI_CONFIG_RELATIVE_PATH)

        if os.path.isfile(config_file_path):
            profile = profile or os.getenv(
                LACEWORK_API_CONFIG_SECTION_ENVIRONMENT_VARIABLE, 'default')
            config_obj = configparser.ConfigParser()
            config_obj.read([config_file_path])
            if config_obj.has_section(profile):
                config_section = config_obj[profile]
                api_key = config_section.get('api_key', '').strip('""')
                if not self._api_key and api_key:
                    self._api_key = api_key

                api_secret = config_section.get('api_secret', '').strip('""')
                if not self._api_secret and api_secret:
                    self._api_secret = api_secret

                account = config_section.get('account', '').strip('""')
                if not self._account and account:
                    self._account = account

                subaccount = config_section.get('subaccount', '').strip('""')
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
        self.agent_access_tokens = AgentAccessTokensAPI(self._session)
        self.alert_channels = AlertChannelsAPI(self._session)
        self.alert_rules = AlertRulesAPI(self._session)
        self.audit_logs = AuditLogsAPI(self._session)
        self.cloud_accounts = CloudAccountsAPI(self._session)
        self.cloud_activities = CloudActivitiesAPI(self._session)
        self.compliance = ComplianceAPI(self._session)
        self.compliance.config = CustomComplianceConfigAPI(self._session)
        self.container_registries = ContainerRegistriesAPI(self._session)
        self.contract_info = ContractInfoAPI(self._session)
        self.events = EventsAPI(self._session)
        self.files = DownloadFileAPI(self._session)
        self.integrations = IntegrationsAPI(self._session)
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
        self.vulnerabilities = VulnerabilityAPI(self._session)
