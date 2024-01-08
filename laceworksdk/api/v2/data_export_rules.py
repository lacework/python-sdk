# -*- coding: utf-8 -*-
"""Lacework DataExportRules API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class DataExportRulesAPI(CrudEndpoint):
    """A class used to represent the `Data Export Rules API endpoint <https://docs.lacework.net/api/v2/docs/#tag/DataExportRules>`_

    S3 data export allows you to export data collected from your Lacework account and send it to an S3 bucket of your
    choice. You can extend Lacework processed/normalized data to report/visualize alone or combine with other
    business/security data to get insights and make meaningful business decisions.
    """

    def __init__(self, session):
        """Initializes the DataExportRulesAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            DataExportRulesAPI: An instance of this class.

        """
        super().__init__(session, "DataExportRules")

    def create(self, type, filters, intg_guid_list, **request_params):
        """A method to create a new DataExportRules object.

        Args:
          type (str): The type of data export rule to create. Valid values are:  "Dataexport"
          intg_guid_list (list of str): The guids of the alert channels for the rule to use
          filters (dict): A dict containing the fields needed to define the rule. fields are:

              - name (str): The name of the alert
              - enabled (bool|int): Whether the export rule is enabled
              - description (str, optional): The description of the export rule
              - profileVersions (list of str, optional): A list of profile versions

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
          dict: The created data export rule

        """
        return super().create(
            filters=self._format_filters(filters),
            type=type,
            intg_guid_list=intg_guid_list,
            **request_params,
        )

    def get(self, guid=None):
        """A method to get data export rules. Using no args will get all rules.

        Args:
          guid (str, optional): The guid of the rule to get.

        Returns:
          dict: The requested data export rule(s)

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """A method to get an DataExportRules object by GUID.

        Args:
          guid (str): The guid of the rule to get.

        Returns:
          dict: The requested data export rule

        """
        return self.get(guid=guid)

    def update(
        self, guid, filters=None, intg_guid_list=None, **request_params
    ):
        """A method to update an existing DataExportRules object.

        Args:
          guid (str): The guid of the export rule to update
          intg_guid_list (list of str): The guids of the alert channels for the rule to use
          filters (dict): A dict containing the fields needed to define the rule. fields are:

              - name (str, optional): The name of the alert
              - enabled (bool|int, optional): Whether the export rule is enabled
              - description (str, optional): The description of the export rule
              - profileVersions (list of str, optional): A list of profile versions

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
          dict: The updated data export rule

        """
        return super().update(
            id=guid,
            filters=self._format_filters(filters),
            intg_guid_list=intg_guid_list,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete a data export rule.

        Args:
          guid (str): The GUID of the data export rule to delete

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
