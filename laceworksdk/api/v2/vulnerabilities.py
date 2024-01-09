# -*- coding: utf-8 -*-
"""Lacework Vulnerabilities API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint
from laceworksdk.api.search_endpoint import SearchEndpoint


class VulnerabilitiesAPI:
    """A class used to represent the `Vulnerabilities API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Vulnerabilities>`_ .

    The Vulnerabilities API endpoint is a parent for different types of
    vulnerabilities that can be queried.  Due to namespace overlap with the v1
    API, this class is a subclass of VulnerabilityAPI to expose those methods
    and provide backwards compatibility.

    Attributes:
    ----------
    containers:
        A ContainerVulnerabilitiesAPI instance.
    hosts:
        A HostVulnerabilitiesAPI instance.
    packages:
        A SoftwarePackagesAPI instance.

    """

    def __init__(self, session):
        """Initializes the VulnerabilitiesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            VulnerabilitiesAPI: An instance of this class

        """

        super().__init__()

        self._base_path = "Vulnerabilities"

        self.containers = self.ContainerVulnerabilitiesAPI(session, self._base_path)
        self.hosts = self.HostVulnerabilitiesAPI(session, self._base_path)
        self.packages = self.SoftwarePackagesAPI(session, self._base_path)

    class ContainerVulnerabilitiesAPI(SearchEndpoint):
        """A class used to represent the Container Vulnerabilities API endpoint."""

        RESOURCE = "Containers"

        def scan(self, registry, repository, tag, **request_params):
            """A method to issue Container Vulnerability scans.

            Args:
              registry (str): The container registry to use.
              repository (str): The container repository to use.
              tag (str): The container tag to use.
              request_params (dict, optional): Use to pass any additional parameters the API

            Returns:
                dict: The status of the requested scan
            """

            json = self._build_dict_from_items(
                **request_params, registry=registry, repository=repository, tag=tag
            )

            response = self._session.post(
                self._build_url(resource="Containers", action="scan"), json=json
            )

            return response.json()

        def status(self, request_id):
            """A method to get the status of a Container Vulnerability scan.

            Args:
              request_id (str): The request ID of the container scan

            Returns:
                dict: The status of the requested scan
            """
            if request_id is None or len(request_id) == 0:
                raise ValueError(
                    "The value 'request_id' must be a valid container scan request ID."
                )

            response = self._session.get(
                self._build_url(id=request_id, resource="Containers", action="scan")
            )

            return response.json()

    class HostVulnerabilitiesAPI(SearchEndpoint):
        """A class used to represent the Host Vulnerabilities API endpoint."""

        RESOURCE = "Hosts"

    class SoftwarePackagesAPI(BaseEndpoint):
        """A class used to represent the Software Packages API endpoint."""

        def scan(self, os_pkg_info_list, **request_params):
            """A method to initiate a software package vulnerability scan.

            Args:
              os_pkg_info_list (list of dict): A list of packages to be scanned given the OS, OS version, package, and \
              package version. Fields are:\n

                  - os (str): The name of the operating system.
                  - osVer (str): The version of the operating system.
                  - pkg (str): The name of the software package.
                  - pkgVer (str): The verion of the software package.

              request_params (dict, optional): Use to pass any additional parameters the API

            Returns:
                dict: The resulting vulnerability data

            """

            json = self._build_dict_from_items(
                **request_params, os_pkg_info_list=os_pkg_info_list
            )

            response = self._session.post(
                self._build_url(resource="SoftwarePackages", action="scan"), json=json
            )

            return response.json()
