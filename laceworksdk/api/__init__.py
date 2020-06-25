# -*- coding: utf-8 -*-
"""
Lacework API wrappers.
"""

from laceworksdk.http_session import HttpSession
from .compliance import ComplianceAPI
from .custom_compliance_config import CustomComplianceConfigAPI
from .download_file import DownloadFileAPI
from .events import EventsAPI
from .integrations import IntegrationsAPI
from .run_reports import RunReportsAPI
from .token import TokenAPI
from .vulnerability import VulnerabilityAPI


class LaceworkClient(object):
    """
    Lacework API wrapper for Python.
    """

    def __init__(self,
                 api_key=None,
                 api_secret=None,
                 instance=None):
        """
        Initializes the Lacework Client object.

        :return LaceworkClient object.
        """

        # Set object params
        self._api_key = api_key
        self._api_secret = api_secret
        self._instance = instance

        # Create an HttpSession instance
        self._session = HttpSession(
            self._api_key,
            self._api_secret,
            self._instance
        )

        # API Wrappers
        self.compliance = ComplianceAPI(self._session)
        self.compliance.config = CustomComplianceConfigAPI(self._session)
        self.events = EventsAPI(self._session)
        self.files = DownloadFileAPI(self._session)
        self.integrations = IntegrationsAPI(self._session)
        self.run_reports = RunReportsAPI(self._session)
        self.tokens = TokenAPI(self._session)
        self.vulnerabilties = VulnerabilityAPI(self._session)
