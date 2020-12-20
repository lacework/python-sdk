# -*- coding: utf-8 -*-
"""
Lacework API wrappers.
"""

import os

from dotenv import load_dotenv
from laceworksdk.http_session import HttpSession
from .alert_channels import AlertChannelsAPI
from .audit_logs import AuditLogsAPI
from .cloudtrail import CloudTrailAPI
from .compliance import ComplianceAPI
from .custom_compliance_config import CustomComplianceConfigAPI
from .download_file import DownloadFileAPI
from .events import EventsAPI
from .integrations import IntegrationsAPI
from .run_reports import RunReportsAPI
from .schemas import SchemasAPI
from .token import TokenAPI
from .vulnerability import VulnerabilityAPI

from laceworksdk.config import (
    LACEWORK_ACCOUNT_ENVIRONMENT_VARIABLE,
    LACEWORK_SUBACCOUNT_ENVIRONMENT_VARIABLE,
    LACEWORK_API_KEY_ENVIRONMENT_VARIABLE,
    LACEWORK_API_SECRET_ENVIRONMENT_VARIABLE,
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
                 instance=None):
        """
        Initializes the Lacework Client object.

        :return LaceworkClient object.
        """

        # Attempt to use Environment Variables
        self._account = account or instance or os.getenv(LACEWORK_ACCOUNT_ENVIRONMENT_VARIABLE)
        self._subaccount = subaccount or os.getenv(LACEWORK_SUBACCOUNT_ENVIRONMENT_VARIABLE)
        self._api_key = api_key or os.getenv(LACEWORK_API_KEY_ENVIRONMENT_VARIABLE)
        self._api_secret = api_secret or os.getenv(LACEWORK_API_SECRET_ENVIRONMENT_VARIABLE)

        # Create an HttpSession instance
        self._session = HttpSession(
            self._account,
            self._subaccount,
            self._api_key,
            self._api_secret
        )

        # API Wrappers
        self.alert_channels = AlertChannelsAPI(self._session)
        self.audit_logs = AuditLogsAPI(self._session)
        self.cloudtrail = CloudTrailAPI(self._session)
        self.compliance = ComplianceAPI(self._session)
        self.compliance.config = CustomComplianceConfigAPI(self._session)
        self.events = EventsAPI(self._session)
        self.files = DownloadFileAPI(self._session)
        self.integrations = IntegrationsAPI(self._session)
        self.run_reports = RunReportsAPI(self._session)
        self.schemas = SchemasAPI(self._session)
        self.tokens = TokenAPI(self._session)
        self.vulnerabilities = VulnerabilityAPI(self._session)
