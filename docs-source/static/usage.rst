=========================
Lacework Python SDK Usage
=========================

The Lacework Python SDK closely mirrors the `Lacework API <https://docs.lacework.net/api/v2/docs/>`_
in structure. The main class of the SDK is ``LaceworkClient`` which has attributes representing
the various resources/endpoints of the Lacework API. Depending on the resource, these attributes
will have some combination of CRUD and search methods, though a few have other unique methods.
You can read about the various attributes and methods of the SDK `here <https://lacework.github.io/python-sdk/autoapi/laceworksdk/index.html>`_.

Usage Examples
==============

Example 1: Create a New User
----------------------------

This example leverages the ``team_users`` `attribute <https://lacework.github.io/python-sdk/autoapi/laceworksdk/api/v2/team_users/index.html>`_
to create a new Lacework user.


..  code-block:: python
    :caption: Creating a New User

    from laceworksdk import LaceworkClient

    lw = LaceworkClient(profile="default")
    response = lw.team_users.create("testuser", "testuser@testdomain.com", "Test Company")

Example 2: Searching for an Alert
---------------------------------

This example leverages the ``alerts`` `attribute <https://lacework.github.io/python-sdk/autoapi/laceworksdk/api/v2/alerts/index.html>`_
to find all ``Critical`` alerts that occured in the last 24 hours.

..  code-block:: python
    :caption: Searching for an Alert

    from laceworksdk import LaceworkClient
    from datetime import datetime, timedelta, timezone

    lw = LaceworkClient(profile="default")

    # Lacework will require us to specify a search window in a specific format
    # The following will allow us to specify a window that starts 1 day ago
    # and ends "now"
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=1)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # We need to specify our start time, end time, and search criteria in this structure
    # In this case we are specifying that the alert "severity" property should be equal
    # to "Critical"
    filters = {
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters":
            [
                {
                    "field": "severity",
                    "expression": "eq",
                    "value": "critical"
                }
            ]
    }

    # Make the API call, note that all search methods in this SDK will return
    # Generators, not lists or dicts
    alerts = lw.alerts.search(json=filters)


Note: This search will return a generator object, not a list or dict. If you are
unfamiliar with Python generators you may want to read up on them.

https://wiki.python.org/moin/Generators

Example 3: Retrieving a Compliance Report
-----------------------------------------

This example leverages the ``cloud_accounts`` `attribute <https://lacework.github.io/python-sdk/autoapi/laceworksdk/api/v2/cloud_accounts/index.html>`_
first to retrieve a list of AWS account integrations, specifically those that retrieve "config"
information. It uses a python list comprehension to select the first one it finds and parses the
AWS account ID from that data.

Once it has a valid AWS account integration it uses this to pull a CIS 1.4 report using the
``reports`` `attribute <https://lacework.github.io/python-sdk/autoapi/laceworksdk/api/v2/reports/index.html>`_.

..  code-block:: python
    :caption: Retrieving a Report

    from laceworksdk import LaceworkClient

    lw = LaceworkClient(profile="default")

    # Get a list of accounts
    accounts = lw.cloud_accounts.get()['data']

    # List comprehension to filter out disabled or misconfigured integrations
    # as well as only select for "config" type integrations
    config_accounts = [account for account in accounts if ("Cfg" in account['type'] and account['enabled'] == 1 and account['state']['ok'] is True)]

    # Loop through what's left and find the first AWS integration
    for config_account in config_accounts:
        if config_account['type'] == 'AwsCfg':
            # Parse the AWS account ID from the account details
            arn_elements = config_account['data']['crossAccountCredentials']['roleArn'].split(':')
            primary_query_id = arn_elements[4]
            break

    # Leverage the retrieved account ID to pull a CIS 1.4 report for that account
    # in html format
    response = lw.reports.get(primary_query_id=primary_query_id,
                    format="html",
                    type="COMPLIANCE",
                    report_type="AWS_CIS_14")



More Examples
-------------

You can find more examples in the "examples" folder of the github repository
`here <https://github.com/lacework/python-sdk/tree/main/examples>`_.
