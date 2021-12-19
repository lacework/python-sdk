# A simple class to get a jupyter client.

from laceworkjupyter import helper
from laceworkjupyter import manager


@manager.register_feature
def get_client(
        api_key=None, api_secret=None, account=None,
        subaccount=None, instance=None, base_domain=None,
        profile=None, ctx=None):
    """
    Returns a Lacework API client for use in a notebook.

    :return: An instance of a LaceworkJupyterClient.
    """

    client = helper.LaceworkJupyterClient(
        api_key=api_key, api_secret=api_secret, account=account,
        subaccount=subaccount, instance=instance, base_domain=base_domain,
        profile=profile)

    ctx.set_client(client)
    return client
