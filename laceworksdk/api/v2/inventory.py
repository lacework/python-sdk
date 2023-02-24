# -*- coding: utf-8 -*-
"""
Lacework Inventory API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class InventoryAPI(SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the Inventory API object.

        :param session: An instance of the HttpSession class

        :return InventoryAPI object.
        """

        super().__init__(session, "Inventory")

    def scan(self,
             csp,
             **request_params):
        """
        A method to issue Resource Inventory scans.

        :param csp: A string representing the cloud service provider to run the scan on (i.e. AWS, Azure, GCP).
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            csp=csp
        )

        response = self._session.post(self.build_url(action="scan"), params=params)

        return response.json()

    def status(self,
               csp):
        """
        A method to get the status of a Resource Inventory scan.

        :param csp: A string representing the cloud service provider retrieve the scan status from (i.e. AWS, Azure, GCP).

        :return response json
        """

        params = self.build_dict_from_items(
            csp=csp
        )

        response = self._session.get(self.build_url(action="scan"), params=params)

        return response.json()
