# -*- coding: utf-8 -*-
"""
Lacework Entities API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class EntitiesAPI:
    """A class used to represent the Entities API endpoint.

    The Entities API endpoint is simply a parent for different types of
    entities that can be queried.

    Attributes
    ----------
    applications:
        A ApplicationsAPI instance.
    command_lines:
        A CommandLinesAPI instance.
    containers:
        A ContainersAPI instance.
    files:
        A FilesAPI instance.
    images:
        A ImagesAPI instance.
    internal_ip_addresses:
        A InternalIPAddressesAPI instance.
    k8s_pods:
        A K8sPodsAPI instance.
    machines:
        A MachinesAPI instance.
    machine_details:
        A MachineDetailsAPI instance.
    network_interfaces:
        A NetworkInterfacesAPI instance.
    new_file_hashes:
        A NewFileHashesAPI instance.
    packages:
        A PackagesAPI instance.
    processes:
        A ProcessesAPI instance.
    users:
        A UsersAPI instance.
    """

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
    """A class used to represent the Applications API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Applications objects.
    """
    RESOURCE = "Applications"


class CommandLinesAPI(SearchEndpoint):
    """A class used to represent the Command Lines API endpoint.

    Methods
    -------
    search(json=None)
        A method to search CommandLines objects.
    """
    RESOURCE = "CommandLines"


class ContainersAPI(SearchEndpoint):
    """A class used to represent the Containers API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Containers objects.
    """
    RESOURCE = "Containers"


class FilesAPI(SearchEndpoint):
    """A class used to represent the Files API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Files objects.
    """
    RESOURCE = "Files"


class ImagesAPI(SearchEndpoint):
    """A class used to represent the Images API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Images objects.
    """
    RESOURCE = "Images"


class InternalIPAddressesAPI(SearchEndpoint):
    """A class used to represent the Internal IP Addresses API endpoint.

    Methods
    -------
    search(json=None)
        A method to search InternalIPAddresses objects.
    """
    RESOURCE = "InternalIPAddresses"


class K8sPodsAPI(SearchEndpoint):
    """A class used to represent the K8s Pods API endpoint.

    Methods
    -------
    search(json=None)
        A method to search K8sPods objects.
    """
    RESOURCE = "K8sPods"


class MachinesAPI(SearchEndpoint):
    """A class used to represent the Machines API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Machines objects.
    """
    RESOURCE = "Machines"


class MachineDetailsAPI(SearchEndpoint):
    """A class used to represent the Machine Details API endpoint.

    Methods
    -------
    search(json=None)
        A method to search MachineDetails objects.
    """
    RESOURCE = "MachineDetails"


class NetworkInterfacesAPI(SearchEndpoint):
    """A class used to represent the Network Interfaces API endpoint.

    Methods
    -------
    search(json=None)
        A method to search NetworkInterfaces objects.
    """
    RESOURCE = "NetworkInterfaces"


class NewFileHashesAPI(SearchEndpoint):
    """A class used to represent the New File Hashes API endpoint.

    Methods
    -------
    search(json=None)
        A method to search NewFileHashes objects.
    """
    RESOURCE = "NewFileHashes"


class PackagesAPI(SearchEndpoint):
    """A class used to represent the Packages API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Packages objects.
    """
    RESOURCE = "Packages"


class ProcessesAPI(SearchEndpoint):
    """A class used to represent the Processes API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Processes objects.
    """
    RESOURCE = "Processes"


class UsersAPI(SearchEndpoint):
    """A class used to represent the Users API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Users objects.
    """
    RESOURCE = "Users"
