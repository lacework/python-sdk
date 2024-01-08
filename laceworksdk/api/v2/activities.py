# -*- coding: utf-8 -*-
"""Lacework Activities API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class ActivitiesAPI:
    """A class used to represent the `Activities API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Activities>`_

    Get information about network activities detected through the Lacework agent.

    The Activities API endpoint is a parent for different types of
    activities that can be queried.

    Attributes:
    ----------
    changed_files:
        A ChangedFilesAPI instance.
    connections:
        A ConnectionsAPI instance.
    dns:
        A DnsAPI instance.
    user_logins:
        A UserLoginsAPI instance.

    """

    def __init__(self, session):
        """Initializes the ActivitiesAPI object.

        Args:
            session(HttpSession): An instance of the HttpSession class

        Return:
            ActivitiesAPI object.
        """
        super().__init__()
        self._base_path = "Activities"

        self.changed_files = self.ChangedFilesAPI(session, self._base_path)
        self.connections = self.ConnectionsAPI(session, self._base_path)
        self.dns = self.DnsAPI(session, self._base_path)
        self.user_logins = self.UserLoginsAPI(session, self._base_path)

    class ChangedFilesAPI(SearchEndpoint):
        """A class used to represent the `Changed Files API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Activities/paths/~1api~1v2~1Activities~1ChangedFiles~1search/post>`_

        Search for changed files in your environment
        """

        RESOURCE = "ChangedFiles"

    class ConnectionsAPI(SearchEndpoint):
        """A class used to represent the `Connections API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Activities/paths/~1api~1v2~1Activities~1Connections~1search/post>`_

        Search for connections in your environment.
        """

        RESOURCE = "Connections"

    class DnsAPI(SearchEndpoint):
        """A class used to represent the `DNS Lookup API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Activities/paths/~1api~1v2~1Activities~1DNSs~1search/post>`_

        Search for DNS summaries in your environment.
        """

        RESOURCE = "DNSs"

    class UserLoginsAPI(SearchEndpoint):
        """A class used to represent the `UserLogins API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Activities/paths/~1api~1v2~1Activities~1UserLogins~1search/post>`_

        Search for user logins in your environment.
        """

        RESOURCE = "UserLogins"
