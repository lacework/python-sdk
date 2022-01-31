"""Various functions that are shared across features."""

import datetime
import os

import yaml
from IPython import get_ipython

from laceworkjupyter import utils as main_utils


def format_access_denied(event_value):
    """
    Creates a filter format string for a Yes No variable.

    :return: A string that can be used in a LQL filter.
    """
    if event_value.lower().startswith('y'):
        return "ERROR_CODE IN ('AccessDenied', 'Client.UnauthorizedOperation')"

    return "ERROR_CODE IS NULL"


def format_generic_string(event_value, attribute):
    """
    Creates a filter format string for a generic attribute.

    :param str event_value: String that is used to generate the filter string.
    :param str attribute: The attribute that is used in the filter.
    :return: A string that can be used in a LQL filter.
    """
    if event_value.lower() == "exists":
        return "{0:s} IS NOT NULL".format(attribute)

    if event_value.startswith("!"):
        return "{0:s} NOT LIKE '%{1:s}%'".format(attribute, event_value[1:])

    return "{0:s} LIKE '%{1:s}%'".format(attribute, event_value)


def format_generic_number(event_value, attribute):
    """
    Creates a filter format string for a generic number attribute.

    :param str event_value: String that is used to generate the filter string.
    :param str attribute: The attribute that is used in the filter.
    :return: A string that can be used in a LQL filter.
    """
    if event_value.isdigit():
        pre = "="

    if event_value.startswith("<"):
        event_value = event_value[1:]
        pre = "<="

    if event_value.startswith(">"):
        event_value = event_value[1:]
        pre = ">="

    return f"{attribute} {pre} {event_value}"


def load_yaml_file(rel_file_path):
    """
    Load a YAML file from features path and return a python object.

    :param str rel_file_path: The relative file path to the YAML file.
    :raises ValueError: If the path does not exist.
    :return: Returns the parsed YAML structure as a Python object.
    """
    feature_directory = os.path.dirname(__file__)
    yaml_path = os.path.join(feature_directory, rel_file_path)

    if not os.path.isfile(yaml_path):
        raise ValueError(
            "The YAML file '{0:s}' does not exist within the feature "
            "directory.".format(rel_file_path))

    with open(yaml_path, "r") as fh:
        return yaml.safe_load(fh)


def get_query_definition(table_name, filters):
    """
    Returns a dict with query defintion from a table name and fiters.

    :param str table_name: The name of the table as defined in the table
        definitions.
    :param dict filters: A dict with filter names as keys.
    :raises ValueError: If the table does not exist within the definitions.
    :return: A dict with four keys, table_name, evaluator_id, filters
        and return_fields.
    """
    tables = load_yaml_file("tables.yaml")
    table_filters = load_yaml_file("filters.yaml")

    table_dict = {}
    for table in tables:
        if table.get("display_name", "N/A") == table_name:
            table_dict = table
            break

    if not table:
        raise ValueError("No table with display_name: {0:s}".format(
            table_name))

    table_name = table_dict.get("name", "_")
    available_filters = [
        x for x in table_filters if table_name in x.get("tables", [])]
    filter_keys = list(filters.keys())
    filters_use = [
        x for x in available_filters if x.get("parameter") in filter_keys]

    filter_lines = []

    for filter_dict in filters_use:
        for parameter, value in filters.items():
            if filter_dict.get("parameter", "") != parameter:
                continue
            if "format_string" in filter_dict:
                filter_string = filter_dict.get("format_string").format(value)
            elif "callback" in filter_dict:
                fname = filter_dict.get("callback")
                callback_parameters = filter_dict.get(
                    "callback_parameters", {})
                callback_parameters["event_value"] = value

                fn = globals().get(fname)
                if fn:
                    filter_string = fn(**callback_parameters)
                else:
                    filter_string = value

            filter_lines.append(filter_string)

    return {
        "table_name": table_dict.get("name"),
        "filters": filter_lines,
        "evaluator_id": table_dict.get("evaluator_id"),
        "return_fields": table_dict.get("return_fields", [])
    }


