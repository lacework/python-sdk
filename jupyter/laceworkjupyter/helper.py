import logging

from laceworksdk import LaceworkClient
from laceworksdk.api import base_endpoint


from . import decorators
from . import plugins


logger = logging.getLogger("lacework_sdk.jupyter.helper")


class APIWrapper:
    """
    API Wrapper class that takes an API wrapper and decorates functions.
    """

    def __init__(self, api_wrapper, wrapper_name):
        self._api_wrapper = api_wrapper
        self._api_name = wrapper_name

        for fname in [f for f in dir(api_wrapper) if not f.startswith("_")]:
            func = getattr(api_wrapper, fname)

            decorator_plugin = plugins.PLUGINS.get(
                f"{self._api_name}.{fname}")
            if decorator_plugin:
                setattr(
                    self,
                    fname,
                    decorators.plugin_decorator(func, decorator_plugin))
            else:
                setattr(self, fname, decorators.dataframe_decorator(func))


class LaceworkJupyterClient:
    """
    Lacework API client wrapped up for Jupyter usage.

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

        wrappers = [w for w in dir(self.sdk) if not w.startswith("_")]
        for wrapper in wrappers:
            if wrapper == 'subaccount':
                continue

            wrapper_object = getattr(self.sdk, wrapper)
            api_wrapper = APIWrapper(wrapper_object, wrapper_name=wrapper)

            save_wrapper = True

            for subwrapper in dir(wrapper_object):
                if subwrapper.startswith("_"):
                    continue
                subwrapper_object = getattr(wrapper_object, subwrapper)
                if isinstance(subwrapper_object, base_endpoint.BaseEndpoint):
                    save_wrapper = False
                    subapi_wrapper = APIWrapper(
                        subwrapper_object, wrapper_name=f"{wrapper}/{subwrapper}")
                    setattr(wrapper_object, subwrapper, subapi_wrapper)

            if save_wrapper:
                setattr(self, wrapper, api_wrapper)
            else:
                setattr(self, wrapper, wrapper_object)

    @property
    def subaccount(self):
        """Returns the subaccount that is in use."""
        return self.sdk.subaccount

    @subaccount.setter
    def subaccount(self, subaccount):
        """Changes the subaccount that is in use."""
        if subaccount == self.subaccount:
            return

        self.sdk.set_subaccount(subaccount)

    def __enter__(self):
        """
        Support the with statement in python.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Support the with statement in python.
        """
        pass
