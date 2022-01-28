# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import random

from datetime import datetime, timedelta, timezone


class BaseEndpoint:

    OBJECT_ID_NAME = None
    OBJECT_TYPE = None
    OBJECT_PARAM_EXCEPTIONS = []

    def test_object_creation(self, api_object):
        assert isinstance(api_object, self.OBJECT_TYPE)

    def _check_object_values(self, param_dict, response):
        for key, value in param_dict.items():
            if key not in self.OBJECT_PARAM_EXCEPTIONS:
                key = self._convert_lower_camel_case(key)

                if isinstance(value, dict):
                    assert value.items() <= response["data"][key].items()
                else:
                    assert value == response["data"][key]

    def _get_object_classifier_test(self,
                                    api_object,
                                    classifier_name,
                                    classifier_key=None):
        if classifier_key is None:
            classifier_key = classifier_name

        classifier_value = self._get_random_object(api_object, classifier_key)

        if classifier_value:
            method = getattr(api_object, f"get_by_{classifier_name}")

            response = method(classifier_value)

            assert "data" in response.keys()
            if isinstance(response["data"], list):
                assert response["data"][0][classifier_key] == classifier_value
            elif isinstance(response["data"], dict):
                assert response["data"][classifier_key] == classifier_value

    def _get_random_object(self, api_object, key=None):
        response = api_object.get()

        if len(response["data"]) > 0:
            if key:
                return random.choice(response["data"])[key]
            else:
                return random.choice(response["data"])
        else:
            return None

    def _get_start_end_times(self, day_delta=1):
        current_time = datetime.now(timezone.utc)
        start_time = current_time - timedelta(days=day_delta)
        start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        return start_time, end_time

    @staticmethod
    def _convert_lower_camel_case(param_name):
        words = param_name.split("_")
        first_word = words[0]

        if len(words) == 1:
            return first_word

        word_string = "".join([x.capitalize() or "_" for x in words[1:]])

        return f"{first_word}{word_string}"
