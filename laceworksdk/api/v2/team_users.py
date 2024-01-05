# -*- coding: utf-8 -*-
"""Lacework TeamUsers API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint
import logging

logger = logging.getLogger(__name__)


class TeamUsersAPI(CrudEndpoint):
    """A class used to represent the `Team Users API endpoint <https://docs.lacework.net/api/v2/docs/#tag/TeamUsers>`_ .

    The Team Users API works with the new Lacework role-based access control (RBAC) model. After you enable RBAC in the \
    Lacework Console, the Team Users API is available and the legacy Team Members API (deprecated) is disabled.
    """

    def __init__(self, session):
        """Initializes the TeamUsersAPI object.

        Args:
          session(HttpSession): An instance of the HttpSession class

        Returns:
            TeamUsersAPI: An instance of this class
        """
        super().__init__(session, "TeamUsers")


    def get(self, guid=None):
        """(Experimental API) A method to get team users. Using no args will get all team users.

        Args:
          guid (str, optional): The GUID of the team user to get.

        Returns:
            dict: The requested team user(s)

        """
        return super().get(id=guid)

    def get_by_guid(self, guid):
        """(Experimental API) A method to get a TeamUsers object by GUID.

        Args:
          guid (str): The GUID of the team user to get.

        Returns:
            dict: The requested team user(s)

        """
        return self.get(guid=guid)

    def create(
        self,
        name,
        email=None,
        company=None,
        description=None,
        user_enabled=True,
        type="StandardUser",
        **request_params,
    ):
        """A method to create a new team users standard user object.

        Args:
          name (str): The friendly name of the user.
          email (str): The email address of the user (valid only for type=StandardUser).
          company (str): The company of the user (valid only for type=StandardUser).
          description (str): A description text for describing service accounts (valid only for ServiceUser)
          user_enabled (bool|int, optional): Whether the new team user is enabled.
          type (str, optional): The type of the user to create. Valid values: "StandardUser", "ServiceUser" \
          (Default value = "StandardUser")
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The newly created team user
        """

        return super().create(
            name=name,
            email=email,
            description=description,
            company=company,
            user_enabled=int(bool(user_enabled)),
            type=type,
            **request_params,
        )

    def update(
        self, guid, name=None, user_enabled=None, description=None, **request_params
    ):
        """(Experimental API) A method to update a TeamUsers object.

        Args:
          guid (str): The GUID of the team user to update
          name (str): The friendly name of the user.
          user_enabled (bool|int, optional): Whether the new team user is enabled.
          description (str): A description text for describing service accounts (valid only for ServiceUser).
          request_params (dict, optional): Use to pass any additional parameters the API


        Returns:
            dict: The newly created team user

        """
        if user_enabled is not None:
            user_enabled = int(bool(user_enabled))

        return super().update(
            id=guid,
            name=name,
            user_enabled=user_enabled,
            description=description,
            **request_params,
        )

    def delete(self, guid):
        """A method to delete a team user.

        Args:
          guid (str): The GUID of the team user to delete

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=guid)
