import functools

import pandas as pd

from . import config


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


def plugin_decorator(function, output_plugin):
    """
    A decorator used to use a plugin to convert Lacework JSON API output.
    """
    @functools.wraps(function)
    def get_output(*args, **kwargs):
        data = function(*args, **kwargs)
        return output_plugin(data)

    return get_output
