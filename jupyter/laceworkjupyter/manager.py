"""A manager that manages various plugins in the helper."""


class LaceworkManager:
    """Simple plugin management class."""

    # Dictionaries holding the registered functions.
    _plugins = {}
    _features = {}

    @classmethod
    def add_feature(cls, feature_fn, feature_name):
        """
        Add a feature to the registration.

        :param func feature_fn: The function to be registered.
        :param str feature_name: The name of the function.
        :raises ValueError: If the function is already registered.
        """
        feature_name = feature_name.lower()

        if feature_name == 'ctx':
            raise ValueError(
                'Feature ctx is a reserved name for a feature.')

        if feature_name in cls._features:
            raise ValueError(
                'Feature {0:s} is already registered as a feature.'.format(
                    feature_name))
        cls._features[feature_name] = feature_fn

    @classmethod
    def get_features(cls):
        """
        Yields a tuple with the feature function and name.

        :yields: A tuple two items, feature function and feature name.
            A tuple is yielded for each registered feature in the system.
        """
        for feature_fn, feature_name in cls._features.items():
            yield (feature_name, feature_fn)


def register_feature(fn, name=""):
    """
    Decorator that can be used to register a feature.

    :param function fn: The function to register.
    :param str name: Optional string with the name of the function
        as it should be registered. If not provided the name of the
        function is used.
    """
    if not name:
        name = fn.__name__

    LaceworkManager.add_feature(fn, name)
    return fn
