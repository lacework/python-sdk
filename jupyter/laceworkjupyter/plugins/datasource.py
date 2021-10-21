"""An output plugin for the Lacework DataSource API."""


import pandas as pd


def process_list_data_sources(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    lines = [{'name': x, 'description': y} for x, y in data]
    return pd.DataFrame(lines)


def process_datasource_schema(data):
    """
    Returns a Pandas DataFrame from the output of the API call.

    :return: A pandas DataFrame.
    """
    data_dict = data.get('data', {})
    schemas = data_dict.get('resultSchema', [])

    return pd.DataFrame(schemas)
