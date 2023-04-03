# -*- coding: utf-8 -*-
"""
Community-developed Python SDK for interacting with Lacework APIs.
"""

from importlib_metadata import version

import logging

from .api import LaceworkClient  # noqa: F401
from .exceptions import ApiError, LaceworkSDKException  # noqa: F401

__version__ = version(__name__)

# Initialize Package Logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
