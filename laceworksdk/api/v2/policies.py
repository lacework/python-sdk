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
        :type policy_type: str
        :param query_id: A string representing the object query ID.
        :type query_id: str
        :param enabled: A boolean representing whether the object is enabled.
        :type enabled: bool
        :param title: A string representing the object title.
        :type title: str
        :param description: A string representing the object description.
        :type description: str
        :param remediation: A string representing the remediation strategy for the object.
        :type remediation: str
        :param severity: A string representing the object severity.
            ("info", "low", "medium", "high", "critical")
        :type severity: str
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :type alert_enabled: bool
        :param alert_profile: A string representing the alert profile.
        :type alert_profile: str
        :param evaluator_id: A string representing the evaluator in which the object is to be run.
        :type evaluator_id: str
        :param limit: An integer representing the number of results to return.
        :type limit: int
        :param eval_frequency: A string representing the frequency in which to evaluate the object.
            ("Hourly", "Daily")
        :type eval_frequency: str
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return: response json
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
        :type policy_id: str

        :return: response json
        """

        return super().get(id=policy_id)

    def get_by_id(self,
                  policy_id):
        """
        A method to get a Policies object by policy ID.

        :param policy_id: A string representing the object policy ID.
        :type policy_id: str

        :return: response json
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
        :type policy_id: str
        :param policy_type: A string representing the object policy type.
        :type policy_type: str
        :param query_id: A string representing the object query ID.
        :type query_id: str
        :param enabled: A boolean representing whether the object is enabled.
        :type enabled: bool
        :param title: A string representing the object title.
        :type title: str
        :param description: A string representing the object description.
        :type description: str
        :param remediation: A string representing the remediation strategy for the object.
        :type remediation: str
        :param severity: A string representing the object severity.
            ("info", "low", "medium", "high", "critical")
        :type severity: str
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :type alert_enabled: bool
        :param alert_profile: A string representing the alert profile.
        :type alert_profile: str
        :param limit: An integer representing the number of results to return.
        :type limit: int
        :param eval_frequency: A string representing the frequency in which to evaluate the object.
            ("Hourly", "Daily")
        :type eval_frequency: str
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return: response json
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
        """
        A method to update Policy objects in bulk

        :param json: A list of JSON objects containing policy configuration.
        :type json: list(dict(str, Any))
            obj:
                :param policyId: A string representing the ID of the policy.
                :param enabled: A boolean representing the status of the policy.
                :param severity: A string representing the severity of the policy.
                    ("info", "low", "medium", "high", "critical")

        :return: response json
        """

        response = self._session.patch(self.build_url(), json=json)

        return response.json()

    def delete(self,
               policy_id):
        """
        A method to delete a Policies object.

        :param policy_id: A string representing the object policy ID.
        :type policy_id: str

        :return: response json
        """

        return super().delete(id=policy_id)
