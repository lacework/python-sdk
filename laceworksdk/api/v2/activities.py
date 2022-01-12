# -*- coding: utf-8 -*-
"""
Lacework Activities API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class ActivitiesAPI:

    def __init__(self, session):
        """
        Initializes the ActivitiesAPI object.

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

    def __init__(self, session, base_path):
        """
        Initializes the ChangedFilesAPI object.

        :param session: An instance of the HttpSession class

        :return ChangedFilesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Changed Files objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="ChangedFiles", json=json)


class ConnectionsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ConnectionsAPI object.

        :param session: An instance of the HttpSession class

        :return ConnectionsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Connections objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Connections", json=json)


class DnsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the DnsAPI object.

        :param session: An instance of the HttpSession class

        :return DnsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search DNS lookup objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="DNSs", json=json)


class UserLoginsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the UserLoginsAPI object.

        :param session: An instance of the HttpSession class

        :return UserLoginsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search User Logins objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="UserLogins", json=json)
