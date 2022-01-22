# -*- coding: utf-8 -*-
"""
Lacework Activities API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class ActivitiesAPI:
    """A class used to represent the Activities API endpoint.

    The Activities API endpoint is simply a parent for different types of
    activities that can be queried.

    Attributes
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

        :param session: An instance of the HttpSession class

        :return ActivitiesAPI object.
        """

        super().__init__()
        self._base_path = "Activities"

        self.changed_files = ChangedFilesAPI(session, self._base_path)
        self.connections = ConnectionsAPI(session, self._base_path)
        self.dns = DnsAPI(session, self._base_path)
        self.user_logins = UserLoginsAPI(session, self._base_path)


class ChangedFilesAPI(SearchEndpoint):
    """A class used to represent the Changed Files API endpoint.

    Methods
    -------
    search(json=None)
        A method to search ChangedFiles objects.
    """
    RESOURCE = "ChangedFiles"


class ConnectionsAPI(SearchEndpoint):
    """A class used to represent the Connections API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Connections objects.
    """
    RESOURCE = "Connections"


class DnsAPI(SearchEndpoint):
    """A class used to represent the DNS Lookup API endpoint.

    Methods
    -------
    search(json=None)
        A method to search DNS lookup objects.
    """
    RESOURCE = "DNSs"


class UserLoginsAPI(SearchEndpoint):
    """A class used to represent the UserLogins API endpoint.

    Methods
    -------
    search(json=None)
        A method to search UserLogins objects.
    """
    RESOURCE = "UserLogins"
