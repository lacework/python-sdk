# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python Jupyter notebook
assistant interacting with Lacework APIs.
"""

import datetime

import pandas
from pandas._testing import assert_frame_equal
import pytest

from laceworkjupyter import utils


TIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"


def test_parse_data_offset():
    """Test the data offset operation."""
    def get_diff(offset_string):
        start_date, end_date = utils.parse_date_offset(offset_string)
        start_date_dt = datetime.datetime.strptime(start_date, TIME_FMT)
        end_date_dt = datetime.datetime.strptime(end_date, TIME_FMT)

        return end_date_dt - start_date_dt

    diff_dt = get_diff("LAST 3 DAYS")
    assert diff_dt.days == 3

    diff_dt = get_diff("LAST 23 MINUTES")
    assert diff_dt.total_seconds() == (23 * 60)

    diff_dt = get_diff("LAST 16 SECONDS")
    assert diff_dt.total_seconds() == 16

    with pytest.raises(ValueError):
        _ = utils.parse_date_offset("HIMA")

    with pytest.raises(ValueError):
        _ = utils.parse_date_offset("FIRST 132 DAYS")

    with pytest.raises(ValueError):
        _ = utils.parse_date_offset("LAST 132")

    with pytest.raises(ValueError):
        _ = utils.parse_date_offset("LAST 132 YEARS")


def test_flatten_json_output():
    """Test flattening out a JSON structure."""
    test_json = {
        "items": [{"value": 1243}, {"value": 634}],
        "stuff": "This is stuff",
        "value": 2355
    }

    flattened = list(utils.flatten_json_output(test_json))[0]
    expected_json = {
        "items_1.value": 1243,
        "items_2.value": 634,
        "stuff": "This is stuff",
        "value": 2355
    }
    assert flattened == expected_json

    flattened = list(utils.flatten_json_output(test_json, pre_key="foobar"))[0]
    new_expected = {
        f"foobar.{key}": value for key, value in expected_json.items()}
    assert flattened == new_expected

    flattened = list(utils.flatten_json_output(test_json, lists_to_rows=True))
    expected_json = [
        {
            "items.value": 1243,
            "stuff": "This is stuff",
            "value": 2355
        }, {
            "items.value": 634,
            "stuff": "This is stuff",
            "value": 2355
        }
    ]

    assert flattened == expected_json


def test_flatten_data_frame():
    """Generate a dataframe and flatten it."""
    lines = [
        {"first": 234, "second": 583, "third": {
            "item": 3, "another": "fyrirbaeri"}},
        {"first": 214, "second": 529, "third": {
            "item": 23, "another": "blanda"}},
        {"first": 134, "second": 545, "third": {
            "item": 43, "another": "ymist"}},
        {"first": 452, "second": 123, "third": {
            "item": 95, "another": "dot"}},
    ]

    data_frame = pandas.DataFrame(lines)
    flattened_frame = utils.flatten_data_frame(data_frame)

    expected_lines = [
        {
            "first": 234, "second": 583,
            "third.item": 3, "third.another": "fyrirbaeri"},
        {
            "first": 214, "second": 529, "third.item": 23,
            "third.another": "blanda"},
        {
            "first": 134, "second": 545, "third.item": 43,
            "third.another": "ymist"},
        {
            "first": 452, "second": 123, "third.item": 95,
            "third.another": "dot"},
    ]
    expected_frame = pandas.DataFrame(expected_lines)

    assert_frame_equal(flattened_frame, expected_frame)
