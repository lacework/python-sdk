# -*- coding: utf-8 -*-
"""
Lacework Vulnerabilities API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint
from laceworksdk.api.search_endpoint import SearchEndpoint
from laceworksdk.api.v1.vulnerability import VulnerabilityAPI


class VulnerabilitiesAPI(VulnerabilityAPI):
    """A class used to represent the Vulnerabilities API endpoint.

    The Vulnerabilities API endpoint is simply a parent for different types of
    vulnerabilities that can be queried.  Due to namespace overlap with the v1
    API, this class is a subclass of VulnerabilityAPI to expose those methods
    and provide backwards compatibility.

    Attributes
    ----------
    containers:
        A ContainerVulnerabilitiesAPI instance.
    hosts:
        A HostVulnerabilitiesAPI instance.
    packages:
        A SoftwarePackagesAPI instance.
    """

    def __init__(self, session):
        """
        Initializes the VulnerabilitiesAPI object.

        :param session: An instance of the HttpSession class

        :return VulnerabilitiesAPI object.
        """

        super().__init__(session)
        self._base_path = "Vulnerabilities"

        self.containers = ContainerVulnerabilitiesAPI(session, self._base_path)
        self.hosts = HostVulnerabilitiesAPI(session, self._base_path)
        self.packages = SoftwarePackagesAPI(session, self._base_path)


class ContainerVulnerabilitiesAPI(SearchEndpoint):
    """A class used to represent the Container Vulnerabilities API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Container Vulnerabilities objects.
    scan(registry, repository, tag, **request_params)
        A method to issue a Container Vulnerability scan.
    status(request_id)
        A method to get the status of a Container Vulnerability scan.
    """
    RESOURCE = "Containers"

    def scan(self,
             registry,
             repository,
             tag,
             **request_params):
        """
        A method to issue Container Vulnerability scans.

        :param registry: A string representing the container registry to use.
        :param repository: A string representing the container repository to use.
        :param tag: A string representing the container tag to use.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        json = self.build_dict_from_items(
            **request_params,
            registry=registry,
            repository=repository,
            tag=tag
        )

        response = self._session.post(self.build_url(resource="Containers", action="scan"), json=json)

        return response.json()

    def status(self,
               request_id):
        """
        A method to get the status of a Container Vulnerability scan.

        :param rquest_id: A string representing the request ID of the container scan.

        :return response json
        """

        if request_id is None or len(request_id) == 0:
            raise ValueError("The value 'request_id' must be a valid container scan request ID.")

        response = self._session.get(self.build_url(id=request_id, resource="Containers", action="scan"))

        return response.json()


class HostVulnerabilitiesAPI(SearchEndpoint):
    """A class used to represent the Host Vulnerabilities API endpoint.

    Methods
    -------
    search(json=None)
        A method to search Host Vulnerabilities objects.
    """
    RESOURCE = "Hosts"


class SoftwarePackagesAPI(BaseEndpoint):
    """A class used to represent the Software Packages API endpoint.

    Methods
    -------
    scan(os_pkg_info_list, **request_params)
        A method to initiate a Software Package vulnerability scan.
    """

    def scan(self,
             os_pkg_info_list,
             **request_params):
        """
        A method to initiate a software package vulnerability scan.

        :param os_pkg_info_list: A list of packages to be scanned given the OS, OS Version, Package, and Package Version.
            :obj
                :param os: A string representing the name of the operating system.
                :param osVer: A string representing the version of the operating system.
                :param pkg: A string representing the name of the software package.
                :param pkgVer: A string representing the verion of the software package.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return: response json
        """

        json = self.build_dict_from_items(
            **request_params,
            os_pkg_info_list=os_pkg_info_list
        )

        response = self._session.post(self.build_url(resource="SoftwarePackages", action="scan"), json=json)

        return response.json()
