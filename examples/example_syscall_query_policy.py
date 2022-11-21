# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class with Syscall data sources.
Note: As of this commit, the Lacework Syscall agent is not GA. Please contact your Lacework rep for more information
"""

import logging
import random
import string

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

RANDOM_TEXT = "".join(random.choices(string.ascii_uppercase, k=4))
QUERY_ID = f"Custom_Syscall_Query_{RANDOM_TEXT}"
POLICY_TITLE = f"Custom_Syscall_Policy_{RANDOM_TEXT}"

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Queries/Policies API

    # Create a Query
    query_response = lacework_client.queries.create(
        query_id=QUERY_ID,
        query_text=f"""{{
          source {{
                LW_HA_SYSCALLS_FILE
          }}
          filter {{
                TARGET_OP like any('create','modify') AND TARGET_PATH like any('%/.ssh/authorized_keys','%/ssh/sshd_config')
          }}
          return distinct {{
                RECORD_CREATED_TIME,
                MID,
                TARGET_OP,
                TARGET_PATH
          }}
        }}
        """
    )

    # Create a Policy, uncomment alternate alert_profiles as required
    lacework_client.policies.create(
        policy_type="Violation",
        query_id=query_response["data"]["queryId"],
        enabled=True,
        title=POLICY_TITLE,
        description="Description here..",
        remediation="Policy remediation here..",
        severity="high",
        alert_enabled=True,
        alert_profile="LW_HA_SYSCALLS_FILE_DEFAULT_PROFILE.Violation"
    )
