# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

from tests.api.test_base_endpoint import BaseEndpoint


class CrudEndpoint(BaseEndpoint):

    def test_api_get(self, api_object):
        response = api_object.get()

        assert "data" in response.keys()

    def test_api_create(self, api_object, api_object_create_body, request):
        response = api_object.create(**api_object_create_body)

        assert "data" in response.keys()
        self._check_object_values(api_object_create_body, response)

        request.config.cache.set(self.OBJECT_ID_NAME, response["data"][self.OBJECT_ID_NAME])

    def test_api_search(self, api_object, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)

        if guid is None:
            guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)

        assert guid is not None
        if guid:
            response = api_object.search(json={
                "filters": [
                    {
                        "expression": "eq",
                        "field": self.OBJECT_ID_NAME,
                        "value": guid
                    }
                ],
                "returns": [
                    self.OBJECT_ID_NAME
                ]
            })

            assert "data" in response.keys()
            assert len(response["data"]) == 1
            assert response["data"][0][self.OBJECT_ID_NAME] == guid

    def test_api_update(self, api_object, api_object_update_body, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)

        if guid is None:
            guid = self._get_random_object(api_object, self.OBJECT_ID_NAME)

        assert guid is not None
        if guid:
            response = api_object.update(guid, **api_object_update_body)

            assert "data" in response.keys()

            self._check_object_values(api_object_update_body, response)

    def test_api_delete(self, api_object, request):
        guid = request.config.cache.get(self.OBJECT_ID_NAME, None)
        assert guid is not None
        if guid:
            response = api_object.delete(guid)
            assert response.status_code == 204
