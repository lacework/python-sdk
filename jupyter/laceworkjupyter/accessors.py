"""
File that includes custom accessors to pandas.

This is a way to define custom accessors to either
data frames or series objects.
"""

import base64
import binascii
import logging
import socket

import urllib.parse

import numpy as np
import pandas as pd


logger = logging.getLogger("lacework_sdk.jupyter.accessor")


@pd.api.extensions.register_series_accessor("decode")
class DecodeAccessor:
    """
    Accessor class for decoding data.
    """
    def __init__(self, data):
        self.data = data

    def _decode_string_base64(self, string_value):
        """
        Returns decoded base64 string.

        :param str string_value: The base64 decoded string.
        :return: A decoded string.
        """
        try:
            decoded_string = base64.b64decode(string_value)
        except binascii.Error as exc:
            logger.error(
                "Unable to decode string: '{0:s}', error: {1!s}".format(
                    string_value, exc)),
            return string_value

        try:
            return decoded_string.decode("utf8")
        except UnicodeDecodeError:
            logger.warning("Unable to decode string using UTF-8")
            return decoded_string

    def base64(self):
        """
        Takes a series with base64 encoded data and decodes it.
        """
        return self.data.apply(self._decode_string_base64)

    def base64_altchars(self, altchars):
        """
        Takes a series with base64 encoded data and decodes it using altchars.

        :param bytes altchars: A byte-like object of length 2 which specifies
            the alternative alphabet used instead of the '+' and '/'
            characters.
        :return: Decoded Base64 string.
        """
        return self.data.apply(
            lambda x: base64.b64decode(x, altchars=altchars, validate=True))

    def url_unquote(self):
        """
        Takes a series with URL encoded characters and unquotes them.
        """
        return self.data.apply(urllib.parse.unquote_plus)


@pd.api.extensions.register_series_accessor("encode")
class EncodeAccessor:
    """
    Accessor class to encode data.
    """
    def __init__(self, data):
        self.data = data

    def base64(self):
        """
        Returns base64 encoded data from a string series.
        """
        return self.data.astype(bytes).apply(base64.b64encode)


@pd.api.extensions.register_series_accessor("ip")
class IPAccessor:
    """
    Accessor class for IP address related information.
    """
    def __init__(self, data):
        self.data = data
        self._cache = {}

    def _reverse(self, ip):
        """
        Returns a reverse DNS lookup for an IP address.

        :param str ip: An IP address to lookup
        :return: A string with the results from the reverse lookup
            or a NAN value if none found.
        """
        cached = self._cache.get("reverse", {}).get(ip)
        if cached:
            return cached

        try:
            results = socket.gethostbyaddr(ip)
        except (socket.gaierror, socket.herror):
            return np.nan

        if not results:
            return np.nan

        value = results[0]
        self._cache.setdefault("reverse", {})
        self._cache["reverse"][ip] = value
        return value

    def reverse_dns(self):
        """
        Takes a pandas Series or a column and does reverse DNS lookups.

        This takes a column in a DataFrame or a Series object that contains
        IP addresses and does a reverse DNS lookup for each of the IPs found
        in the dataset.

        :return: A pandas Series object with either a rDNS value or NAN if not
            found for each IP address in the incoming column.
        """
        return self.data.apply(self._reverse)
