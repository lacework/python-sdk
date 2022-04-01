"""
Simple utility class for the helper plugins.
"""


def get_data_dicts(data):
    """
    Yields data dicts from data input.
    """
    if isinstance(data, dict):
        for data_dict in data.get("data", []):
            yield data_dict
    else:
        for data_item in data:
            for data_dict in data_item.get("data", []):
                if isinstance(data_dict, dict):
                    yield data_dict
