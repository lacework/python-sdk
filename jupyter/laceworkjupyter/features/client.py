"""A simple class that contains Lacework API related features."""

import datetime

import pandas as pd

from laceworkjupyter import helper
from laceworkjupyter import manager


DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


@manager.register_feature
def get_client(
        api_key=None, api_secret=None, account=None,
        subaccount=None, instance=None, base_domain=None,
        profile=None, ctx=None):
    """
    Returns a Lacework API client for use in a notebook.

    :return: An instance of a LaceworkJupyterClient.
    """

    client = helper.LaceworkJupyterClient(
        api_key=api_key, api_secret=api_secret, account=account,
        subaccount=subaccount, instance=instance, base_domain=base_domain,
        profile=profile)

    ctx.set_client(client)
    return client


@manager.register_feature
def get_events_from_alert(alert_id, client=None, ctx=None):
    """
    Return a data frame with the attached events from a single alert.

    :param str alert_id: The ID of the alert.
    :param client: Optional client object, defaults to using the client
        that is stored in the context, or by fetching a default client.
    :return: A pandas DataFrame with the evidence associated with the event.
    """
    if not client:
        if ctx:
            client = ctx.client
        if not client:
            client = get_client()

    return client.alerts.get_details(alert_id, scope='Events')
