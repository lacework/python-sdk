# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging
import os
import random
import time

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Use enviroment variables to instantiate a LaceworkClient instance
    lacework_client = LaceworkClient(api_key=os.getenv("LW_API_KEY"),
                                     api_secret=os.getenv("LW_API_SECRET"),
                                     account=os.getenv("LW_ACCOUNT"))

    # Build start/end times
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=6)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # Vulnerability API

    # Host

    # Get host vulnerabilities for the previous 24 hours
    host_vulnerabilities = lacework_client.vulnerabilities.get_host_vulnerabilities()

    # Get host vulnerabilities for the specified CVE
    host_vulnerabilities_cve = lacework_client.vulnerabilities.get_host_vulnerabilities_by_cve(random.choice(host_vulnerabilities["data"])["cve_id"])

    # Get host vulnerabilities for the specified machine ID
    host_vulnerabilities_machine_id = lacework_client.vulnerabilities.get_host_vulnerabilities_by_machine_id("1")

    # Containers

    # Get container evaluations for the specified time range
    container_evaluations = lacework_client.vulnerabilities.get_container_assessments_by_date(start_time=start_time, end_time=end_time)

    # Get container vulnerabilities for the specified image digest
    container_vulnerabilities = lacework_client.vulnerabilities.get_container_vulnerabilities(image_digest="sha256:123")

    # Initiate a container scan for the specified repo and tag
    container_vulnerability_scan = lacework_client.vulnerabilities.initiate_container_scan("index.docker.io", "foo/bar", "latest")

    # Loop/wait for the container vulnerability scan to finish
    while True:

        # Get the scan status
        container_vulnerability_scan_status = lacework_client.vulnerabilities.get_container_scan_status(container_vulnerability_scan["data"]["RequestId"])

        # Wait for the scan to finish, then break
        if "Status" in container_vulnerability_scan_status["data"].keys():
            print(f"Current Scan Status: {container_vulnerability_scan_status['data']['Status']}...")
            time.sleep(10)
        else:
            break
