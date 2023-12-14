# -*- coding: utf-8 -*-
"""
Lacework DataExportRules API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class DataExportRulesAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the DataExportRulesAPI object.

        :param session: An instance of the HttpSession class

        :return DataExportRulesAPI object.
        """

        super().__init__(session, "DataExportRules")

    def create(self,
               name,
               enabled,
               int_guid_list,
               rule_type,
               description='',
               profile_versions=[],
               **request_params):
        """
        A method to create a new DataExportRules object.

        Args:
            name(str): A string representing the rule name.
            description(str): A string representing the rule description. (optional)
            enabled(bool): A boolean/integer representing whether the object is enabled.
            rule_type(str): A string representing the type of rule to be added.
            profile_version(list): A list of strings representing profile versions. (optional)
            int_guid_list(str): A list of strings representing the guids of the alert channels to use.

            request_params(any): Additional request parameters.
            (provides support for parameters that may be added in the future)

        Return:
            response(json)
        """
        filters = {
            'name': name,
            'description': description,
            'enabled': int(bool(enabled)),
            'profileVersions': profile_versions
        }
        return super().create(
            filters=filters,
            type=rule_type,
            int_guid_list=int_guid_list,
            **request_params
        )

    def get(self,
            guid=None):
        """
        A method to get DataExportRules objects.

        :param guid: A string representing the object GUID.
        :param type: A string representing the object type.

        :return response json
        """

        return super().get(id=guid)


    def update(self,
               name,
               enabled,
               int_guid_list,
               rule_type,
               description='',
               profile_versions=[],
               **request_params):
        """
        A method to create a new DataExportRules object.

        Args:
            name(str): A string representing the rule name.
            description(str): A string representing the rule description. (optional)
            enabled(bool): A boolean/integer representing whether the object is enabled.
            rule_type(str): A string representing the type of rule to be added.
            profile_version(list): A list of strings representing profile versions. (optional)
            int_guid_list(str): A list of strings representing the guids of the alert channels to use.

            request_params(any): Additional request parameters.
            (provides support for parameters that may be added in the future)

        Return:
            response(json)
        """

        if enabled is not None:
            enabled = int(bool(enabled))

        filters = {
            'name': name,
            'description': description,
            'enabled': enabled,
            'profileVersions': profile_versions
        }

        return super().update(
            filters=filters,
            type=rule_type,
            int_guid_list=int_guid_list,
            **request_params
        )

    def delete(self,
               guid):
        """
        A method to delete a DataExportRules object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)
