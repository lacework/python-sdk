import datetime
import functools
import itertools
import logging

import pandas as pd

from . import config


logger = logging.getLogger('lacework_sdk.jupyter.utils')


def dataframe_decorator(function):
    """
    A decorator used to convert Lacework JSON API output into a dataframe.
    """
    @functools.wraps(function)
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


def flatten_json_output(  # noqa: C901
        json_data, pre_key='', lists_to_rows=False):
    """
    Flatten and yield dict objects from a Lacework JSON structure.

    :param dict json_data: A JSON dict object.
    :param str pre_key: Optional string with the key path into the JSON object.
    :param lists_to_rows bool: Determines whether values in lists get expanded
            into column_1, column_2, ..., column_2 or if it gets expanded
            into multiple rows (defaults to column_N, set to True to expand
            to rows).
    :yields: A dict with all elements of the JSON structure flattened.
    """
    flattened_data = {}
    data_to_list = {}

    for key, value in json_data.items():
        if pre_key:
            use_key = f'{pre_key}.{key}'
        else:
            use_key = key

        if isinstance(value, dict):
            new_dicts = flatten_json_output(
                value, pre_key=use_key, lists_to_rows=lists_to_rows)
            for new_dict in new_dicts:
                flattened_data.update(new_dict)

        elif isinstance(value, list):
            count = 1
            for list_value in value:
                if lists_to_rows:
                    list_key = use_key
                else:
                    list_key = f'{use_key}_{count}'

                if isinstance(list_value, dict):
                    new_dicts = flatten_json_output(
                        list_value, pre_key=list_key,
                        lists_to_rows=lists_to_rows)

                    for new_dict in new_dicts:
                        if lists_to_rows:
                            data_to_list.setdefault(list_key, [])
                            data_to_list[list_key].append(new_dict)
                        else:
                            flattened_data.update(new_dict)
                else:
                    flattened_data[list_key] = list_value
                count += 1

        else:
            flattened_data[use_key] = value

    if lists_to_rows:
        if data_to_list:
            keys, values = zip(*data_to_list.items())
            expanded_dicts = [
                dict(zip(keys, v)) for v in itertools.product(*values)]

            for expanded_dict in expanded_dicts:
                new_dict = flattened_data.copy()
                for dict_value in expanded_dict.values():
                    new_dict.update(dict_value)
                yield new_dict
        else:
            yield flattened_data

    else:
        yield flattened_data


def flatten_data_frame(data_frame, lists_to_rows=False):
    """
    Flatten a DataFrame that contains nested dicts in columns.

    Be careful using this function on a larger data frames since this
    is a slow flattening process.

    :param DataFrame DataFrame: The data frame to flatten.
    :param lists_to_rows bool: Determines whether values in lists get expanded
            into column_1, column_2, ..., column_2 or if it gets expanded
            into multiple rows (defaults to column_N, set to True to expand
            to rows).
    :return: A DataFrame that is flattened.
    """
    rows = []
    for _, row in data_frame.iterrows():
        new_rows = flatten_json_output(
            row.to_dict(), lists_to_rows=lists_to_rows)
        rows.extend(list(new_rows))

    return pd.DataFrame(rows)


def parse_date_offset(offset_string):  # noqa: C901
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

    return f'{start_time}Z', f'{end_time}Z'
