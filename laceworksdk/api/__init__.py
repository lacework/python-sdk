# -*- coding: utf-8 -*-
"""
Lacework API wrappers.
"""

from laceworksdk.http_session import HttpSession
from .compliance import ComplianceAPI
from .download_file import DownloadFileAPI
from .events import EventsAPI
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
        self.events = EventsAPI(self._session)
        self.files = DownloadFileAPI(self._session)
        self.tokens = TokenAPI(self._session)
        self.vulnerabilties = VulnerabilityAPI(self._session)
