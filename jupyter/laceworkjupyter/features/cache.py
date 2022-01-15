"""
Simple feature to get values from cache.
"""

from laceworkjupyter import manager


@manager.register_feature
def get_from_cache(key, default_value=None, ctx=None):
    """Returns value from the context cache.

    :param str key: String with the key.
    :param obj default_value: Optional default value, if the
        key is not found inside the cache this value will be
        returned, defaults to None.
    :param obj ctx: The context object.
    :returns: The value in the cache that corresponds to the provided key.
    """
    if not ctx:
        return default_value

    return ctx.get(key, default_value)
