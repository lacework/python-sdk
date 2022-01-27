# -*- coding: utf-8 -*-
"""
Lacework CloudActivities API wrapper.
"""

from laceworksdk.api.base_endpoint import BaseEndpoint


class CloudActivitiesAPI(BaseEndpoint):

    def __init__(self, session):
        """
        Initializes the CloudActivitiesAPI object.

        :param session: An instance of the HttpSession class

        :return CloudActivitiesAPI object.
        """

        super().__init__(session, "CloudActivities")

    def get(self,
            start_time=None,
            end_time=None,
            **request_params):
        """
        A method to get CloudActivities objects.

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

    def get_pages(self,
                  **request_params):
        """
        A method to get pages of objects objects.

        :param request_params: request parameters.

        :return a generator which yields pages of CloudActivities objects returned by the Lacework API.
        """

        params = self.build_dict_from_items(
            request_params
        )

        for page in self._session.get_pages(self.build_url(), params=params):
            yield page.json()

    def get_data_items(self,
                       **request_params):
        """
        A method to get data items.

        :param request_params: request parameters.

        :return a generator which yields individual CloudActivities objects returned by the Lacework API.
        """

        params = self.build_dict_from_items(
            request_params
        )

        for item in self._session.get_data_items(self.build_url(), params=params):
            yield item

    def search(self,
               json=None):
        """
        A method to search CloudActivities objects.

        :param json: A dictionary containing the necessary search parameters.
            (timeFilter, filters, returns)

        :return response json
        """

        response = self._session.post(self.build_url(action="search"), json=json)

        return response.json()
