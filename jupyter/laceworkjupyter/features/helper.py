"""
File that contains data frame helpers for the Lacework notebook environment.
"""

import json
import logging

import pandas as pd
import numpy as np

from laceworkjupyter import manager


logger = logging.getLogger("lacework_sdk.jupyter.feature.helper")


@manager.register_feature
def deep_extract_field(data_frame, column, field_string, ctx=None):
    """
    Extract a field from a JSON struct inside a DataFrame.

    Usage example:
        df['hostname'] = lw.deep_extract_field(
            df, 'properties', 'host.hostname')

    :param DataFrame data_frame: The data frame to extract from.
    :param str column: The name of the column that contains the JSON struct.
    :param str field_string: String that contains the field to extract from,
        this is a dot delimited string, eg: key.foo.bar, that will extract
        a value from {'key': 'foo': {'bar': 'value'}}.
    :param obj ctx: The context object.
    :return: A pandas Series with the extracted value.
    """
    def _extract_function(json_obj, item):
        if isinstance(json_obj, str):
            try:
                json_obj = json.loads(json_obj)
            except json.JSONDecodeError:
                logger.error("Unable to decode JSON string: %s", json_obj)
                return np.nan

        if not isinstance(json_obj, dict):
            logger.error("Unable to extract, not a dict: %s", type(json_obj))
            return np.nan

        data = json_obj
        for point in item.split("."):
            if not isinstance(data, dict):
                logger.error(
                    "Sub-item %s is not a dict (%s)", point, type(data))
                return np.nan

            data = data.get(point)
        return data

    if column not in data_frame:
        logger.error("Column does not exist in the dataframe.")
        return pd.Series()

    return data_frame[column].apply(
        lambda x: _extract_function(x, field_string))
