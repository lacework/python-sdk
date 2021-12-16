"""
File that includes new custom accessors to pandas.
"""

import base64
import urllib.parse

import pandas as pd


@pd.api.extensions.register_series_accessor('decode')
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
        decoded_string = base64.b64decode(string_value)
        try:
            return decoded_string.decode('utf8')
        except UnicodeDecodeError:
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
            the alternative alphabet used instead of the '+' and '/' characters.
        :return: Decoded Base64 string.
        """
        return self.data.apply(
            lambda x: base64.b64decode(x, altchars=altchars, validate=True))

    def url_unquote(self):
        """
        Takes a series with URL encoded characters and unquotes them.
        """
        return self.data.apply(urllib.parse.unquote_plus)


@pd.api.extensions.register_series_accessor('encode')
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
