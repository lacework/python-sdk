# -*- coding: utf-8 -*-

class BaseEndpoint:
    """
    A class used to implement base functionality for Lacework API Endpoints
    """

    def __init__(self,
                 session,
                 object_type,
                 endpoint_root="/api/v2"):
        """
        :param session: An instance of the HttpSession class.
        :param object_type: The Lacework object type to use.
        :param endpoint_root: The URL endpoint root to use.
        """

        super().__init__()
        self._session = session
        self._object_type = object_type
        self._endpoint_root = endpoint_root

    def build_dict_from_items(self, *dicts, **items):
        """
        A method to build a dictionary based on inputs, pruning items that are None.

        :raises KeyError: In case there is a duplicate key name in the dictionary.
        :returns: A single dict built from the input.
        """

        dict_list = list(dicts)
        dict_list.append(items)
        result = {}

        for d in dict_list:
            for key, value in d.items():
                camel_key = self._convert_lower_camel_case(key)
                if value is None:
                    continue
                if camel_key in result.keys():
                    raise KeyError(f"Attempted to insert duplicate key '{camel_key}'")

                result[camel_key] = value

        return result

    def build_url(self, id=None, resource=None, action=None):
        """
        Builds the URL to use based on the endpoint path, resource, type, and ID.

        :param id: A string representing the ID of an object to use in the URL
        :param resource: A string representing the type of resource to append to the URL
        :param action: A string representing the type of action to append to the URL
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
        """
        Convert a Pythonic variable name to lowerCamelCase.

        This function will take an underscored parameter name like 'query_text' and convert it
        to lowerCamelCase of 'queryText'.  If a parameter with no underscores is provided, it will
        assume that the value is already in lowerCamelCase format.
        """

        words = param_name.split("_")
        first_word = words[0]

        if len(words) == 1:
            return first_word

        word_string = "".join([x.capitalize() or "_" for x in words[1:]])

        return f"{first_word}{word_string}"

    def _get_schema(self, subtype=None):
        """
        Get the schema for the current object type.
        """
        if subtype:
            url = f"/api/v2/schemas/{self._object_type}/{subtype}"
        else:
            url = f"/api/v2/schemas/{self._object_type}"

        response = self._session.get(url)

        return response.json()

    @property
    def session(self):
        """
        Get the :class:`HttpSession` instance the object is using.
        """

        return self._session

    def validate_json(self, json, subtype=None):
        """
        TODO: A method to validate the provided JSON based on the schema of the current object.
        """

        schema = self._get_schema(subtype)

        # TODO: perform validation here

        return schema

    def __repr__(self):
        if hasattr(self, "id"):
            return "<%s %s>" % (self.__class__.__name__, self.id)
