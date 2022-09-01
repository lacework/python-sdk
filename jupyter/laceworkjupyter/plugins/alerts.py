"""An output plugin for the Lacework Alerts API."""


import pandas as pd


def process_alerts(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    data_dicts = data.get("data", [])
    lines = []
    for data_dict in data_dicts:
        info = data_dict.pop("alertInfo", {})
        # Add Prefix.
        new_info = {
            f"info{key.capitalize()}": value for key, value in info.items()}
        data_dict.update(new_info)
        lines.append(data_dict)
    return pd.DataFrame(lines)
