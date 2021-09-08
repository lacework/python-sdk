import logging
import os

from laceworksdk import LaceworkClient

from . import config
from . import utils


logger = logging.getLogger('lacework_sdk.jupyter.client')


class APIWrapper:
    """
    API Wrapper class that takes an API wrapper and decorates functions.
    """

    def __init__(self, api_wrapper):
        self._api_wrapper = api_wrapper
        for func_name in [f for f in dir(api_wrapper) if not f.startswith('_')]:
            func = getattr(api_wrapper, func_name)
            setattr(self, func_name, utils.dataframe_decorator(func))


class LaceworkJupyterHelper:
    """
    Lacework Jupyter helper class.

    This is a simple class that acts as a Jupyter wrapper around the
    Python Lacework SDK. It simply wraps the SDK functions to return
    a DataFrame instead of a dict when calling API functions.
    """

    def __init__(
            self, api_key=None, api_secret=None, account=None,
            subaccount=None, instance=None, base_domain=None,
            profile=None):

        self.sdk = LaceworkClient(
            api_key=api_key, api_secret=api_secret,
            account=account, subaccount=subaccount,
            instance=instance, base_domain=base_domain,
            profile=profile)

        wrappers = [w for w in dir(self.sdk) if not w.startswith('_')]
        for wrapper in wrappers:
            wrapper_object = getattr(self.sdk, wrapper)
            api_wrapper = APIWrapper(wrapper_object)
            setattr(self, wrapper, api_wrapper)

    def __enter__(self):
        """
        Support the with statement in python.
        """
        self.load_config()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Support the with statement in python.
        """
        pass
