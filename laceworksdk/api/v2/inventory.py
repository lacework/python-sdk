# -*- coding: utf-8 -*-
"""
Lacework Inventory API wrapper.
"""

from laceworksdk.api.search_endpoint import SearchEndpoint


class InventoryAPI(SearchEndpoint):

    def __init__(self, session):
        """
        Initializes the Evidence API object.

        :param session: An instance of the HttpSession class

        :return EvidenceAPI object.
        """

        super().__init__(session, "Inventory")
