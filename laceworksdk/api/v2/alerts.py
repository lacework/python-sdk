# -*- coding: utf-8 -*-
"""Lacework Alerts API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class AlertsAPI(SearchEndpoint):

    def __init__(self, session):
        """Initializes the AlertsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return AlertsAPI object.

        Returns:

        """
        super().__init__(session, "Alerts")

    def get(self,
            start_time=None,
            end_time=None,
            limit=None,
            **request_params):
        """A method to get Alerts objects.

        Args:
          start_time: A "%Y-%m-%dT%H:%M:%SZ" structured timestamp to begin from. (Default value = None)
          end_time: A "%Y-%m-%dT%H:%M:%S%Z" structured timestamp to end at. (Default value = None)
          limit: An integer representing the number of Alerts to return. (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
          **request_params: 

        Returns:
          response json

        """
        params = self.build_dict_from_items(
            request_params,
            start_time=start_time,
            end_time=end_time
        )

        response = self._session.get(self.build_url(), params=params)

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
                next_page = response_json.get("paging", {}).get("urls", {}).get("nextPage")
            except Exception:
                next_page = None

            if next_page:
                response = self._session.get(next_page, params=params)
            else:
                break

        return return_data

    def get_details(self,
                    id,
                    scope,
                    **request_params):
        """A method to get Alerts objects by ID.

        Args:
          id: A string representing the object ID.
          scope: A string representing the scope of the detailst to return.
        ("Details", "Investigation", "Events", "RelatedAlerts", "Integrations", "Timeline")
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

        """
        params = self.build_dict_from_items(
            request_params,
            scope=scope
        )

        response = self._session.get(self.build_url(id=id), params=params)

        return response.json()

    def search(self,
               json=None):
        """A method to search Alerts objects.

        Args:
          json: A dictionary containing the necessary search parameters.
        (timeFilter, filters, returns)
        
        :return response json (Default value = None)

        Returns:

        """
        return super().search(json=json)

    def comment(self,
                id,
                comment):
        """A method to comment on an Alerts object.

        Args:
          id: A string representing the object ID.
          comment: A string representing the comment to post.
        
        :return response json

        Returns:

        """
        json = self.build_dict_from_items(
            comment=comment
        )

        response = self._session.post(self.build_url(resource=id, action="comment"), json=json)

        return response.json()

    def close(self,
              id,
              reason,
              comment=None):
        """A method to close an Alerts object.

        Args:
          id: A string representing the object ID.
          reason: An integer representing the close reason.
        0: Other
        1: False positive
        2: Not enough information
        3: Malicious and have resolution in place
        4: Expected because of routine testing
          comment: A string representing the comment to post.
        
        :return response json (Default value = None)

        Returns:

        """
        json = self.build_dict_from_items(
            reason=reason,
            comment=comment
        )

        response = self._session.post(self.build_url(resource=id, action="close"), json=json)

        return response.json()
