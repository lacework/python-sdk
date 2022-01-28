# -*- coding: utf-8 -*-
"""
Lacework ContractInfo API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class ContractInfoAPI(BaseEndpoint):

    def __init__(self, session):
        """
        Initializes the ContractInfoAPI object.

        :param session: An instance of the HttpSession class

        :return ContractInfoAPI object.
        """

        super().__init__(session, "ContractInfo")

    def get(self,
            **request_params):
        """
        A method to get ContractInfo objects.

        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            request_params
        )

        response = self._session.get(self.build_url(), params=params)

        return response.json()
