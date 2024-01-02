# -*- coding: utf-8 -*-
"""Lacework Policies API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PoliciesAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the PoliciesAPI object.

        Args:
          session: An instance of the HttpSession class

        :return PoliciesAPI object.

        Returns:

        """
        super().__init__(session, "Policies")

    def create(self,
               policy_type,
               query_id,
               enabled,
               title,
               description,
               remediation,
               severity,
               alert_enabled,
               alert_profile,
               evaluator_id=None,
               limit=None,
               eval_frequency=None,
               **request_params):
        """A method to create a new Policies object.

        Args:
          policy_type(str): A string representing the object policy type.
          query_id(str): A string representing the object query ID.
          enabled(bool): A boolean representing whether the object is enabled.
          title(str): A string representing the object title.
          description(str): A string representing the object description.
          remediation(str): A string representing the remediation strategy for the object.
          severity(str): A string representing the object severity.
        ("info", "low", "medium", "high", "critical")
          alert_enabled(bool): A boolean representing whether alerting is enabled.
          alert_profile(str): A string representing the alert profile.
          evaluator_id(str, optional): A string representing the evaluator in which the object is to be run. (Default value = None)
          limit(int, optional): An integer representing the number of results to return. (Default value = None)
          eval_frequency(str, optional): A string representing the frequency in which to evaluate the object.
        ("Hourly", "Daily") (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
          **request_params: 

        Returns:
          response json

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
            evaluator_id=evaluator_id,
            limit=limit,
            eval_frequency=eval_frequency,
            **request_params
        )

    def get(self,
            policy_id=None):
        """A method to get Policies objects.

        Args:
          policy_id(str, optional): A string representing the object policy ID. (Default value = None)

        Returns:
          response json

        """
        return super().get(id=policy_id)

    def get_by_id(self,
                  policy_id):
        """A method to get a Policies object by policy ID.

        Args:
          policy_id(str): A string representing the object policy ID.

        Returns:
          response json

        """
        return self.get(policy_id=policy_id)

    def update(self,  # noqa: C901
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
               eval_frequency=None,
               **request_params):
        """A method to update a Lacework Query Language (LQL) policy.

        Args:
          policy_id(str): A string representing the object policy ID.
          policy_type(str, optional): A string representing the object policy type. (Default value = None)
          query_id(str, optional): A string representing the object query ID. (Default value = None)
          enabled(bool, optional): A boolean representing whether the object is enabled. (Default value = None)
          title(str, optional): A string representing the object title. (Default value = None)
          description(str, optional): A string representing the object description. (Default value = None)
          remediation(str, optional): A string representing the remediation strategy for the object. (Default value = None)
          severity(str, optional): A string representing the object severity.
        ("info", "low", "medium", "high", "critical") (Default value = None)
          alert_enabled(bool, optional): A boolean representing whether alerting is enabled. (Default value = None)
          alert_profile(str, optional): A string representing the alert profile. (Default value = None)
          limit(int, optional): An integer representing the number of results to return. (Default value = None)
          eval_frequency(str, optional): A string representing the frequency in which to evaluate the object.
        ("Hourly", "Daily") (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
          # noqa: C901policy_id: 
          **request_params: 

        Returns:
          response json

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
            eval_frequency=eval_frequency,
            **request_params
        )

    def bulk_update(self,
                    json):
        """A method to update Policy objects in bulk.

        Args:
          json(list(dict(str, Any))
    obj:): A list of JSON objects containing policy configuration.
          policyId: A string representing the ID of the policy.
          enabled: A boolean representing the status of the policy.
          severity: A string representing the severity of the policy.
        ("info", "low", "medium", "high", "critical")

        Returns:
          response json

        """
        response = self._session.patch(self.build_url(), json=json)

        return response.json()

    def delete(self,
               policy_id):
        """A method to delete a Policies object.

        Args:
          policy_id(str): A string representing the object policy ID.

        Returns:
          response json

        """
        return super().delete(id=policy_id)
