# -*- coding: utf-8 -*-
"""
Lacework Alerts API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class AlertsAPI(SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the AlertsAPI object.

        :param session: An instance of the HttpSession class

        :return AlertsAPI object.
        """

        super().__init__(session, "Alerts")

    def get(self,
            start_time=None,
            end_time=None,
            **request_params):
        """
        A method to get Alerts objects.

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

    def get_details(self,
                    id,
                    **request_params):
        """
        A method to get Alerts objects by ID.

        :param id: A string representing the object ID.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            request_params
        )

        response = self._session.get(self.build_url(id=id), params=params)

        return response.json()

    def search(self,
               json=None):
        """
        A method to search Alerts objects.

        :param json: A dictionary containing the necessary search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        return super().search(json=json)
