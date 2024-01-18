# -*- coding: utf-8 -*-
"""
Example script showing how to use the LaceworkClient class.
"""

import logging

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from laceworksdk import LaceworkClient

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

if __name__ == "__main__":

    # Instantiate a LaceworkClient instance
    lacework_client = LaceworkClient()

    # Build start/end times
    current_time = datetime.now(timezone.utc)
    start_time = current_time - timedelta(days=6)
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
    end_time = current_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # Vulnerability API

    # Host

    # This yields a generator
    host_vulns = lacework_client.vulnerabilities.hosts.search(json={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    # get the first page of data from the generator using "next" and print it
    print(next(host_vulns)['data'])
    # Containers

    container_vulns = lacework_client.vulnerabilities.containers.search({
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        }
    })

    # iterate through the generator but let's stop at the first page so we don't have to see all the container vulns
    for page in container_vulns:
        print(page['data'])
        # we wouldn't normally break here but for this example there's no reason to retrieve all the pages
        break
