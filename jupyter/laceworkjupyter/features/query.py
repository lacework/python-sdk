"""
Provides a quick access to predefined LQL queries.
"""
import os

import yaml
import pandas as pd

from laceworkjupyter import manager
from laceworkjupyter import utils


def _get_arguments(days=0, start_time="", end_time=""):
    """
    Returns an argument dict for LQL queries.

    :param int days: Optional number of days from today.
    :param str start_time: Start date in an ISO format.
    :param str end_tune: End date in an ISO format.
    :return: A dict with arguments that can be passed on to a LQL query API.
    """
    if days:
        start_time, end_time = utils.parse_date_offset(f"LAST {days} DAYS")

        start_time, _, _ = start_time.partition(".")
        start_time = f"{start_time}Z"

        end_time, _, _ = end_time.partition(".")
        end_time = f"{end_time}Z"

    return {
        "StartTimeRange": start_time,
        "EndTimeRange": end_time,
    }


def _run_query(query, arguments, evaluator=None, ctx=None):
    """
    Runs a LQL query and returns a dataframe with the results.

    :param str query: The LQL query to run.
    :param dict arguments: A dict containing the arguments to send to the LQL
        evaluator.
    :param str evaluator: Optional string with an evaluator ID.
    :param obj ctx: An optional Lacework context object.
    :return: A pandas DataFrame with the results from the query.
    """
    if not ctx:
        raise ValueError("Unable to run query, no context available.")

    client = ctx.client
    if not client:
        raise ValueError("Unable to run query, no client set.")

    return client.queries.execute(
        evaluator_id=evaluator, query_text=query, arguments=arguments)


def _get_help_frame(parameters):
    """
    Returns a dataframe with the parameters for the query function.

    :param list parameters: A list of dictionaries with the required extra
        parameters the function requries.
    :return: A dataframe with all the parameters listed.
    """
    new_list = parameters.copy()
    for parameter in new_list:
        parameter["required"] = True
        parameter["note"] = "For replacing values in the query itself."

    new_list.append({
        "name": "days",
        "type": "int",
        "required": False,
        "note": (
            "Number of days to search back in time, end day is now. "
            "Required to either provide days or both start and end time.")
    })

    new_list.append({
        "name": "start_time",
        "type": "str",
        "required": False,
        "note": "Start time expressed as an ISO formatted string."
    })
    new_list.append({
        "name": "end_time",
        "type": "str",
        "required": False,
        "note": "End time expressed as an ISO formatted string."
    })

    return pd.DataFrame(new_list)


def _query_function(query_dict):
    """
    Generates a function to query LQL from a query dictionary.

    :param dict query_dict: A dictionary that contains the query as well
        as additional parameters.

    :return: A function that can be used to generate a LQL query.
    """
    def wrapper(
            days=0, start_time="", end_time="", ctx=None,
            help=False, **kwargs):
        """
        Query LQL and return back a DataFrame with the discovered content.

        :param int days: Number of days to query back in time.
        :param str start_time: ISO formatted timestamp of the start time of
            the query. Optional and not needed if days is defined.
        :param str end_time: ISO formatted timestamp of the end time of
            the query. Optional and not needed if days is defined.
        :param bool help: Defaults to False, if set to True the query
            is not run and a dataframe with the parameters required is
            returned back.
        :param dict kwargs: Optional parameters that depend on each
            specific search query. To understand what parameters are
            required to be passed on for each query function call
            the function with just the parameter help=True.
        """
        query = query_dict.get("query", "")
        if not query:
            raise ValueError("There is no query defined.")

        params = query_dict.get("params", [])
        if help:
            return _get_help_frame(params)

        if not days and not (start_time and end_time):
            raise ValueError(
                "The parameters days, or both start_time and end_time need "
                "to be defined.")

        param_dict = {}
        for parameter in params:
            # TODO: Add type checking.
            param_name = parameter.get("name", "__not_exists__")
            if param_name not in kwargs:
                raise ValueError(
                    "Unable to run, missing parameter: {0:s}".format(
                        param_name))
            param_dict[param_name] = kwargs.get(param_name)

        # Prepare the query for format strings.
        query = query.replace("{", "{{").replace("}", "}}")
        query = query.replace("<<", "{").replace(">>", "}")
        query = query.format(**param_dict)
        query = query.replace("{{", "{").replace("}}", "}")

        arguments = _get_arguments(
            days=days, start_time=start_time, end_time=end_time)
        evaluator = query_dict.get("evaluator")

        return _run_query(
            query=query, evaluator=evaluator,
            arguments=arguments, ctx=ctx)
    return wrapper


query_feature_directory = os.path.dirname(__file__)
query_yaml_path = os.path.join(query_feature_directory, "query.yaml")

if os.path.isfile(query_yaml_path):
    with open(query_yaml_path, "r") as fh:
        data = yaml.safe_load(fh)
        for query_dict in data.get("queries", []):
            name = query_dict.get("name", "")
            function_name = f"query_{name}"
            function_fn = _query_function(query_dict)

            manager.LaceworkManager.add_feature(function_fn, function_name)