def build_lql_query(query_name, query_dict, join_support=True):  # noqa: C901
    """
    Build a LQL query and return evaluator ID and the query.

    :param str query_name: The name of the LQL query.
    :param dict query_dict: A dict with three keys, table_name,
        filters and return_fields.
    :param bool join_support: Indicates whether we should consider
        join operations if the table is supported for JOIN. Optional
        and defaults to True.
    :return: A string with the LQL query.
    """
    lql_name = query_dict.get("table_name", "NOTABLE")
    filter_lines = query_dict.get("filters", [])
    return_fields = query_dict.get("return_fields", [])

    join = False
    join_dict = {}
    join_tables = load_yaml_file("join.yaml")
    for join_table in join_tables:
        if lql_name in join_table.get("to", []):
            join_dict = join_table
            break

    if join_support and bool(join_dict):
        join = True

    query_lines = [f"Lacebook_Hunt_{query_name}"]
    query_lines.append("{\n  SOURCE {")
    if join:
        table_pieces = lql_name.split('_')
        if len(table_pieces) == 3:
            table_alias = table_pieces[-1].lower()
        elif len(table_pieces) > 3:
            table_alias = table_pieces[-2].lower()
        else:
            table_alias = 'pre'

        join_table = join_dict.get("from", "")
        join_alias = join_dict.get("alias", "post")
        query_lines.append(
            f"    {lql_name} {table_alias} WITH {join_table} {join_alias}")
    else:
        query_lines.append(f"    {lql_name}")

    query_lines.append("  }")
    query_lines.append("  FILTER {")

    if join:
        for index, filter_line in enumerate(filter_lines):
            filter_lines[index] = f"{table_alias}.{filter_line}"

    filter_lines[0] = f"     {filter_lines[0]}"
    query_lines.append("\n    AND ".join(filter_lines))
    query_lines.append("  }")
    query_lines.append("  RETURN DISTINCT {")

    if join:
        for index, return_field in enumerate(return_fields):
            return_fields[index] = f"{table_alias}.{return_field}"

        join_fields = join_dict.get("return_fields", [])
        return_fields.extend([f"{join_alias}.{x}" for x in join_fields])

    return_fields[0] = f"     {return_fields[0]}"
    query_lines.append(",\n     ".join(return_fields))
    query_lines.append("  }\n}")

    return "\n".join(query_lines)


def write_to_namespace(key, value):
    """
    Write a variable to the global namespace.

    :params str key: The name of the namespace variable.
    :params obj value: The value to store in the namespace.
    """
    ip = get_ipython()

    if ip and key:
        ip.push({key: value})


def get_start_and_end_time(ctx):
    """
    Return start and end time from cache.

    This function returns the currently stored start and end time
    in the cache. If there aren't any values stored in the cache
    the values for last two days are returned.

    :return: A tuple, with two strings, start and end time.
    """
    start_time = ctx.get("start_time")
    end_time = ctx.get("end_time")

    if not (start_time and end_time):
        start_time, end_time = main_utils.parse_date_offset('LAST 2 DAYS')

    start_time, _, _ = start_time.partition('.')
    start_time = f'{start_time}Z'

    end_time, _, _ = end_time.partition('.')
    end_time = f'{end_time}Z'

    return start_time, end_time


def get_times_from_widgets(ctx):
    """
    Returns start and end times read from widgets.

    :raises ValuError: If the timestamps are wrongly formatted.
    :return: A tuple with two entries, start and end time.
    """
    start_widget = ctx.get_state(
        state="query_builder", key="query_start_widget")
    start_time = start_widget.value

    end_widget = ctx.get_state(state="query_builder", key="query_end_widget")
    end_time = end_widget.value

    if not (start_time and end_time):
        start_time, end_time = get_start_and_end_time(ctx)

    start_time = start_time.upper()
    if not start_time.endswith('Z'):
        start_time = f'{start_time}Z'

    try:
        _ = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as err:
        raise ValueError(
            "Unable to verify the end time (remember it should be entered "
            "in the format 'YYYY-MM-DDTHH:MM:SSZ' ({0:s}) - {1}".format(
                start_time, err))

    end_time = end_time.upper()
    if not end_time.endswith('Z'):
        end_time = f'{end_time}Z'

    try:
        _ = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as err:
        raise ValueError(
            "Unable to verify the end time (remember it should be entered "
            "in the format 'YYYY-MM-DDTHH:MM:SSZ' ({0:s}) - {1}".format(
                start_time, err))

    return start_time, end_time
