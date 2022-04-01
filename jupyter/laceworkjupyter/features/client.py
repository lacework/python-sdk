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
def get_evidence_from_event_id(event_id, client=None, minutes=10, ctx=None):
    """
    Return a data frame with the attached evidence from a single event.

    :param str event_id: The ID of the event.
    :param client: Optional client object, defaults to using the client
        that is stored in the context, or by fetching a default client.
    :param int minutes: Optional number of minutes around the event
        to gather the evidence details, defaults to 10 minutes.
    :return: A pandas DataFrame with the evidence associated with the event.
    """
    if not client:
        if ctx:
            client = ctx.client
        if not client:
            client = get_client()

    events = client.events.get_details(event_id)

    if events.empty:
        return pd.DataFrame()

    event = events.iloc[0]
    start_time = datetime.datetime.strptime(event.START_TIME, DATE_FORMAT)
    end_time = datetime.datetime.strptime(event.END_TIME, DATE_FORMAT)

    time_delta = datetime.timedelta(minutes=minutes)

    start_time -= time_delta
    end_time += time_delta

    search_filter = {
        'timeFilter': {
            'startTime': start_time.strftime(DATE_FORMAT),
            'endTime': end_time.strftime(DATE_FORMAT)
        },
        'filters': [{
            'field': 'id',
            'expression': 'eq',
            'value': event_id
        }],
    }
    return client.evidence.search(json=search_filter)
