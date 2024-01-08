# -*- coding: utf-8 -*-
"""Lacework AlertProfiles API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertProfilesAPI(CrudEndpoint):
    """A class used to represent the `Alert Profiles API endpoint <https://docs.lacework.net/api/v2/docs/#tag/AlertProfiles>`_

    An alert profile is a set of metadata that defines how your LQL queries get consumed into events and alerts.
    """

    def __init__(self, session):
        """Initializes the AlertProfilesAPI object.

        Args:
            session (HttpSession): An instance of the HttpSession class

        Returns:
            AlertProfilesAPI: returns an AlertProfilesAPI object
        """
        super().__init__(session, "AlertProfiles")

    def create(self, alert_profile_id, alerts, extends, **request_params):
        """A method to create a new AlertProfiles object.

        Args:
          alert_profile_id (str): A unique ID to name the new alert profile
          extends (str):The base alert profile object.
          alerts (list of dict): A list of dictionaries containing alert details to create. Alert fields are:

              - name (str): The name of the alert.
              - eventName (str): The name to show in Event Triage.
              - description (str): The description to show in Event Triage.
              - subject (str): The subject to show in the Event Dossier.

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: A JSON object containing the created Alert Profile

        """
        return super().create(
            alert_profile_id=alert_profile_id,
            alerts=alerts,
            extends=extends,
            **request_params,
        )

    def get(self, id=None):
        """A method to get AlertProfiles objects.

        Args:
          id (str): A string representing the alert profile ID.

        Returns:
            dict: The returned alert profile(s)
        """
        return super().get(id=id)

    def get_by_id(self, id):
        """A method to get an AlertProfiles object by ID.

        Args:
          id (str): A string representing the alert profile ID.

        Returns:
            dict: The returned alert profile(s)
        """
        return self.get(id=id)

    def search(self, **request_params):
        """
        Search functionality is not yet implemented for Alert Profiles.
        """
        pass

    def update(self, id, alerts=None, **request_params):
        """A method to update an AlertProfiles object.

        Args:
          id (str): A string representing the object ID.
          alerts (list of dicts): A list of dictionaries containing alert details to update. Alert fields are:

              - name (str): The name of the alert.
              - eventName (str): The name to show in Event Triage.
              - description (str): The description to show in Event Triage.
              - subject (str): The subject to show in the Event Dossier.

          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated Alert Profile
        """
        return super().update(id=id, alerts=alerts, **request_params)

    def delete(self, id):
        """A method to delete an AlertProfiles object.

        Args:
            id (str): A string representing the alert profile ID.

        Returns:
            requests.models.Response: a Requests response object containing the response code
        """
        return super().delete(id=id)
