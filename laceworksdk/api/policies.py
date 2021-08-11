# -*- coding: utf-8 -*-
"""
Lacework Policies API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class PoliciesAPI(object):

    def __init__(self, session):
        """
        Initializes the PoliciesAPI object.

        :param session: An instance of the HttpSession class

        :return PoliciesAPI object.
        """

        super(PoliciesAPI, self).__init__()

        self._session = session

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
               evaluator_id,
               limit=None,
               eval_frequency=None,
               policy_ui=None,
               org=False):
        """
        A method to create a new Lacework Query Language (LQL) policy.

        :param policy_type: A string representing the policy type.
        :param query_id: A string representing the LQL query ID.
        :param enabled: A boolean representing whether the policy is enabled.
        :param title: A string representing the policy title.
        :param description: A string representing the policy description.
        :param remediation: A string representing the remediation strategy for the policy.
        :param severity: A string representing the policy severity.
            ("info", "low", "medium", "high", "critical")
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :param alert_profile: A string representing the alert profile.
        :param evaluator_id: A string representing the evaluator in which the policy is to be run.
        :param limit: An integer representing the number of results to return.
        :param eval_frequency: A string representing the frequency in which to evaluate the policy.
            ("Hourly", "Daily")
        :param policy_ui: A dictionary which specifies the policyUi domain and subdomain.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating LQL policy in Lacework...")

        # Build the Policies request URI
        api_uri = "/api/v2/Policies"

        if policy_ui is None:
            policy_ui = {}

        data = {
            "policyType": policy_type,
            "queryId": query_id,
            "title": title,
            "enabled": int(bool(enabled)),
            "description": description,
            "remediation": remediation,
            "severity": severity,
            "alertEnabled": int(bool(alert_enabled)),
            "alertProfile": alert_profile,
            "policyUi": policy_ui,
            "evaluatorId": evaluator_id
        }

        if isinstance(limit, int) and limit >= 0:
            data["limit"] = limit
        if eval_frequency:
            data["evalFrequency"] = eval_frequency

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            policy_id=None,
            org=False):
        """
        A method to get LQL policies.

        :param policy_id: A string representing the LQL policy ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting LQL policy info from Lacework...")

        # Build the Policies request URI
        if policy_id:
            api_uri = f"/api/v2/Policies/{policy_id}"
        else:
            api_uri = "/api/v2/Policies"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_id(self,
                  policy_id,
                  org=False):
        """
        A method to get an LQL policy by policy ID.

        :param policy_id: A string representing the LQL policy ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(policy_id=policy_id, org=org)

    def update(self,
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
               policy_ui=None,
               org=False):
        """
        A method to update a Lacework Query Language (LQL) policy.

        :param policy_id: A string representing the policy ID.
        :param policy_type: A string representing the policy type.
        :param query_id: A string representing the LQL query ID.
        :param enabled: A boolean representing whether the policy is enabled.
        :param title: A string representing the policy title.
        :param description: A string representing the policy description.
        :param remediation: A string representing the remediation strategy for the policy.
        :param severity: A string representing the policy severity.
            ("info", "low", "medium", "high", "critical")
        :param alert_enabled: A boolean representing whether alerting is enabled.
        :param alert_profile: A string representing the alert profile.
        :param limit: An integer representing the number of results to return.
        :param eval_frequency: A string representing the frequency in which to evaluate the policy.
            ("Hourly", "Daily")
        :param policy_ui: A dictionary which specifies the policyUi domain and subdomain.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating LQL policy in Lacework...")

        # Build the Policies request URI
        api_uri = f"/api/v2/Policies/{policy_id}"

        data = {}

        if policy_type:
            data["policyType"] = policy_type
        if query_id:
            data["queryId"] = query_id
        if enabled is not None:
            data["enabled"] = bool(enabled)
        if title:
            data["title"] = title
        if description:
            data["description"] = description
        if remediation:
            data["remediation"] = remediation
        if severity:
            data["severity"] = severity
        if alert_enabled is not None:
            data["alertEnabled"] = bool(alert_enabled)
        if alert_profile:
            data["alertProfile"] = alert_profile
        if isinstance(limit, int) and limit >= 0:
            data["limit"] = limit
        if eval_frequency:
            data["evalFrequency"] = eval_frequency
        if policy_ui:
            data["policyUi"] = policy_ui

        response = self._session.patch(api_uri, org=org, data=data)

        return response.json()

    def delete(self,
               policy_id,
               org=False):
        """
        A method to delete a Lacework Query Language (LQL) policy.

        :param policy_id: A string representing the LQL policy ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting LQL policy in Lacework...")

        # Build the Policies request URI
        api_uri = f"/api/v2/Policies/{policy_id}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
