# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    from laceworksdk import LaceworkClient

    lw = LaceworkClient(profile="default")

    # Get a list of accounts
    accounts = lw.cloud_accounts.get()['data']

    # List comprehension to filter out disabled or misconfigured integrations
    # as well as only select for "config" type integrations
    config_accounts = [account for account in accounts if
                       ("Cfg" in account['type'] and account['enabled'] == 1 and account['state']['ok'] is True)]

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
