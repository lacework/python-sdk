# -*- coding: utf-8 -*-
import logging

from urllib.parse import quote

from laceworksdk.exceptions import ApiError

logger = logging.getLogger(__name__)


class LqlPoliciesAPI(object):
    """
    Lacework LQL Policy API.
    """

    def __init__(self, session):
        """
        Initializes the LqlPoliciesAPI object.

        :param session: An instance of the HttpSession class.

        :return LqlPoliciesAPI object
        """
        super(LqlPoliciesAPI, self).__init__()

        self.lql_policies_base_uri = '/api/v1/external/lqlPolicies'
        self.lql_policies_identifier_key = 'POLICY_ID'
        self._session = session

    def create(self, policy_json, smart=False):
        """
        Create a LQL Policy

        Parameters:
        policy_json (dict): LQL Policy JSON
        smart (bool): Whether to update if policy already exists

        Return:
        response (dict): requests json() object
        """
        api_uri = self.lql_policies_base_uri

        try:
            response = self._session.post(api_uri, data=policy_json)
        except ApiError as e:
            if (
                smart
                and 'already exists' in str(e)
                and 'policy_id' in policy_json
            ):
                return self.update(policy_json)
            raise

        return response.json()

    def delete(self, policy_id):
        """
        Delete a LQL Policy

        Parameters:
        policy_id (str): LQL Policy ID

        Return:
        response (dict): requests json() object
        """
        api_uri = (
            f'{self.lql_policies_base_uri}'
            f'?{self.lql_policies_identifier_key}={quote(policy_id, safe="")}'
        )

        response = self._session.delete(api_uri)

        return response.json()

    def disable(self, policy_id, alert_enabled=None):
        """
        Disable a LQL Policy

        Parameters:
        policy_id (str): LQL Policy ID
        alert_enabled (bool): What to set for alert_enabled. Defaults to None (unchanged).

        Return:
        response (dict): requests json() object
        """
        policy_json = {'enabled': False}
        if alert_enabled in [True, False]:
            policy_json['alert_enabled'] = alert_enabled

        return self.update(policy_json, policy_id=policy_id)

    def enable(self, policy_id, alert_enabled=None):
        """
        Enable a LQL Policy

        Parameters:
        policy_id (str): LQL Policy ID
        alert_enabled (bool): What to set for alert_enabled. Defaults to None (unchanged).

        Return:
        response (dict): requests json() object
        """
        policy_json = {'enabled': True}
        if alert_enabled in [True, False]:
            policy_json['alert_enabled'] = alert_enabled

        return self.update(policy_json, policy_id=policy_id)

    def get(self, policy_id=None):
        """
        Get a LQL Policy or Policies

        If called without policy_id return all policies.
        Otherwise return specified policy.

        Parameters:
        policy_id (str): LQL Policy ID (optional)

        Return:
        response (dict): requests json() object
        """
        api_uri = self.lql_policies_base_uri

        if policy_id:
            api_uri += f'?{self.lql_policies_identifier_key}={quote(policy_id, safe="")}'

        response = self._session.get(api_uri)

        return response.json()

    def update(self, policy_json, policy_id=None):
        """
        Update a LQL Policy

        A LQL Policy ID is required to update LQL Policies

        The policy_id parameter is optional unless policy_id is
        not specified in the policy_json

        Parameters:
        policy_id (str): LQL Policy ID
        policy_json (dict): LQL Policy JSON
        smart (bool): Whether to update if policy already exists

        Return:
        response (dict): requests json() object
        """
        policy_id = policy_json['policy_id'] if 'policy_id' in policy_json else policy_id
        assert policy_id, 'Must specify a valid LQL Policy ID to update'

        api_uri = (
            f'{self.lql_policies_base_uri}'
            f'?{self.lql_policies_identifier_key}={quote(policy_id, safe="")}'
        )

        response = self._session.patch(api_uri, data=policy_json)

        return response.json()
