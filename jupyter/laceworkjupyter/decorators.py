import functools
import types

import pandas as pd

from . import config


def dataframe_decorator(function):
    """
    A decorator used to convert Lacework JSON API output into a dataframe.
    """
    def _get_frame_from_dict(data):
        if not isinstance(data, dict):
            return

        data_items = data.get('data', [])
        if isinstance(data_items, dict):
            data_items = [data_items]

        df = pd.DataFrame(data_items)
        if 'SEVERITY' in df:
            df['SEVERITY'] = df.SEVERITY.apply(
                lambda x: config.SEVERITY_DICT.get(x, x))
        return df

    @functools.wraps(function)
    def get_output(*args, **kwargs):
        data = function(*args, **kwargs)

        if isinstance(data, dict):
            return _get_frame_from_dict(data)

        elif isinstance(data, (types.GeneratorType, list, map, filter)):
            frames = [_get_frame_from_dict(x) for x in data]
            return pd.concat(frames)

        return data

    return get_output


def plugin_decorator(function, output_plugin):
    """
    A decorator used to use a plugin to convert Lacework JSON API output.
    """
    @functools.wraps(function)
    def get_output(*args, **kwargs):
        data = function(*args, **kwargs)
        return output_plugin(data)

    return get_output


def feature_decorator(function, ctx=None):
    """
    A decorator that adds a context to a function call.
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if ctx:
            kwargs['ctx'] = ctx
        return function(*args, **kwargs)

    return wrapper
