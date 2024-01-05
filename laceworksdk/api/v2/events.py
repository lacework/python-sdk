# -*- coding: utf-8 -*-
"""Lacework Events API wrapper."""

from laceworksdk.api.search_endpoint import SearchEndpoint


class EventsAPI(SearchEndpoint):
    """A class used to represent the `Events API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Events>`_

    View and verify the evidence or observation details of individual events.
    """

    def __init__(self, session):
        """Initializes the EventsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            EventsAPI: An instance of this class

        """
        super().__init__(session, "Events")
