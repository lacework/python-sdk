# -*- coding: utf-8 -*-
"""Lacework Policies API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PoliciesAPI(CrudEndpoint):
    """A class used to represent the `Policies API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Policies>`_

    Policies are a mechanism used to add annotated metadata to queries for improving the context of alerts, reports,
    and information displayed in the Lacework Console. You can fully customize policies.
    """

    def __init__(self, session):
        """Initializes the PoliciesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            PoliciesAPI: An instance of this class

        """
        super().__init__(session, "Policies")

    def create(
        self,
        policy_type,
        query_id,
        enabled,
        title,
        description,
        remediation,
        severity,
        alert_enabled,
        alert_profile,
        limit=1000,
        eval_frequency=None,
        tags=[],
        **request_params,
    ):
        """A method to create a new Policies object.

        Args:
          policy_type (str, optional): The policy type. Valid values are: "Violation"
          query_id (str): The policy query ID.
          enabled (bool): Whether the policy is enabled.
          title (str): The policy title.
          description (str): The policy description.
          remediation (str): The remediation strategy for the object.
          severity (str): A string representing the object severity. Valid values are :\
          "info", "low", "medium", "high", "critical"
          alert_enabled (bool): A boolean representing whether alerting is enabled.
          alert_profile (str, optional): A string representing the alert profile.
          limit (int, optional): An integer representing the number of results to return. (Default value = 1000)
          tags (list of str): A list of policy tags
          eval_frequency (str, optional, deprecated): A string representing the frequency in which to evaluate the \
          object. Valid values are: "Hourly", "Daily"
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
          dict: The newly created policy.

        """
        return super().create(
            policy_type=policy_type,
            query_id=query_id,
            enabled=enabled,
            title=title,
            description=description,
            remediation=remediation,
            severity=severity,
            alert_enabled=alert_enabled,
            alert_profile=alert_profile,
            tags=tags,
            limit=limit,
            eval_frequency=eval_frequency,
            **request_params,
        )

    def get(self, policy_id=None):
        """A method to get Policies objects. Using no args will get all policies.

        Args:
          policy_id (str, optional): A string representing the object policy ID.

        Returns:
          dict: The requested policies

        """
        return super().get(id=policy_id)

    def get_by_id(self, policy_id):
        """A method to get a Policies object by policy ID.

        Args:
          policy_id(str): A string representing the object policy ID.

        Returns:
          dict: The requested policy

        """
        return self.get(policy_id=policy_id)

    def update(
        self,  # noqa: C901
        policy_id,
        policy_type=None,
        query_id=None,
        enabled=None,
        title=None,
        description=None,
        remediation=None,
        severity=None,
        alert_enabled=None,
        alert_profile=None,
        limit=None,
        tags=[],
        eval_frequency=None,
        **request_params,
    ):
        """A method to update a Lacework Query Language (LQL) policy.

        Args:
          policy_id(str): A string representing the object policy ID.
          policy_type (str, optional): The policy type. Valid values are: "Violation"
          query_id (str, optional): The policy query ID.
          enabled (bool, optional): Whether the policy is enabled.
          title (str, optional): The policy title.
          description (str, optional): The policy description.
          remediation (str, optional): The remediation strategy for the object.
          severity (str, optional): A string representing the object severity. Valid values are :\
          "info", "low", "medium", "high", "critical"
          alert_enabled (bool, optional): A boolean representing whether alerting is enabled.
          alert_profile (str, optional): A string representing the alert profile.
          limit (int, optional): An integer representing the number of results to return. (Default value = 1000)
          tags (list of str, optional): A list of policy tags
          eval_frequency (str, optional, deprecated): A string representing the frequency in which to evaluate the \
          object. Valid values are: "Hourly", "Daily"
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
          dict: The newly created policy.

        """
        if enabled is not None:
            enabled = bool(enabled)

        if alert_enabled is not None:
            alert_enabled = bool(alert_enabled)

        return super().update(
            id=policy_id,
            policy_type=policy_type,
            query_id=query_id,
            enabled=enabled,
            title=title,
            description=description,
            remediation=remediation,
            severity=severity,
            alert_enabled=alert_enabled,
            alert_profile=alert_profile,
            limit=limit,
            tags=tags,
            eval_frequency=eval_frequency,
            **request_params,
        )

    def bulk_update(self, json):
        """A method to update Policy objects in bulk.

        Args:
          json (list of dicts): A list of dictionaries containing policy configuration.
              - policyId (str): The ID of the policy.
              - enabled (bool): The status of the policy.
              - severity (str): The severity of the policy. Valid values: "info", "low", "medium", "high", "critical"

        Returns:
          dict: The updated policies.

        """
        response = self._session.patch(self._build_url(), json=json)

        return response.json()

    def delete(self, policy_id):
        """A method to delete a policy.

        Args:
          policy_id (str): A string representing the policy ID.

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=policy_id)
