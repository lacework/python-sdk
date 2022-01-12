# -*- coding: utf-8 -*-
"""
Lacework Events API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class EventsAPI:
    """
    Lacework Events API.
    """

    def __init__(self, session):
        """
        Initializes the EventsAPI object.

        :param session: An instance of the HttpSession class.

        :return EventsAPI object
        """

        super().__init__()

        self._session = session

    def get(self,
            id=None,
            start_time=None,
            end_time=None):
        """
        A method to get Event details

        :param event_id: An integer representing the Event ID to retrieve.
        :param start_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to end at.

        :return response json
        """

        logger.info("Getting Event information from Lacework...")

        # Build the Event request URI
        if id:
            api_uri = f"/api/v1/external/events/GetEventDetails?EVENT_ID={id}"
        elif start_time and end_time:
            api_uri = f"/api/v1/external/events/GetEventsForDateRange?START_TIME={start_time}&END_TIME={end_time}"
        else:
            logger.error("Either an Event ID or start/end times need to be provided to run queries on the Lacework Events API.")
            exit()

        response = self._session.get(api_uri)

        return response.json()

    def get_details(self,
                    event_id):
        """
        A method to get the Event Details for the specified Event ID.

        :param event_id: An integer representing the Event ID to retrieve.

        :return response json
        """

        logger.warning("The 'get_details' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get(id=event_id)

    def get_for_date_range(self,
                           start_time,
                           end_time):
        """
        A method to get Events for the specified time range.

        :param start_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to end at.

        :return response json
        """

        logger.warning("The 'get_for_date_range' function may be deprecated shortly, please consider switching to 'get'.")

        return self.get(start_time=start_time, end_time=end_time)
