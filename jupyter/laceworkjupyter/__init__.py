"""Defines helpers for interacting with the Lacework API in a notebook."""
import logging

import pandas as pd

from . import decorators
from . import features  # noqa: F401
from . import manager

# TODO: Remove this, kept for maintaining backward compatability
# for the original design. Will be removed after a grace period.
from .helper import LaceworkJupyterClient as LaceworkJupyterHelper  # noqa: F401, E501


logger = logging.getLogger("lacework_sdk.jupyter.client")


class LaceworkContext:
    """
    A simple context class for working in a notebook environment.
    """

    def __init__(self):
        self._cache = {}
        self._state = ""
        self._state_cache = {}
        self.client = None

    @property
    def cache(self):
        """
        Return a DataFrame with the content of the cache.
        """
        lines = []
        for key, value in self._cache.items():
            lines.append({
                "Name": key,
                "Type": type(value)
            })
        return pd.DataFrame(lines)

    @property
    def state(self):
        """
        Returns the current state that is in use.
        """
        return self._state

    def set_client(self, client):
        """
        Set the Lacework client inside the context.

        :param obj client: The client, instance of LaceworkJupyterClient.
        """
        self.client = client

    def add(self, key, value):
        """
        Add an entry into the context's cache.

        If the key already exists, the value in the cache is overwritten.

        :param str key: The key, or name used to store the value in the cache.
        :param obj value: The value, which can be any object.
        """
        self._cache[key] = value

    def add_state(self, state, key, value):
        """
        Add an entry into a state cache.

        This cache is meant for modules that need a bit of state, but not
        necessarily make it available for easy access from the context.

        There can only be one state at a given time, so if a module adds to
        a state that differs from the previous state, that state's cache
        gets cleared.

        :param str state: The name of the state that is adding a cache.
        :param str key: The key, or name used to store the value in the cache.
        :param obj value: The value, which can be any object.
        """
        if state != self._state:
            self._state = state
            self.state_cache = {}

        self._state_cache[key] = value

    def get(self, key, default_value=None):
        """
        Get a value from the cache.

        :param str key: The key, or name used to store the value in the cache.
        :param obj default_value: The default value that is returned if the
            cache key is not stored in the cache. Defaults to None.
        :return: The value in the cache, and if not found returns the default
            value.
        """
        return self._cache.get(key, default_value)

    def get_state(self, state, key, default_value=None):
        """
        Get a value from the state cache.

        :param str state: The name of the state we are pulling from.
        :param str key: The key, or name used to store the value in the cache.
        :param obj default_value: The default value that is returned if the
            cache key is not stored in the cache. Defaults to None.
        :return: The value in the cache, and if not found returns the default
            value.
        """
        if state != self._state:
            logger.warning(
                "Attempting to fetch from a wrong state ({0:s} vs "
                "{1:s})".format(state, self._state))
            return default_value

        return self._state_cache.get(key, default_value)


class LaceworkHelper:
    """
    Lacework Jupyter helper class.

    This is a simple class that can be used to interact with
    the Lacework API. It provides access to an API client,
    wrapped for better notebook experience as well as
    other helper functions.
    """

    def __init__(self):
        self.ctx = LaceworkContext()
        self.refresh_features()

    def refresh_features(self):
        """
        Refresh all the features of the helper.

        IF a new feature is added this function can be called to refresh
        the features that are registered to the helper object.
        """
        for feature, feature_name in manager.LaceworkManager.get_features():
            feature_fn = decorators.feature_decorator(feature, self.ctx)
            setattr(self, feature_name, feature_fn)

    @property
    def client(self):
        """
        Returns a Lacework API client object.
        """
        if self.ctx.client:
            return self.ctx.client

        return self.get_client()

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
