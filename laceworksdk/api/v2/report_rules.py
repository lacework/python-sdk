# -*- coding: utf-8 -*-
"""
Lacework ReportRules API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ReportRulesAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the ReportRulesAPI object.

        :param session: An instance of the HttpSession class

        :return ReportRulesAPI object.
        """

        super().__init__(session, "ReportRules")

    def create(self,
               type,
               filters,
               intg_guid_list,
               report_notification_types,
               **request_params):
        """
        A method to create a new ReportRules object.

        :param type: A string representing the type of the object.
            ('Report')
        :param filters: A filter object for the object configuration.
            obj:
                :param name: A string representing the object name.
                :param description: A string representing the object description.
                :param enabled: A boolean/integer representing whether the object is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the object.
                :param severity: A list of alert severities to define for the object.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the report channels to use.
        :param report_notification_types: An object of booleans for the types of reports that should be sent.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            report_notification_types=report_notification_types,
            **request_params
        )

    def get(self,
            guid=None):
        """
        A method to get ReportRules objects.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """
        A method to get a ReportRules object by GUID.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return self.get(guid=guid)

    def update(self,
               guid,
               type=None,
               filters=None,
               intg_guid_list=None,
               report_notification_types=None,
               **request_params):
        """
        A method to update a ReportRules object.

        :param guid: A string representing the object GUID.
        :param type: A string representing the type of the object.
            ('Report')
        :param filters: A filter object for the object configuration.
            obj:
                :param name: A string representing the object name.
                :param description: A string representing the object description.
                :param enabled: A boolean/integer representing whether the object is enabled.
                    (0 or 1)
                :param resourceGroups: A list of resource groups to define for the object.
                :param severity: A list of alert severities to define for the object.
                    (1, 2, 3, 4, 5)
        :param intg_guid_list: A list of integration GUIDs representing the report channels to use.
        :param report_notification_types: An object of booleans for the types of reports that should be sent.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().update(
            id=guid,
            type=type,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            report_notification_types=report_notification_types,
            **request_params
        )

    def delete(self,
               guid):
        """
        A method to delete a ReportRules object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)
