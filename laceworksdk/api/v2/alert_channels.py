# -*- coding: utf-8 -*-
"""Lacework AlertChannels API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertChannelsAPI(CrudEndpoint):
    """A class used to represent the `Alert Channels API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AlertChannels>`_

    Lacework combines alert channels with alert rules or report rules to provide a flexible method for routing alerts and reports.
    """

    def __init__(self, session):
        """Initializes the AlertChannelsAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            AlertChannelsAPI: an AlertChannelsAPI object.
        """
        super().__init__(session, "AlertChannels")

    def create(self, name, type, enabled, data, **request_params):
        """A method to create a new AlertChannels object.

        Args:
          name (str): The name of the alert channel you wish to create.
          type (str): The type of alert channel you wish to create. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertChannels/paths/~1api~1v2~1AlertChannels/post>`_ for valid values.
          enabled (bool|int): A boolean/integer representing whether the object is enabled. (0 or 1)
          data (dict): A dict matching the schema for the specified type. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertChannels/paths/~1api~1v2~1AlertChannels/post>`_ for valid values.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The new alert channel
        """
        return super().create(
            name=name,
            type=type,
            enabled=int(bool(enabled)),
            data=data,
            **request_params,
        )

    def get(self, guid=None, type=None):
        """A method to get all Alert Channels, optionally filtered by guid and/or type.

        Args:
            guid (str, optional): The alert channel GUID.
            type (str, optional): A string representing the alert channel type.

        Returns:
            dict: The channel(s) requested.

        """
        return super().get(id=guid, resource=type)

    def get_by_guid(self, guid):
        """A method to get AlertChannels objects by GUID.

        Args:
            guid (str): The alert channel GUID.

        Returns:
            dict: The channel(s) requested.
        """
        return self.get(guid=guid)

    def get_by_type(self, type):
        """A method to get AlertChannels objects by type.

        Args:
          type (str): The alert channel type to return

        Returns:
            dict: The channel(s) requested.
        """
        return self.get(type=type)

    def update(
        self, guid, name=None, type=None, enabled=None, data=None, **request_params
    ):
        """A method to update an AlertChannels object.

        Args:
            guid (str): The guild of the alert channel to update.
            name (str): The name of the alert channel you wish to update.
            type (str): The type of alert channel you wish to update. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertChannels/paths/~1api~1v2~1AlertChannels/post>`_ for valid values.
            enabled (bool|int): A boolean/integer representing whether the object is enabled. (0 or 1)
            data (dict): A dict matching the schema for the specified type. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertChannels/paths/~1api~1v2~1AlertChannels/post>`_ for valid values.
            request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated alert channel info.
        """

        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid, name=name, type=type, enabled=enabled, data=data, **request_params
        )

    def delete(self, guid):
        """A method to delete an AlertChannels object.

        Args:
            guid (str): A string representing the object GUID.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        return super().delete(id=guid)

    def test(self, guid):
        """A method to test an AlertChannels object.

        Args:
            guid (str): A string representing the object GUID.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        response = self._session.post(self._build_url(resource=guid, action="test"))

        return response
