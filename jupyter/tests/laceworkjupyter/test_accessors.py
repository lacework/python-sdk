"""
Test file for the local accessors.
"""
import pandas as pd

from laceworkjupyter import accessors  # noqa: F401


def test_decode_accessor():
    """
    Tests the decode accessor.
    """
    lines = [
        {
            'value': 12, 'some_string': 'VGhpcyBpcyBhIHN0cmluZw==',
            'uri': 'http://mbl.is/%3Fstuff=r+1%20af'
        }, {
            'value': 114, 'some_string': 'VGhpcyBpcyBhIGEgc2VjcmV0',
            'uri': 'http://mbl.is/%3Fsfi=r+1%20af'
        },
    ]
    frame = pd.DataFrame(lines)

    decoded_series = frame.some_string.decode.base64()
    discovered_set = set(list(decoded_series.values))

    expected_set = set([
        'This is a a secret', 'This is a string'])

    assert expected_set == discovered_set

    unquoted_series = frame.uri.decode.url_unquote()
    unquoted_set = set(list(unquoted_series.values))

    expected_set = set([
        'http://mbl.is/?stuff=r 1 af',
        'http://mbl.is/?sfi=r 1 af'])

    assert expected_set == unquoted_set
