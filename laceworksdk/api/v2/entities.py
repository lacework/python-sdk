# -*- coding: utf-8 -*-
"""
Lacework Entities API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class EntitiesAPI:

    def __init__(self, session):
        """
        Initializes the EntitiesAPI object.

        :param session: An instance of the HttpSession class

        :return EntitiesAPI object.
        """

        super().__init__()
        self._base_path = "Entities"

        self.applications = ApplicationsAPI(session, self._base_path)
        self.command_lines = CommandLinesAPI(session, self._base_path)
        self.containers = ContainersAPI(session, self._base_path)
        self.files = FilesAPI(session, self._base_path)
        self.images = ImagesAPI(session, self._base_path)
        self.internal_ip_addresses = InternalIPAddressesAPI(session, self._base_path)
        self.k8s_pods = K8sPodsAPI(session, self._base_path)
        self.machines = MachinesAPI(session, self._base_path)
        self.machine_details = MachineDetailsAPI(session, self._base_path)
        self.network_interfaces = NetworkInterfacesAPI(session, self._base_path)
        self.new_file_hashes = NewFileHashesAPI(session, self._base_path)
        self.packages = PackagesAPI(session, self._base_path)
        self.processes = ProcessesAPI(session, self._base_path)
        self.users = UsersAPI(session, self._base_path)


class ApplicationsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ApplicationsAPI object.

        :param session: An instance of the HttpSession class

        :return ApplicationsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Applications objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Applications", json=json)


class CommandLinesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the CommandLinesAPI object.

        :param session: An instance of the HttpSession class

        :return CommandLinesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search CommandLines objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="CommandLines", json=json)


class ContainersAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ContainersAPI object.

        :param session: An instance of the HttpSession class

        :return ContainersAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Containers objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Containers", json=json)


class FilesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the FilesAPI object.

        :param session: An instance of the HttpSession class

        :return FilesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Files objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Files", json=json)


class ImagesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ImagesAPI object.

        :param session: An instance of the HttpSession class

        :return ImagesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Images objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Images", json=json)


class InternalIPAddressesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the InternalIPAddressesAPI object.

        :param session: An instance of the HttpSession class

        :return InternalIPAddressesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search InternalIPAddresses objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="InternalIPAddresses", json=json)


class K8sPodsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the K8sPodsAPI object.

        :param session: An instance of the HttpSession class

        :return K8sPodsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search K8sPods objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="K8sPods", json=json)


class MachinesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the MachinesAPI object.

        :param session: An instance of the HttpSession class

        :return MachinesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Machines objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Machines", json=json)


class MachineDetailsAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the MachineDetailsAPI object.

        :param session: An instance of the HttpSession class

        :return MachineDetailsAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search MachineDetails objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="MachineDetails", json=json)


class NetworkInterfacesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the NetworkInterfacesAPI object.

        :param session: An instance of the HttpSession class

        :return NetworkInterfacesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search NetworkInterfaces objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="NetworkInterfaces", json=json)


class NewFileHashesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the NewFileHashesAPI object.

        :param session: An instance of the HttpSession class

        :return NewFileHashesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search NewFileHashes objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="NewFileHashes", json=json)


class PackagesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the PackagesAPI object.

        :param session: An instance of the HttpSession class

        :return PackagesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Packages objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Packages", json=json)


class ProcessesAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the ProcessesAPI object.

        :param session: An instance of the HttpSession class

        :return ProcessesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Processes objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Processes", json=json)


class UsersAPI(SearchEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the UsersAPI object.

        :param session: An instance of the HttpSession class

        :return UsersAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Users objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Users", json=json)
