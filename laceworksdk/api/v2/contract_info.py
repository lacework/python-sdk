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
            start_time=None,
            end_time=None,
            **request_params):
        """
        A method to get ContractInfo objects.

        :param start_time: A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time
        )

        response = self._session.get(self.build_url(), params=params)

        return response.json()
