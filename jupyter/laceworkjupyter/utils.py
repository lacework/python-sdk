import datetime
import logging

import pandas as pd

from . import config


logger = logging.getLogger('lacework_sdk.jupyter.utils')


def dataframe_decorator(function):
    """
    A decorator used to convert Lacework JSON API output into a dataframe.
    """
    def get_output(*args, **kwargs):
        data = function(*args, **kwargs)

        if isinstance(data, dict):
            df = pd.DataFrame(data.get('data', []))
            if 'SEVERITY' in df:
                df['SEVERITY'] = df.SEVERITY.apply(
                    lambda x: config.SEVERITY_DICT.get(x, x))
            return df

        return data

    return get_output


def flatten_json_output(json_data, pre_key=''):
    """
    Flatten and return a dict from a Lacework JSON structure.

    :param dict json_data: A JSON dict object.
    :param str pre_key: Optional string with the key path into the JSON object.
    :return: A dict with all elements of the JSON structure flattened.
    """
    flattened_data = {}

    for key, value in json_data.items():
        if pre_key:
            use_key = f'{pre_key}.{key}'
        else:
            use_key = key

        if isinstance(value, dict):
            new_dict = flatten_json_output(value, pre_key=use_key)
            flattened_data.update(new_dict)

        elif isinstance(value, list):
            count = 1
            for list_value in value:
                if isinstance(list_value, dict):
                    new_dict = flatten_json_output(
                        list_value, pre_key=f'{use_key}_{count}')
                    flattened_data.update(new_dict)
                else:
                    flattened_data[f'{use_key}_{count}'] = list_value
                count += 1

        else:
            flattened_data[use_key] = value

    return flattened_data


def flatten_data_frame(data_frame):
    """
    Flatten a DataFrame that contains nested dicts in columns.

    Be careful using this function on a larger data frames since this
    is a slow flattening process.

    :param DataFrame data_frame: The data frame to flatten.
    :return: A DataFrame that is flattened.
    """
    rows = []
    for _, row in data_frame.iterrows():
        rows.append(flatten_json_output(row.to_dict()))

    return pd.DataFrame(rows)


def parse_date_offset(offset_string):
    """
    Parse date offset string and return a start and end time.

    :param str offset_string: The offset string describing the time period.
    :raises ValueError: If not able to convert the string to dates.
    :return: A tuple with start and end time as ISO 8601 formatted strings.
    """
    string = offset_string.lower()
    if not string.startswith('last'):
        raise ValueError('Offset string needs to start with LAST to be valid')

    end_time_object = datetime.datetime.utcnow()
    end_time = end_time_object.isoformat()

    items = string.split()
    if len(items) != 3:
        raise ValueError(
            'Offset string needs to be three words, '
            '"LAST X SECONDS/MINUTES/HOURS/DAYS"')

    try:
        quantity = int(items[1], 10)
    except ValueError:
        raise ValueError(
            'Offset string needs to have a valid integer as '
            'the second word.')

    unit = items[2]
    time_delta = None
    if unit.startswith('minute'):
        time_delta = datetime.timedelta(minutes=quantity)
    elif unit.startswith('hour'):
        time_delta = datetime.timedelta(hours=quantity)
    elif unit.startswith('day'):
        time_delta = datetime.timedelta(days=quantity)
    elif unit.startswith('week'):
        time_delta = datetime.timedelta(weeks=quantity)
    elif unit.startswith('second'):
        time_delta = datetime.timedelta(seconds=quantity)

    if not time_delta:
        raise ValueError('Unable to determine the time delta')

    start_time_object = end_time_object - time_delta
    start_time = start_time_object.isoformat()

    return start_time, end_time
