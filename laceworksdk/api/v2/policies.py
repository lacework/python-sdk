# -*- coding: utf-8 -*-
"""
Lacework Policies API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PoliciesAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the PoliciesAPI object.

        :param session: An instance of the HttpSession class

        :return PoliciesAPI object.
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
        """
        A method to create a new Policies object.

        :param policy_type: A string representing the object policy type.
        :param query_id: A string representing the object query ID.
        :param enabled: A boolean representing whether the object is enabled.
        :param title: A string representing the object title.
        :param description: A string representing the object description.
        :param remediation: A string representing the remediation strategy for the object.
        :param severity: A string representing the object severity.
            ("info", "low", "medium", "high", "critical")
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :param alert_profile: A string representing the alert profile.
        :param evaluator_id: A string representing the evaluator in which the object is to be run.
        :param limit: An integer representing the number of results to return.
        :param eval_frequency: A string representing the frequency in which to evaluate the object.
            ("Hourly", "Daily")
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            policy_type=policy_type,
            query_id=query_id,
            enabled=int(bool(enabled)),
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
        """
        A method to get Policies objects.

        :param policy_id: A string representing the object policy ID.

        :return response json
        """

        return super().get(id=policy_id)

    def get_by_id(self,
                  policy_id):
        """
        A method to get a Policies object by policy ID.

        :param policy_id: A string representing the object policy ID.

        :return response json
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
        """
        A method to update a Lacework Query Language (LQL) policy.

        :param policy_id: A string representing the object policy ID.
        :param policy_type: A string representing the object policy type.
        :param query_id: A string representing the object query ID.
        :param enabled: A boolean representing whether the object is enabled.
        :param title: A string representing the object title.
        :param description: A string representing the object description.
        :param remediation: A string representing the remediation strategy for the object.
        :param severity: A string representing the object severity.
            ("info", "low", "medium", "high", "critical")
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :param alert_profile: A string representing the alert profile.
        :param limit: An integer representing the number of results to return.
        :param eval_frequency: A string representing the frequency in which to evaluate the object.
            ("Hourly", "Daily")
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
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

    def delete(self,
               policy_id):
        """
        A method to delete a Policies object.

        :param policy_id: A string representing the object policy ID.

        :return response json
        """

        return super().delete(id=policy_id)
