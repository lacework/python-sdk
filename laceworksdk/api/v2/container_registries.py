# -*- coding: utf-8 -*-
"""Lacework ContainerRegistries API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ContainerRegistriesAPI(CrudEndpoint):
    """A class used to represent the `Container Registries API endpoint <https://docs.lacework.net/api/v2/docs/#tag/ContainerRegistries>`_

    Lacework provides the ability to assess, identify, and report vulnerabilities found in the operating system
    software packages in a Docker container image. After integrating a container registry in Lacework, Lacework finds
    all container images in the registry repositories, assesses those container images for software packages with
    known vulnerabilities, and reports them.
    """

    def __init__(self, session):
        """Initializes the ContainerRegistriesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            ContainerRegistriesAPI: An instance of this class

        """
        super().__init__(session, "ContainerRegistries")

    def create(self, name, type, enabled, data, **request_params):
        """A method to create a new container registry integration.

        Args:
          name (str): The name to use to create the container registry integration.
          enabled (bool|int): Whether the integration is enabled.
          type (str): The type of the integration. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ContainerRegistries/paths/~1api~1v2~1ContainerRegistries/post>`_ for valid values.
          enabled (bool|int): Whether the object is enabled.
          data (dict): The definition of the new integration to create. Note this changes depending on the value of the "type" field. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ContainerRegistries/paths/~1api~1v2~1ContainerRegistries/post>`_ for valid values.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: Details for the newly created container registry integration

        """
        return super().create(
            name=name,
            type=type,
            enabled=int(bool(enabled)),
            data=data,
            **request_params,
        )

    def get(self, guid=None, type=None):
        """A method to get ContainerRegistries objects. Using no args will get all integrations.

        Args:
          guid (str, optional): The GUID of the container registry integration to get.
          type (str, optional): The type of the container registry integration(s) to get. Valid types are: "ContVulnCfg"

        Returns:
            dict: The details of the requested integration(s)

        """
        return super().get(id=guid, resource=type)

    def get_by_guid(self, guid):
        """A method to get a container registry integration by GUID.

        Args:
          guid (str): The GUID of the container registry integration to get

        Returns:
            dict: The details of the requested integration
        """
        return self.get(guid=guid)

    def get_by_type(self, type):
        """A method to get container registry integration(s) by type.

        Args:
          type (str): The type of the container registry integration(s) to get. Valid types are: "ContVulnCfg"

        Returns:
            dict: The details of the requested integration(s)

        """
        return self.get(type=type)

    def update(
        self, guid, name=None, type=None, enabled=None, data=None, **request_params
    ):
        """A method to update an ContainerRegistries object.

        Args:
          guid: A string representing the object GUID.
          name (str): The name to use to create the container registry integration.
          enabled (bool|int): Whether the integration is enabled.
          type (str): The type of the integration. See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ContainerRegistries/paths/~1api~1v2~1ContainerRegistries/post>`_ for valid values.
          enabled (bool|int): Whether the object is enabled.
          data (dict): The definition of the new integration to create. Note this changes depending on the value of the "type" field. \
          See the `API docs <https://docs.lacework.net/api/v2/docs/#tag/ContainerRegistries/paths/~1api~1v2~1ContainerRegistries/post>`_ for valid values.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: Details for the updated container registry integration

        """
        if enabled is not None:
            enabled = int(bool(enabled))

        return super().update(
            id=guid, name=name, type=type, enabled=enabled, data=data, **request_params
        )

    def delete(self, guid):
        """A method to delete a container registry integration .

        Args:
          guid (str): The GUID of the container registry integration to delete

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
