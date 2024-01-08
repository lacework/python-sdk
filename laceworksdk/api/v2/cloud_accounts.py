# -*- coding: utf-8 -*-
"""Lacework CloudAccounts API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class CloudAccountsAPI(CrudEndpoint):
    """A class used to represent the `Cloud Accounts API endpoint <https://docs.lacework.net/api/v2/docs/#tag/CloudAccounts>`_

    Cloud accounts are integrations between Lacework and cloud providers such as Amazon Web Services, Microsoft Azure, and Google Cloud Platform.
    """

    def __init__(self, session):
        """Initializes the CloudAccountsAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            CloudAccountsAPI: An instance of this class

        """
        super().__init__(session, "CloudAccounts")

    def create(self, name, type, enabled, data, **request_params):
        """A method to create a new cloud accounts integration.

        Args:
          name (str): The name of the integration to create.
          type (str): The type of the integration. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/CloudAccounts/paths/~1api~1v2~1CloudAccounts/post>`_ for valid values.
          enabled (bool|int): Whether the object is enabled.
          data (dict): The definition of the new integration to create. Note this changes depending on the value of the "type" field. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/CloudAccounts/paths/~1api~1v2~1CloudAccounts/post>`_ for valid values.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: Details of the newly created cloud account integration.

        """
        return super().create(
            name=name,
            type=type,
            enabled=int(bool(enabled)),
            data=data,
            **request_params,
        )

    def get(self, guid=None, type=None):
        """A method to get cloud account integrations. Using no args will get all integrations.

        Args:
          guid (str, optional): The GUID of the integration to retrieve.
          type (str, optional): The type of the integration(s) to retrieve. Valid types are: "AwsCfg", "AwsCtSqs", \
          "AwsEksAudit", "AwsUsGovCfg", "AwsUsGovCtSqs", "AzureAlSeq", "AzureCfg", "GcpAtSes", "GcpCfg"

        Returns:
            dict: The details of the requested integration(s)
        """
        return super().get(id=guid, resource=type)

    def get_by_guid(self, guid):
        """A method to get a cloud account integration by its GUID.

        Args:
          guid (str): The GUID of the integration to retrieve.

        Returns:
            dict: The details of the requested integration.
        """
        return self.get(guid=guid)

    def get_by_type(self, type):
        """A method to get cloud account integration(s) by type.

        Args:
            type (str, optional): The type of the integration(s) to retrieve. Valid types are: "AwsCfg", "AwsCtSqs",\
             "AwsEksAudit", "AwsUsGovCfg", "AwsUsGovCtSqs", "AzureAlSeq", "AzureCfg", "GcpAtSes", "GcpCfg"
        
        Returns:
            dict: The details of the requested integration(s)
        """
        return self.get(type=type)

    def update(
        self, guid, name=None, type=None, enabled=None, data=None, **request_params
    ):
        """A method to update an CloudAccounts object.

        Args:
          guid (str): The GUID of the integration to update.
          name (str, optional): The integration name.
          type (str): The type of the integration. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/CloudAccounts/paths/~1api~1v2~1CloudAccounts/post>`_ for valid values.
          enabled (bool|int): Whether the object is enabled.
          data (dict): The definition of the new integration to create. Note this changes depending on the value of the "type" field. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/CloudAccounts/paths/~1api~1v2~1CloudAccounts/post>`_ for valid values.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated details for the integration specified.

        """
        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid, name=name, type=type, enabled=enabled, data=data, **request_params
        )

    def delete(self, guid):
        """A method to delete a cloud account integration.

        Args:
          guid (str): The integration GUID to delete.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        return super().delete(id=guid)
