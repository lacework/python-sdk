"""Various functions that are shared across features."""

import os

import yaml
from IPython import get_ipython


def _format_generic_string(event_value, attribute):
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


def format_event_name(event_value):
    """
    Creates a filter format string for event names.

    :param str event_value: String that is used to generate the filter string.
    :return: A string that can be used in a LQL filter.
    """
    return _format_generic_string(event_value, "EVENT_NAME")


def format_event_type(event_value):
    """
    Creates a filter format string for event type.

    :param str event_value: String that is used to generate the filter string.
    :return: A string that can be used in a LQL filter.
    """
    return _format_generic_string(event_value, "EVENT:eventType::String")


def format_event_source(event_value):
    """
    Creates a filter format string for event sources.

    :param str event_value: String that is used to generate the filter string.
    :return: A string that can be used in a LQL filter.
    """
    return _format_generic_string(event_value, "EVENT_SOURCE")


def format_event_region(event_value):
    """
    Creates a filter format string for event region.

    :param str event_value: String that is used to generate the filter string.
    :return: A string that can be used in a LQL filter.
    """
    return _format_generic_string(event_value, "EVENT:awsRegion")


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


def build_lql_query(table_name, filters):
    """
    Build a LQL query and return evaluator ID and the query.

    :param str table_name: The
    :rasise ValueError: If the table does not exist within the definitions.
    :return:
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

    available_filters = [
        x for x in table_filters if x.get("table", "") == table_dict.get(
            "name", "_")]
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
                fn = locals().get(fname)
                if fn:
                    filter_string = fn(value)
                else:
                    filter_string = value

            filter_lines.append(filter_string)

    lql_name = table_dict.get("name")
    query_name = table_name.replace(" ", "_")

    query_lines = [f"Lacebook_{query_name}"]
    query_lines.append("{\n  SOURCE {")
    query_lines.append(f"    {lql_name}")
    query_lines.append("  }")
    query_lines.append("  FILTER {")
    query_lines.append("\n    AND ".join(filter_lines))
    query_lines.append("  }")
    query_lines.append("  RETURN DISTINCT {")
    query_lines.append(",\n     ".join(table_dict.get("return_fields", [])))
    query_lines.append("  }\n}")

    return table_dict.get("evaluator_id"), "\n".join(query_lines)


def write_to_namespace(key, value):
    """
    Write a variable to the global namespace.

    :params str key: The name of the namespace variable.
    :params obj value: The value to store in the namespace.
    """
    ip = get_ipython()

    if ip and key:
        ip.push({key: value})
