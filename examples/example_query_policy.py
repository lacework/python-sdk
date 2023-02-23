# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import random
import string

from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

RANDOM_TEXT = "".join(random.choices(string.ascii_uppercase, k=4))
QUERY_ID = f"Custom_Query_{RANDOM_TEXT}"
POLICY_TITLE = f"Custom_Policy_{RANDOM_TEXT}"

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Queries/Policies API

    # Create a Query
    query_response = lacework_client.queries.create(
        evaluator_id="Cloudtrail",
        query_id=QUERY_ID,
        query_text="""{{
            source {{CloudTrailRawEvents e}}
            filter {{EVENT_SOURCE = 'iam.amazonaws.com' AND
                     EVENT:userIdentity.name::String NOT LIKE 'Terraform-Service-Acct'}}
            return distinct {{EVENT_NAME, EVENT}}
            }}
        """
    )

    # Create a Policy
    lacework_client.policies.create(
        policy_type="Violation",
        query_id=query_response["data"]["queryId"],
        enabled=True,
        title=POLICY_TITLE,
        description=f"{POLICY_TITLE}_Description",
        remediation="Policy remediation",
        severity="high",
        alert_enabled=True,
        alert_profile="LW_CloudTrail_Alerts",
        evaluator_id=query_response["data"]["evaluatorId"]
    )
