# -*- coding: utf-8 -*-
"""
Lacework Alert Rules API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class AlertRulesAPI(object):
    """
    Lacework Alert Rules API.
    """

    def __init__(self, session):
        """
        Initializes the AlertRulesAPI object.

        :param session: An instance of the HttpSession class

        :return AlertRulesAPI object.
        """

        super(AlertRulesAPI, self).__init__()

        self._session = session

    def create(self,
               type,
               filters,
               intg_guid_list,
               org=False):
        """
        A method to create a new alert rule.

        :param type: A string representing the type of the alert rule.
            ('Event')
        :param filters: A filter object for the alert rule configuration.
            obj:
                :param name: A string representing the alert rule name.
                :param description: A string representing the alert rule description.
                :param enabled: A boolean/integer representing whether the alert rule is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the alert rule.
                :param eventCategory: A list of event categories to define for the alert rule.
                    ("Compliance", "App", "Cloud", "Aws", "AzureActivityLog", "GcpAuditTrail",
                    "File", "Machine", "User")
                :param severity: A list of alert severities to define for the alert rule.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the alert channels to use.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating alert rule in Lacework...")

        # Build the Alert Rules request URI
        api_uri = "/api/v2/AlertRules"

        data = {
            "type": type,
            "filters": self._build_filters(filters),
            "intgGuidList": intg_guid_list
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            guid=None,
            org=False):
        """
        A method to get alert rules.

        :param guid: A string representing the alert rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting alert rule info from Lacework...")

        # Build the Alert Rules request URI
        if guid:
            api_uri = f"/api/v2/AlertRules/{guid}"
        else:
            api_uri = "/api/v2/AlertRules"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_guid(self,
                    guid,
                    org=False):
        """
        A method to get an alert rule by GUID.

        :param guid: A string representing the alert rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search alert rules.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching alert rules from Lacework...")

        # Build the Alert Rules request URI
        api_uri = "/api/v2/AlertRules/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               guid,
               type=None,
               filters=None,
               intg_guid_list=None,
               org=False):
        """
        A method to update an alert rule.

        :param guid: A string representing the alert rule GUID.
        :param type: A string representing the type of the alert rule.
            ('Event')
        :param filters: A filter object for the alert rule configuration.
            obj:
                :param name: A string representing the alert rule name.
                :param description: A string representing the alert rule description.
                :param enabled: A boolean/integer representing whether the alert rule is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the alert rule.
                :param eventCategory: A list of event categories to define for the alert rule.
                    ("Compliance", "App", "Cloud", "Aws", "AzureActivityLog", "GcpAuditTrail",
                    "File", "Machine", "User")
                :param severity: A list of alert severities to define for the alert rule.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the alert channels to use.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating alert rule in Lacework...")

        # Build the Alert Rules request URI
        api_uri = f"/api/v2/AlertRules/{guid}"

        tmp_data = {}

        if type:
            tmp_data["type"] = type
        if filters:
            tmp_data["filters"] = self._build_filters(filters)
        if intg_guid_list:
            tmp_data["intgGuidList"] = intg_guid_list

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()

    def delete(self,
               guid,
               org=False):
        """
        A method to delete an alert rule.

        :param guid: A string representing the alert rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting alert rule in Lacework...")

        # Build the AlertRules request URI
        api_uri = f"/api/v2/AlertRules/{guid}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()

    def _build_filters(self,
                       filters):
        """
        A method to properly structure the filters object.
        """

        keys = filters.keys()

        response = {}

        if "name" in keys:
            response["name"] = filters["name"]
        if "description" in keys:
            response["description"] = filters["description"]
        if "enabled" in keys:
            response["enabled"] = int(bool(filters["enabled"]))
        if "resourceGroups" in keys:
            response["resourceGroups"] = filters["resourceGroups"]
        if "eventCategory" in keys:
            response["eventCategory"] = filters["eventCategory"]
        if "severity" in keys:
            response["severity"] = filters["severity"]

        return response
