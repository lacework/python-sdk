# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


def standard_user_example(client: LaceworkClient):
    """
    Example of create/update/delete and group management for standard user
    """

    # Create user
    data = client.team_users.create("test user", "noreply@lacework.com", "test-company")
    guid = data["data"]["userGuid"]
    logging.debug(f'user guid created:\n{guid}')

    # Get one user
    client.team_users.get(guid)

    # Update user
    client.team_users.update(guid, user_enabled=0)

    # Add user to group
    client.user_groups.add_users("LACEWORK_USER_GROUP_POWER_USER", [guid])

    # Remove user from group
    client.user_groups.remove_users("LACEWORK_USER_GROUP_POWER_USER", [guid])

    # Delete user
    client.team_users.delete(guid)

def service_user_example(client: LaceworkClient):
    """
    Example of create/update/delete and group management for service user
    """

    # Create user
    data = client.team_users.create("test service user", description="test service user", type="ServiceUser")
    guid = data["data"]["userGuid"]
    logging.debug(f'user guid created:\n{guid}')

    # Get one user
    client.team_users.get(guid)

    # Update user
    client.team_users.update(guid, user_enabled=0)

    # Add user to group
    client.user_groups.add_users("LACEWORK_USER_GROUP_POWER_USER", [guid])

    # Remove user from group
    client.user_groups.remove_users("LACEWORK_USER_GROUP_POWER_USER", [guid])

    # Delete user
    client.team_users.delete(guid)



if __name__ == "__main__":
    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # TeamUsers API

    # Get users
    lacework_client.team_users.get()

    standard_user_example(lacework_client)
    service_user_example(lacework_client)

