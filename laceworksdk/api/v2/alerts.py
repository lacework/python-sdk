# -*- coding: utf-8 -*-
"""Lacework Alerts API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class AlertsAPI(SearchEndpoint):
    """A class used to represent the `Alerts API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Alerts>`_

    Lacework provides real-time alerts that are interactive and manageable. Each alert contains various metadata
    information, such as severity level, type, status, alert category, and associated tags.
    """

    def __init__(self, session):
        """Initializes the AlertsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            AlertsAPI: An instance of the AlertsAPI class.
        """
        super().__init__(session, "Alerts")

    def get(self, start_time=None, end_time=None, limit=None, **request_params):
        """A method to get Alerts.

        Args:
          start_time (str): A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from.
          end_time (str): A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at.
          limit (int): An integer representing the number of Alerts to return.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
          dict: The requested alert(s)

        """
        params = self._build_dict_from_items(
            request_params, start_time=start_time, end_time=end_time
        )

        response = self._session.get(self._build_url(), params=params)

        return_data = {"data": []}
        current_rows = 0

        while True:
            response_json = response.json()

            return_data["paging"] = response_json["paging"]

            if limit:
                take = limit - current_rows
                return_data["data"].extend(response_json["data"][:take])
            else:
                return_data["data"].extend(response_json["data"])
            current_rows = len(return_data["data"])

            if limit and current_rows >= limit:
                break

            try:
                next_page = (
                    response_json.get("paging", {}).get("urls", {}).get("nextPage")
                )
            except Exception:
                next_page = None

            if next_page:
                response = self._session.get(next_page, params=params)
            else:
                break

        return return_data

    def get_details(self, id, scope, **request_params):
        """A method to get Alerts objects by ID.

        Args:
          id (str): The alert ID.
          scope (str): The scope of the details to return. Valid values are: "Details", "Investigation", "Events", "RelatedAlerts", "Integrations", "Timeline"
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The requested alert details.
        """
        params = self._build_dict_from_items(request_params, scope=scope)

        response = self._session.get(self._build_url(id=id), params=params)

        return response.json()

    def comment(self, id, comment):
        """A method to comment on an Alerts object.

        Args:
          id (str): The alert ID.
          comment (str): The comment to post.

        Returns:
            dict: The posted comment

        """
        json = self._build_dict_from_items(comment=comment)

        response = self._session.post(
            self._build_url(resource=id, action="comment"), json=json
        )

        return response.json()

    def close(self, id, reason, comment=None):
        """A method to close an Alert.

        Args:
          id (str): The alert ID.
          comment (str, option): A comment on the reason. If 0 is chosen for the "reason" field then the "comment" field is required.
          reason (int): An number representing the close reason. Valid values are: 0: Other, 1: False positive, 2: Not enough information, 3: Malicious and have resolution in place, 4: Expected because of routine testing

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        json = self._build_dict_from_items(reason=reason, comment=comment)

        response = self._session.post(
            self._build_url(resource=id, action="close"), json=json
        )

        return response.json()
