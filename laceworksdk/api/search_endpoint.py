# -*- coding: utf-8 -*-

from laceworksdk.api.base_endpoint import BaseEndpoint


class SearchEndpoint(BaseEndpoint):

    def __init__(self,
                 session,
                 object_type,
                 endpoint_root="/api/v2"):
        """
        :param session: An instance of the HttpSession class.
        :param object_type: The Lacework object type to use.
        :param endpoint_root: The URL endpoint root to use.
        """

        super().__init__(session, object_type, endpoint_root)

    def search(self, json=None, resource=None, **kwargs):
        """
        A method to search objects.

        :param json: A dictionary containing the desired search parameters.
            (timeFilter, filters, returns)

        :return a generator which yields a page of objects at a time as returned by the Lacework API.
        """

        response = self._session.post(self.build_url(resource=resource, action="search"), json=json)

        while True:
            response_json = response.json()
            yield response_json

            try:
                next_page = response_json.get("paging", {}).get("urls", {}).get("nextPage")
            except Exception:
                next_page = None

            if next_page:
                response = self._session.get(next_page, **kwargs)
            else:
                break
