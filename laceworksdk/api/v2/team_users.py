# -*- coding: utf-8 -*-
"""
Lacework TeamUsers API wrapper (Experimental).
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint
import logging
logger = logging.getLogger(__name__)

class TeamUsersAPI(CrudEndpoint):
    def __init__(self, session):
        super().__init__(session, "TeamUsers")

    def get(self, guid=None):
        """
        (Experimental API) A method to get TeamUsers objects.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().get(id=guid)

    def get_by_guid(self, guid):
        """
        (Experimental API) A method to get a TeamUsers object by GUID.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return self.get(guid=guid)

    def create(self,
               name,
               email=None,
               company=None,
               description=None,
               type="StandardUser",
               **request_params):
        """
        (Experimental API) A method to create a new TeamUsers standard user object.

        :param name: A string representing the friendly name of the user.
        :param email: A string representing the email address of the user (valid only for StandardUser).
        :param company: A string representing the company of the user (valid only for StandardUser).
        :param description: A description text for describing service accounts (valid only for ServiceUser).
        :param type: A string representing the type of the user to create.
            (StandardUser or ServiceUser)
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            name=name,
            email=email,
            description=description,
            company=company,
            type=type,
            **request_params
        )

    def update(self,
               guid,
               name=None,
               user_enabled=None,
               description=None,
               **request_params):
        """
        (Experimental API) A method to update a TeamUsers object.

        :param guid: A string representing the object GUID.
        :param name: A string representing the friendly name of the object.
        :param userEnabled: A boolean/integer representing whether the object is enabled.
            (0 or 1)
        :param description: A description text for describing service accounts (only valid for service accounts).

        :return response json
        """

        if user_enabled is not None:
            user_enabled = int(bool(user_enabled))

        return super().update(
            id=guid,
            name=name,
            user_enabled=user_enabled,
            description=description,
            **request_params
        )

    def delete(self, guid):
        """
        (Experimental API) A method to delete a TeamUsers object.

        :param guid: A string representing the object GUID.

        :return response json
        """

        return super().delete(id=guid)
