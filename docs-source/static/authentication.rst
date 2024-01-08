==================================
Lacework Python SDK Authentication
==================================

Once you have installed the SDK you will need to determine how you
want to pass authentication information to the SDK. There are a
variety of ways to do this, however they all require a valid API key
for the Lacework account you wish to access with the SDK. Note that
API keys are generated at the account level only, not a the organization level.
You must have/generate a key for each account you need access to.

Learn more about generating Lacework API keys
`here <https://docs.lacework.net/api/api-access-keys-and-tokens>`_.

Learn more about Lacework organizations `here <https://docs.lacework.net/console/organization-overview>`_.

Once you have created an API key in the Lacework console you should download
the JSON file containing your new API credentials. This will contain 3 or 4 properties
depending on whether the keys you generated are part of a Lacework organization. These
properties are will be ``keyId``, ``secret``, ``account``, and optionally ``subaccount``.
If your key comes from a Lacework organization then the ``account`` property represents the
name of the organization and the ``subaccount`` property represents that name of the account
within that organization.

Be sure keep these credentials **SECURE**!

Now that you have this file you can choose which method of authentication to use:

Auth Method 1: Install the Lacework CLI
=======================================

The Lacework Python SDK does **NOT** require that you install the Lacework CLI tool. However, if you do
have the Lacework CLI `installed <https://docs.lacework.net/cli#install-the-lacework-cli>`_ AND
`configured <https://docs.lacework.net/cli#configure-the-cli>`_ then as part of it's configuration
process the CLI will create a file in your home directory called ``.lacework.toml`` which will contain
one or more sections containing Lacework credentials, with each section representing information for a
single Lacework account.

If you have this file in place and you have not specified credentials using any other method then
the Python SDK will use the credentials stored there to access the Lacework API endpoints. Note that by
default the SDK will use the creds in the  ``default`` section of the ``.lacework.toml`` file.
You can tell the SDK to use a different section using the ``profile=`` keyword argument when
instantiating the class.

..  code-block:: python
    :caption: Using the default profile

    from laceworksdk import LaceworkClient

    lw = LaceworkClient()

..  code-block:: python
    :caption: Specifying a profile

    from laceworksdk import LaceworkClient

    lw = LaceworkClient(profile="testprofile")


Auth Method 2: Specify the Credentials as Environment Variables
===============================================================

You can specify your account credentials or the profile to use in environmental variables.

======================= ====================================================================== ==========
  Environment Variable   Description                                                            Required
  --------------------- ---------------------------------------------------------------------- ----------
   ``LW_PROFILE``        Lacework CLI profile to use (configured at ~/.lacework.toml)              N
   ``LW_ACCOUNT``        Lacework account/organization domain (i.e. `<account>`.lacework.net)      Y
   ``LW_SUBACCOUNT``     Lacework sub-account                                                      N
   ``LW_API_KEY``        Lacework API Access Key                                                   Y
   ``LW_API_SECRET``     Lacework API Access Secret                                                Y
======================= ====================================================================== ==========

Note: Specifying creds this way will override your ``.lacework.toml`` default profile.

Auth Method 3: Specify the Credentials Manually
===============================================

The most straight forward way of specifying credentials is to pass them to the class instance at
instantiation.

..  code-block:: python
    :caption: Specifying the credentials at class instantiation

    from laceworksdk import LaceworkClient

    lw = LaceworkClient(account="ACCOUNT",
                        subaccount="SUBACCOUNT",
                        api_key="API KEY",
                        api_secret="API SECRET")

Note: This will override your ``.lacework.toml`` default profile AND any credentials you may have
specified as environmental variables.
