# -*- coding: utf-8 -*-
"""
Lacework AlertChannels API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertChannelsAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the AlertChannelsAPI object.

        :param session: An instance of the HttpSession class

        :return AlertChannelsAPI object.
        """

        super().__init__(session, "AlertChannels")

    def create(self,
               name,
               type,
               enabled,
               data,
               **request_params):
        """
        A method to create a new AlertChannels object.

        :param name: A string representing the object name.
        :param type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            name=name,
            type=type,
            enabled=int(bool(enabled)),
            data=data,
            **request_params
        )

    def get(self,
            guid=None,
            type=None):
        """
        A method to get AlertChannels objects.

        :param guid: A string representing the object GUID.
        :param type: A string representing the object type.

        :return response json
        """

        return super().get(
            id=guid,
            resource=type
        )

    def get_by_guid(self,
                    guid):
        """
        A method to get AlertChannels objects by GUID.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return self.get(guid=guid)

    def get_by_type(self,
                    type):
        """
        A method to get AlertChannels objects by type.

        :param type: A string representing the object type.

        :return response json
        """

        return self.get(type=type)

    def update(self,
               guid,
               name=None,
               type=None,
               enabled=None,
               data=None,
               **request_params):
        """
        A method to update an AlertChannels object.

        :param guid: A string representing the object GUID.
        :param name: A string representing the object name.
        :param type: A string representing the object type.
        :param enabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param data: A JSON object matching the schema for the specified type.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid,
            name=name,
            type=type,
            enabled=enabled,
            data=data,
            **request_params
        )

    def delete(self,
               guid):
        """
        A method to delete an AlertChannels object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)

    def test(self,
             guid):
        """
        A method to test an AlertChannels object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        response = self._session.post(self.build_url(resource=guid, action="test"))

        return response
