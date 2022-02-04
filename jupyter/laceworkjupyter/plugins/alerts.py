"""An output plugin for the Lacework Alerts API."""


import pandas as pd

from laceworkjupyter.features import helper


def process_alerts(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    data_dicts = data.get("data", [])
    lines = []
    for data_dict in data_dicts:
        data_dict["alertDescription"] = helper.extract_json_field(
            data_dict.get("alertProps", {}), "description.descriptionId")

        description_dict = helper.extract_json_field(
            data_dict.get("alertProps", {}), "description.descriptionObj")
        data_dict.update(description_dict)

        alert_context = helper.extract_json_field(
            data_dict.get("keys", {}), "src.keys.alert")
        if alert_context:
            data_dict.update(alert_context)

        lines.append(data_dict)
    return pd.DataFrame(lines)
