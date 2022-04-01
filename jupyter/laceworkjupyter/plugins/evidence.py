"""An output plugin for the Lacework Evidence API."""

import pandas as pd

from laceworkjupyter.plugins import utils


def process_evidence_search(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    lines = []
    for data_dict in utils.get_data_dicts(data):
        src_event = data_dict.pop('srcEvent', {})
        event = src_event.pop('event', {})

        data_dict.update(src_event)
        data_dict.update(event)

        lines.append(data_dict)
    return pd.DataFrame(lines)
