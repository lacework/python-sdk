# -*- coding: utf-8 -*-
"""
Lacework Events API wrapper.
"""

import json
import logging

logger = logging.getLogger(__name__)


class EventsAPI(object):
    """
    Lacework Events API.
    """

    def __init__(self, session):
        """
        Initializes the EventsAPI object.

        :param session: An instance of the HttpSession class.

        :return EventsAPI object
        """

        super(EventsAPI, self).__init__()

        self._session = session

    def get_details(self, event_id):
        """
        A method to get the Event Details for the specified Event ID.

        :param event_id: An integer representing the Event ID to retrieve.

        :return response json
        """

        logger.info("Getting Event Details from Lacework...")

        # Build the Event Details request URI
        api_uri = f"/api/v1/external/events/GetEventDetails?EVENT_ID={event_id}"

        response = self._session.get(api_uri)

        return response.json()

    def get_for_date_range(self, start_time, end_time):
        """
        A method to get Events for the specified time range.

        :param start_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to begin from.
        :param end_time: A "%Y-%m-%dT%H:%M:%S%z" structured timestamp to end at.

        :return response json
        """

        logger.info("Getting Events within date range from Lacework...")

        # Build the Event Details request URI
        api_uri = f"/api/v1/external/events/GetEventsForDateRange?START_TIME={start_time}&END_TIME={end_time}"

        response = self._session.get(api_uri)

        return response.json()
