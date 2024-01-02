# -*- coding: utf-8 -*-
"""Lacework DataExportRules API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class DataExportRulesAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the DataExportRulesAPI object.

        Args:
          session: An instance of the HttpSession class

        :return DataExportRulesAPI object.

        Returns:

        """
        super().__init__(session, "DataExportRules")

    def create(self,
               type,
               filters,
               intg_guid_list,
               **request_params):
        """A method to create a new DataExportRules object.

        Args:
          type: str
          filters: dict
          profile_version: list
          intg_guid_list: str
          request_params: any
          provides: support for parameters that may be added in the future
          **request_params: 

        Returns:
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
        """A method to get DataExportRules objects.

        Args:
          guid: str (Default value = None)

        Returns:
          response(json)

        """
        return super().get(id=guid)

    def get_by_guid(self,
                    guid):
        """A method to get an DataExportRules object by GUID.

        Args:
          guid: str

        Returns:
          response(json)

        """
        return self.get(guid=guid)

    def update(self,
               guid,
               filters=None,
               intg_guid_list=None,
               type=None,
               **request_params):
        """A method to update an existing DataExportRules object.

        Args:
          guid: str
          type: str (Default value = None)
          filters: dict (Default value = None)
          profile_version: list
          intg_guid_list: str (Default value = None)
          request_params: any
          provides: support for parameters that may be added in the future
          **request_params: 

        Returns:
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
        """A method to delete a DataExportRules object.

        Args:
          guid: str

        Returns:
          response(json)

        """
        return super().delete(id=guid)
