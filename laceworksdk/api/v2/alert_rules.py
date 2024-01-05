# -*- coding: utf-8 -*-
"""Lacework AlertRules API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertRulesAPI(CrudEndpoint):
    """A class used to represent the `Alert Rules API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AlertRules>`_

    Lacework combines alert channels and alert rules to provide a flexible method for routing alerts. For alert
    channels, you define information about where to send alerts, such as to Jira, Slack, or email. For alert rules,
    you define information about which alert types to send, such as critical and high severity compliance alerts.
    """

    def __init__(self, session):
        """Initializes the AlertRulesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            AlertRulesAPI: returns an AlertRulesAPI object
        """
        super().__init__(session, "AlertRules")

    def create(self, type, filters, intg_guid_list, **request_params):
        """A method to create new Alert Rules.

        Args:
            type (str): The type of the alert rule. Valid values are: "Event"
            filters (dict): The alert rule definition. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertRules/paths/~1api~1v2~1AlertRules/post>`_ for valid values.
            intg_guid_list (list of str): A list of GUIDs representing the alert channels to use.

            request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The new rule.
        """
        return super().create(
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            **request_params,
        )

    def get(self, guid=None):
        """A method to get AlertRules objects.

        Args:
            guid (str): The alert rule GUID to retrieve.

        Returns:
            dict: The alert rule(s)

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get an AlertRules object by GUID.

        Args:
            guid (str): The alert rule GUID.

        Returns:
            dict: The alert rule

        """
        return self.get(guid=guid)

    def update(self, guid, filters=None, intg_guid_list=None, **request_params):
        """A method to update an AlertRules object.

        Args:
            guid (str): The Alert Rule GUID you wish to update.
            filters (dict, optional): The alert rule definition. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/AlertRules/paths/~1api~1v2~1AlertRules~1%7BmcGuid%7D/patch>`_ for valid values.
            intg_guid_list (list of str, optional): A list of GUIDs representing the alert channels to use.
            request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated alert rule

        """
        return super().update(
            id=guid,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete an AlertRules object.

        Args:
            guid (str): The alert rule GUID.

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
