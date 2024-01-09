# -*- coding: utf-8 -*-
"""Lacework Exceptions API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PolicyExceptionsAPI(CrudEndpoint):
    """A class used to represent the `Policies Exceptions API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Exceptions>`_

    Policy exceptions are a mechanism used to maintain the policies but allow you to circumvent one or more restrictions.
    """

    def __init__(self, session):
        """Initializes the PolicyExceptionsAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            PolicyExceptionsAPI: An instance of this class

        """
        super().__init__(session, "Exceptions")

    def create(self, policy_id, description, constraints, **request_params):
        """A method to create a new Exceptions object.

        Args:
          policy_id (str): The object policy ID.
          description (str, optional): The object description.
          constraints (list of dicts): The object constraints. Dict fields are:
              - field_key (str): A string representing the constraint key. Values are:\
              'accountIds', 'resourceNames', 'regionNames' and 'resourceTags'
              - field_values (list of str): Constraint values

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The created policy exception

        """
        params = self._build_dict_from_items(policy_id=policy_id)

        return super().create(
            params=params,
            description=description,
            constraints=constraints,
            **request_params,
        )

    def get(self, exception_id=None, policy_id=None):
        """A method to get Exceptions objects.

        Args:
          exception_id (str, optional): A string representing the exception ID. (Default value = None)
          policy_id: The ID of the policy for which to get the exceptions.

        Returns:
            dict: The requested exception(s)

        """
        return super().get(id=exception_id, policy_id=policy_id)

    def get_by_id(self, exception_id, policy_id):
        """A method to get a Exceptions object by policy ID.

        Args:
          exception_id (str): A string representing the exception ID. (Default value = None)
          policy_id: The ID of the policy for which to get the exceptions.

        Returns:
            dict: The requested exception(s)

        """
        return self.get(exception_id=exception_id, policy_id=policy_id)

    def update(
        self,
        exception_id,
        policy_id,
        description=None,
        constraints=None,
        **request_params,
    ):
        """A method to create a new Exceptions object.

        Args:
          exception_id (str): The exception ID to update.
          policy_id (str): The object policy ID.
          description (str, optional): The object description.
          constraints (list of dicts, optional): The object constraints. Dict fields are:
              - field_key (str): A string representing the constraint key. Values are:\
              'accountIds', 'resourceNames', 'regionNames' and 'resourceTags'
              - field_values (list of str): Constraint values

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated policy exception

        """
        params = self._build_dict_from_items(policy_id=policy_id)

        return super().update(
            id=exception_id,
            params=params,
            description=description,
            constraints=constraints,
            **request_params,
        )

    def delete(self, exception_id, policy_id):
        """A method to delete a policy xception

        Args:
          exception_id (str): The exception ID.
          policy_id (str): The policy ID.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        params = self._build_dict_from_items(policy_id=policy_id)

        return super().delete(id=exception_id, params=params)
