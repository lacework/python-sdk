"""An output plugin for the Lacework Events API."""


import pandas as pd


def process_event_details(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    data_dicts = data.get("data", [])
    lines = []
    for data_dict in data_dicts:
        entity_map = data_dict.pop('ENTITY_MAP', {})
        data_dict.update(entity_map)
        lines.append(data_dict)
    return pd.DataFrame(lines)
