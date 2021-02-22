# -*- coding: utf-8 -*-
"""
Lacework Report Rules API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class ReportRulesAPI(object):
    """
    Lacework Report Rules API.
    """

    def __init__(self, session):
        """
        Initializes the ReportRulesAPI object.

        :param session: An instance of the HttpSession class

        :return ReportRulesAPI object.
        """

        super(ReportRulesAPI, self).__init__()

        self._session = session

    def create(self,
               type,
               filters,
               intg_guid_list,
               report_notification_types,
               org=False):
        """
        A method to create a new report rule.

        :param type: A string representing the type of the report rule.
            ('Report')
        :param filters: A filter object for the report rule configuration.
            obj:
                :param name: A string representing the report rule name.
                :param description: A string representing the report rule description.
                :param enabled: A boolean/integer representing whether the report rule is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the report rule.
                :param severity: A list of alert severities to define for the report rule.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the report channels to use.
        :param report_notification_types: An object of booleans for the types of reports that should be sent.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating report rule in Lacework...")

        # Build the Report Rules request URI
        api_uri = "/api/v2/ReportRules"

        data = {
            "type": type,
            "filters": self._build_filters(filters),
            "intgGuidList": intg_guid_list,
            "reportNotificationTypes": self._build_report_notification_types(report_notification_types)
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            guid=None,
            org=False):
        """
        A method to get report rules.

        :param guid: A string representing the report rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting report rule info from Lacework...")

        # Build the Report Rules request URI
        if guid:
            api_uri = f"/api/v2/ReportRules/{guid}"
        else:
            api_uri = "/api/v2/ReportRules"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_guid(self,
                    guid,
                    org=False):
        """
        A method to get an report rule by GUID.

        :param guid: A string representing the report rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(guid=guid, org=org)

    def search(self,
               query_data=None,
               org=False):
        """
        A method to search report rules.

        :param query_data: A dictionary containing the desired search parameters.
            (filters, returns)

        :return response json
        """

        logger.info("Searching report rules from Lacework...")

        # Build the Report Rules request URI
        api_uri = "/api/v2/ReportRules/search"

        response = self._session.post(api_uri, data=query_data, org=org)

        return response.json()

    def update(self,
               guid,
               type=None,
               filters=None,
               intg_guid_list=None,
               report_notification_types=None,
               org=False):
        """
        A method to update an report rule.

        :param guid: A string representing the report rule GUID.
        :param type: A string representing the type of the report rule.
            ('Report')
        :param filters: A filter object for the report rule configuration.
            obj:
                :param name: A string representing the report rule name.
                :param description: A string representing the report rule description.
                :param enabled: A boolean/integer representing whether the report rule is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the report rule.
                :param severity: A list of alert severities to define for the report rule.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the report channels to use.
        :param report_notification_types: An object of booleans for the types of reports that should be sent.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating report rule in Lacework...")

        # Build the Report Rules request URI
        api_uri = f"/api/v2/ReportRules/{guid}"

        tmp_data = {}

        if type:
            tmp_data["type"] = type
        if filters:
            tmp_data["filters"] = self._build_filters(filters)
        if intg_guid_list:
            tmp_data["intgGuidList"] = intg_guid_list
        if report_notification_types:
            tmp_data["reportNotificationTypes"] = self._build_report_notification_types(report_notification_types)

        response = self._session.patch(api_uri, org=org, data=tmp_data)

        return response.json()

    def delete(self,
               guid,
               org=False):
        """
        A method to delete an report rule.

        :param guid: A string representing the report rule GUID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting report rule in Lacework...")

        # Build the ReportRules request URI
        api_uri = f"/api/v2/ReportRules/{guid}"

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
        if "severity" in keys:
            response["severity"] = filters["severity"]

        return response

    def _build_report_notification_types(self,
                                         report_notification_types):
        """
        A method to properly structure the report notification types object.
        """

        response = {}

        for report_notification_type in report_notification_types.keys():
            response[report_notification_type] = report_notification_types[report_notification_type]

        return response
