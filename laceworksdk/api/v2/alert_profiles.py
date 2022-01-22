# -*- coding: utf-8 -*-
"""
Lacework AlertProfiles API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class AlertProfilesAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the AlertProfilesAPI object.

        :param session: An instance of the HttpSession class

        :return AlertProfilesAPI object.
        """

        super().__init__(session, "AlertProfiles")

    def create(self,
               alert_profile_id,
               alerts,
               extends,
               **request_params):
        """
        A method to create a new AlertProfiles object.

        :param alert_profile_id: A string representing the id of the object.
        :param alerts: A list of objects containing alert details for the parent object.
            obj:
                :param name: A string representing the name of the alert.
                :param eventName: A string representing the name to show in Event Triage.
                :param description: A string representing the description to show in Event Triage.
                :param subject: A string representing the subject to show in the Event Dossier.
        :param extends: A string representing the base alert profile object.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            alert_profile_id=alert_profile_id,
            alerts=alerts,
            extends=extends,
            **request_params
        )

    def get(self,
            id=None):
        """
        A method to get AlertProfiles objects.

        :param id: A string representing the object ID.

        :return response json
        """

        return super().get(id=id)

    def get_by_id(self,
                  id):
        """
        A method to get an AlertProfiles object by ID.

        :param id: A string representing the object ID.

        :return response json
        """

        return self.get(id=id)

    def search(self, **request_params):
        """
        A method to 'pass' when attempting to search AlertProfiles objects.

        Search functionality is not yet implemented for Alert Profiles.
        """
        pass

    def update(self,
               id,
               alerts=None,
               **request_params):
        """
        A method to update an AlertProfiles object.

        :param id: A string representing the object ID.
        :param alerts: A list of objects containing alert details for the parent object.
            obj:
                :param name: A string representing the name of the alert.
                :param eventName: A string representing the name to show in Event Triage.
                :param description: A string representing the description to show in Event Triage.
                :param subject: A string representing the subject to show in the Event Dossier.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().update(
            id=id,
            alerts=alerts,
            **request_params
        )

    def delete(self,
               id):
        """
        A method to delete an AlertProfiles object.

        :param guid: A string representing the object ID.

        :return response json
        """

        return super().delete(id=id)
