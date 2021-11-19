"""Defines helpers for interacting with the Lacework API in a notebook."""
import logging

from . import decorators
from . import features
from . import manager

# TODO: Remove this, kept for maintaining backward compatability
# for the original design. Will be removed after a grace period.
from .helper import LaceworkJupyterClient as LaceworkJupyterHelper


logger = logging.getLogger('lacework_sdk.jupyter.client')


class LaceworkContext:
    """
    A simple context class for working in a notebook environment.
    """

    def __init__(self):
        self._cache = {}
        self.client = None

    def set_client(self, client):
        self.client = client

    def add(self, key, value):
        self._cache[key] = value

    def get(key, default_value=None):
        return self._cache.get(key, default_value)


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

        for feature, feature_name in manager.LaceworkManager.get_features():
            feature_fn = decorators.feature_decorator(feature, self.ctx)
            setattr(self, feature_name, feature_fn)

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
