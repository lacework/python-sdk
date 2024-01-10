# -*- coding: utf-8 -*-
"""Lacework API wrapper."""

class BaseEndpoint:
    """A class used to implement base functionality for Lacework API Endpoints."""

    KEY_CONVERSION_EXCLUDES = ["integration_mappings"]

    def __init__(self, session, object_type, endpoint_root="/api/v2"):
        """
        Initialize the BaseEndpoint class.

        Args:
            session (HttpSession): An instance of the HttpSession class.
            object_type (str): The Lacework object type to use.
            endpoint_root (str, optional): The URL endpoint root to use.
        """
        super().__init__()
        self._session = session
        self._object_type = object_type
        self._endpoint_root = endpoint_root

    def _build_dict_from_items(self, *dicts, **items):
        """A method to build a dictionary based on inputs, pruning items that are None.

        Args:
          dicts (dict): Some number of dictionaries the join together
          items (any): Some number of keyword items to add to the joined dicts

        Returns:
          dict: A single dict built from the input.

        """
        dict_list = list(dicts)
        dict_list.append(items)
        result = {}

        for dictionary in dict_list:
            result = {
                **result,
                **self._convert_dictionary(dictionary, list(result.keys())),
            }

        return result

    def _build_url(self, id=None, resource=None, action=None):
        """Builds the URL to use based on the endpoint path, resource, type, and ID.

        Args:
          id (str): A string representing the ID of an object to use in the URL
          resource (str): A string representing the type of resource to append to the URL
          action (str): A string representing the type of action to append to the URL (Default value = None)

        Returns:
            str: a formatted URL

        """
        result = f"{self._endpoint_root}/{self._object_type}"

        if resource:
            result += f"/{resource}"
        if action:
            result += f"/{action}"
        if id:
            result += f"/{id}"

        return result

    @staticmethod
    def _convert_lower_camel_case(param_name):
        """Convert a Pythonic variable name to lowerCamelCase.

        This function will take an underscored parameter name like 'query_text' and convert it
        to lowerCamelCase of 'queryText'.  If a parameter with no underscores is provided, it will
        assume that the value is already in lowerCamelCase format.

        Args:
          param_name (str): the name of the parameter you want to convert to lowerCamelCase

        Returns:
            str: the converted string.
        """
        words = param_name.split("_")
        first_word = words[0]

        if len(words) == 1:
            return first_word

        word_string = "".join([x.capitalize() or "_" for x in words[1:]])

        return f"{first_word}{word_string}"

    def _convert_dictionary(self, dictionary, existing_keys):
        """Iteratively process a dictionary to convert it to expected JSON.

        Args:
          dictionary (dict): a dictionary
          existing_keys (list): a list of keys to append to

        Returns:
          dict: A single dictionary of lowerCamelCase key/value pairs.

        Raises:
          KeyError: In case there is a duplicate key name in the dictionary.

        """
        result = {}

        for key, value in dictionary.items():
            if key in self.KEY_CONVERSION_EXCLUDES:
                continue

            camel_key = self._convert_lower_camel_case(key)

            if value is None:
                continue
            if camel_key in existing_keys:
                raise KeyError(f"Attempted to insert duplicate key '{camel_key}'")
            if isinstance(value, dict):
                value = self._convert_dictionary(value, [])

            existing_keys.append(camel_key)
            result[camel_key] = value

        return result

    def _get_schema(self, subtype=None):
        """Get the schema for the current object type.

        Args:
          subtype (str):  subtype of object for which to retrieve schema

        Returns:
            dict: JSON object containing object schema
        """
        if subtype:
            url = f"/api/v2/schemas/{self._object_type}/{subtype}"
        else:
            url = f"/api/v2/schemas/{self._object_type}"

        response = self._session.get(url)

        return response.json()

    @property
    def session(self):
        """Get the :class:`HttpSession` instance the object is using."""
        return self._session

    def _validate_json(self, json, subtype=None):
        """TODO: A method to validate the provided JSON based on the schema of the current object."""
        schema = self._get_schema(subtype)

        # TODO: perform validation here

        return schema

    def __repr__(self):
        if hasattr(self, "id"):
            return "<%s %s>" % (self.__class__.__name__, self.id)
