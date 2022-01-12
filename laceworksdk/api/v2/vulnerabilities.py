# -*- coding: utf-8 -*-
"""
Lacework Vulnerabilities API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint
from laceworksdk.api.search_endpoint import SearchEndpoint
from laceworksdk.api.v1.vulnerability import VulnerabilityAPI


class VulnerabilitiesAPI(VulnerabilityAPI):

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

    def __init__(self, session, base_path):
        """
        Initializes the ContainerVulnerabilitiesAPI object.

        :param session: An instance of the HttpSession class

        :return ContainerVulnerabilitiesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Container Vulnerabilities objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Containers", json=json)

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

    def __init__(self, session, base_path):
        """
        Initializes the HostVulnerabilitiesAPI object.

        :param session: An instance of the HttpSession class

        :return HostVulnerabilitiesAPI object.
        """

        super().__init__(session, base_path)

    def search(self,
               json=None):
        """
        A method to search Host Vulnerabilities objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(resource="Hosts", json=json)


class SoftwarePackagesAPI(BaseEndpoint):

    def __init__(self, session, base_path):
        """
        Initializes the SoftwarePackagesAPI object.

        :param session: An instance of the HttpSession class

        :return SoftwarePackagesAPI object.
        """

        super().__init__(session, base_path)

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
