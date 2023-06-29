# -*- coding: utf-8 -*-
"""
Lacework Events API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class EventsAPI(SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the EventsAPI object.

        :param session: An instance of the HttpSession class

        :return EventsAPI object.
        """
        super().__init__(session, "Events")

    def get(self,
            event_id=None,
            start_time=None,
            end_time=None,
            limit=None,
            **request_params):
        """
        A method to get Event details

        :param event_id: An integer representing the Event ID to retrieve.
        :param start_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to end at.
        :param limit: An integer representing the number of Alerts to return.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """
        params = self.build_dict_from_items(
            request_params,
            id=event_id,
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
                    event_id,
                    **request_params):
        """
        A method to get the Event Details for the specified Event ID.

        :param event_id: An integer representing the Event ID to retrieve.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            request_params,
        )

        response = self._session.get(self.build_url(id=event_id), params=params)

        return response.json()
