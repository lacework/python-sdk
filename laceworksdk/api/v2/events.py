# -*- coding: utf-8 -*-
"""
Lacework Events API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint
from laceworksdk.api.v1.events import EventsAPIv1


class EventsAPIv2(EventsAPIv1, SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the EventsAPI object.

        :param session: An instance of the HttpSession class

        :return EventsAPI object.
        """

        # The need to pass "Events" into the v1 init() is tied
        # to the super() call within the v1 init()
        super(EventsAPIv1, self).__init__(session, "Events")
        super(SearchEndpoint, self).__init__(session, "Events")
