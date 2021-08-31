import configparser
import logging
import os

from . import config
from . import utils

from laceworksdk import LaceworkClient


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

    def __init__(self):
        self.sdk = None

        self._api_key = ''
        self._api_secret = ''
        self._account = ''
        self._subaccount = None
        self._instance = None
        self._base_domain = None
        self._config_file_path = ''

    def _authenticate_and_load(self):
        """
        Authenticates to the LaceworkClient SDK and loads the SDK functions.
        """
        self.sdk = LaceworkClient(
            api_key=self._api_key, api_secret=self._api_secret,
            account=self._account, subaccount=self._subaccount,
            instance=self._instance, base_domain=self._base_domain)

        wrappers = [w for w in dir(self.sdk) if not w.startswith('_')]
        for wrapper in wrappers:
            wrapper_object = getattr(self.sdk, wrapper)
            api_wrapper = APIWrapper(wrapper_object)
            setattr(self, wrapper, api_wrapper)

    def load_config(self, file_path=''):
        """
        Use a CLI configuration file to authenticate to the Lacework SDK.

        :param str file_path: Optional path to the TOML file that defines
                authentication information to the SDK. If not provided it
                will use the default path.
        :raises ValueError: If the config cannot be loaded.
        """
        if not file_path:
            file_path = os.path.join(
                os.path.expanduser('~'), config.DEFAULT_REL_CONFIG_PATH)

        if not os.path.isfile(file_path):
            raise ValueError('Unable to load path, file does not exist.')

        config_obj = configparser.ConfigParser()
        config_obj.read([file_path])
        if not config_obj.has_section('default'):
            raise ValueError('Config file does not have the default section.')

        config_section = config_obj['default']
        self._api_key = config_section.get('api_key', '').strip('""')
        self._api_secret = config_section.get('api_secret', '').strip('""')
        self._account = config_section.get('account', '').strip('""')

        self._authenticate_and_load()

    def set_auth_parameters(
            self, api_key=None, api_secret=None, account=None,
            subaccount=None, instance=None, base_domain=None):
        """
        Manually authenticate to the Lacework SDK.
        """
        self._api_key = api_key
        self._api_secret = api_secret
        self._account = account
        self._subaccount = subaccount
        self._instance = instance
        self._base_domain = base_domain

        self._authenticate_and_load()

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
