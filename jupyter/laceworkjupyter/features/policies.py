"""Simple file to list and execute LQL policies."""

import logging

import pandas as pd

from laceworksdk import http_session
from laceworkjupyter import manager
from laceworkjupyter.features import utils


logger = logging.getLogger("lacework_sdk.jupyter.feature.policies")


@manager.register_feature
def list_available_queries(ctx=None):
    """
    Returns a DataFrame with the available LQL queries.

    :return: Pandas DataFrame with available LQL quries.
    """
    return ctx.client.queries.get()


@manager.register_feature
def query_stored_lql(query_id, start_time="", end_time="", ctx=None):
    """
    Returns the results from running a LQL query.

    This is a simple feature that simply exposes the ability of the client
    to run stored LQL queries.

    :param str query_id: The ID of the query.
    :param str start_time: ISO formatted start time, if not provided defaults
        to two days ago.
    :param str end_time: ISO formatted end time. If not provided defaults
        to current time.
    :param obj ctx: The Lacework context object.
    :return: Returns a pandas DataFrame with the results of running the query.
    """
    client = ctx.client

    try:
        _ = client.sdk.queries.get_by_id(query_id)
    except http_session.ApiError as err:
        logger.error("Query ID not found: {}".format(err))
        return pd.DataFrame()

    default_start_time, default_end_time = utils.get_start_and_end_time(ctx)
    if not start_time:
        start_time = default_start_time

    if not end_time:
        end_time = default_end_time

    arguments = {
        "StartTimeRange": start_time,
        "EndTimeRange": end_time
    }

    return client.queries.execute_by_id(
        query_id=query_id, arguments=arguments)
