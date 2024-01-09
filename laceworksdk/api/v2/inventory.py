# -*- coding: utf-8 -*-
"""Lacework Inventory API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class InventoryAPI(SearchEndpoint):
    """A class used to represent the `Inventory API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Inventory>`_

    View and monitor in-use cloud resources' risk, compliance, and configuration changes.
    """

    def __init__(self, session):
        """Initializes the Inventory API object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            InventoryAPI: An instance of this class.

        """
        super().__init__(session, "Inventory")

    def scan(self, csp):
        """A method to trigger a resource inventory scan.

        Args:
          csp (string): The cloud service provider to run the scan on. Valid values are: "AWS" "Azure" "GCP"

        Returns:
            dict: Status of scan

        """
        params = self._build_dict_from_items(csp=csp)

        response = self._session.post(self._build_url(action="scan"), params=params)

        return response.json()

    def status(self, csp):
        """A method to get the status of a Resource Inventory scan.

        Args:
          csp (string): The cloud service provider to run the scan on. Valid values are: "AWS" "Azure" "GCP"

        Returns:
            dict: Status of scan

        """
        params = self._build_dict_from_items(csp=csp)

        response = self._session.get(self._build_url(action="scan"), params=params)

        return response.json()
