"""An output plugin for the Lacework Alert Rules API."""


import pandas as pd


def process_alert_rules(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    data_dicts = data.get("data", [])
    lines = []
    for data_dict in data_dicts:
        filter_dict = data_dict.get("filters", {})
        filter_dict["mcGuid"] = data_dict.get("mcGuid")
        filter_dict["intgGuidList"] = data_dict.get("intgGuidList")
        filter_dict["type"] = data_dict.get("type")
        lines.append(filter_dict)
    return pd.DataFrame(lines)
