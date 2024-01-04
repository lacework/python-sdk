# -*- coding: utf-8 -*-
"""Lacework CloudActivities API wrapper."""

from laceworksdk.api.base_endpoint import BaseEndpoint


class CloudActivitiesAPI(BaseEndpoint):
    """A class used to represent the `Cloud Activities API endpoint <https://docs.lacework.net/api/v2/docs/#tag/CloudActivities>`_

    Get information about cloud activities for the integrated AWS cloud accounts in your Lacework instance.
    """
    def __init__(self, session):
        """Initializes the CloudActivitiesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            CloudActivitiesAPI: An instance of this class

        """
        super().__init__(session, "CloudActivities")

    def get(self,
            start_time=None,
            end_time=None,
            **request_params):
        """A method to get cloud activities objects.

        Args:
          start_time (str): A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
          end_time (str): A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.

        Returns:
            dict: The requested cloud activity data.

        """
        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time
        )

        response = self._session.get(self.build_url(), params=params)

        return response.json()

    def get_pages(self,
                  start_time=None,
                  end_time=None,
                  **request_params):
        """A helper method that yields a generator which allows you to iterate through the resulting pages of \
        activities. Call this instead of the "get" method if you don't want to write your own code to get the paginated\
        results.

        Args:
          start_time (str): A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
          end_time (str): A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.

        Yields:
            dict: a generator which yields a dict of cloud activities.
        """
        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time
        )

        for page in self._session.get_pages(self.build_url(), params=params):
            yield page.json()

    def get_data_items(self,
                       start_time=None,
                       end_time=None,
                       **request_params):
        """A helper method that yields a generator which allows you to iterate through the resulting pages of \
        activities. Call this instead of the "get" method if you don't want to write your own code to get the paginated\
        results.

        Args:
          start_time (str): A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
          end_time (str): A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.

        Yields:
            dict: a generator which yields multipe dicts of cloud activities.
        """
        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time,
        )

        for item in self._session.get_data_items(self.build_url(), params=params):
            yield item

    def search(self,
               json=None):
        """A method to search cloud activities.

       Args:
          json (list of dicts): A list of dictionaries containing the desired search parameters: \n
            - field (str): The name of the data field to which the condition applies\n
            - expression (str): The comparison operator for the filter condition. Valid values are:\n
                - "eq"\n
                - "ne"\n
                - "in"\n
                - "not_in"\n
                - "like"\n
                - "ilike"\n
                - "not_like"\n
                - "not_ilike"\n
                - "not_rlike"\n
                - "rlike"\n
                - "gt"\n
                - "ge"\n
                - "lt"\n
                - "le"\n
                - "between"\n
            - value (str, optional):  The value that the condition checks for in the specified field. Use this attribute
             when using an operator that requires a single value.\n
            - values (list of str, optional): The values that the condition checks for in the specified field. Use this
            attribute when using an operator that requires multiple values.\n

        Yields:
            dict: returns a generator which yields a page of objects at a time as returned by the Lacework API.
        """

        response = self._session.post(self.build_url(action="search"), json=json)
        return response.json()
