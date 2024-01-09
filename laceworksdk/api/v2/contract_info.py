# -*- coding: utf-8 -*-
"""Lacework ContractInfo API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class ContractInfoAPI(BaseEndpoint):
    """A class used to represent the `Contract Info API endpoint <https://docs.lacework.net/api/v2/docs/#tag/ContractInfo>`_

    Get Lacework contract information.
    """

    def __init__(self, session):
        """Initializes the ContractInfoAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            ContractInfoAPI: An instance of this class.

        """
        super().__init__(session, "ContractInfo")

    def get(self, **request_params):
        """A method to get contract info

        Returns:
            dict: Contract info for the lacework instance.
            request_params (dict, optional): Use to pass any additional parameters the API

        """
        params = self._build_dict_from_items(request_params)

        response = self._session.get(self._build_url(), params=params)

        return response.json()
