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
               type,
               filters,
               intg_guid_list,
               **request_params):
        """
        A method to create a new DataExportRules object.

        Args:
            type(str): A string representing the type of rule to be added.
            filters(dict): A dictionary containing the name(string), description(string), enabled(bool), and
                           profile_version(list[string]) fields.
            intg_guid_list(str): A list of strings representing the guids of the alert channels to use (s3 only).
            request_params(any): Additional request parameters.
            (provides support for parameters that may be added in the future)

        Return:
            response(json)
        """

        return super().create(
            filters=self._format_filters(filters),
            type=type,
            intg_guid_list=intg_guid_list,
            **request_params
        )

    def get(self,
            guid=None):
        """
        A method to get DataExportRules objects.

        Args:

            guid(str): A string representing the object GUID.


        Return:
             response(json)
        """

        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """
        A method to get an DataExportRules object by GUID.

        Args:

            guid(str): A string representing the object GUID.


        Return:
             response(json)
        """

        return self.get(guid=guid)

    def update(self,
               guid,
               filters=None,
               intg_guid_list=None,
               type=None,
               **request_params):
        """
        A method to update an existing DataExportRules object.

        Args:
            guid(str): A string representing the object GUID.
            type(str): A string representing the type of rule.
            filters(dict): A dictionary containing the name(string), description(string), enabled(bool), and
                           profile_version(list[string]) fields.
            intg_guid_list(str): A list of strings representing the guids of the alert channels to use (s3 only).
            request_params(any): Additional request parameters.
            (provides support for parameters that may be added in the future)

        Return:
            response(json)
        """

        return super().update(
            id=guid,
            filters=self._format_filters(filters),
            type=type,
            intg_guid_list=intg_guid_list,
            **request_params
        )

    def delete(self,
               guid):
        """
        A method to delete a DataExportRules object.

        Args:
            guid(str): A string representing the object GUID.

        Return:
            response(json)
        """

        return super().delete(id=guid)
