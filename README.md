# Lacework Python SDK

![Build Status](https://github.com/lacework/python-sdk/workflows/Python%20Test/badge.svg)

**laceworksdk** is a community developed Python library for interacting with the Lacework APIs.

The purpose of this library is to simplify the common tasks required for interacting with the Lacework API, and allow
users write simple code to automate tasks related to their Lacework instance.  From data retrieval to configuration,
this library aims to expose all publicly available APIs.  For example, the following code would authenticate,
fetch events, fetch host vulnerabilities, and fetch container vulnerabilities - in 5 lines of code.

```
from laceworksdk import LaceworkClient

lw = LaceworkClient(account="ACCOUNT",
                    api_key="API KEY",
                    api_secret="API SECRET")

events = lw.events.get_for_date_range(start_time=start_time, end_time=end_time)

host_vulns = lw.vulnerabilities.get_host_vulnerabilities()

container_vulns = lw.vulnerabilities.get_container_vulnerabilities(image_digest="sha256:123")
```

## Requirements

- Python 3.6 or higher
- Lacework API Credentials
  - Account Name
  - API Key
  - API Secret

## How-To

The following data points are required to instantiate a LaceworkClient instance:
   - `account`: The Lacework account/organization domain. (`xxxxx`.lacework.net)
   - `subaccount`: (Optional) The Lacework sub-account domain. (`xxxxx`.lacework.net)
      - This is only used if leveraging the Manage@Scale organization feature of Lacework
   - `api_key`: The API Key that was generated from the Lacework UI/API.
   - `api_secret`: The API Secret that was generated from the Lacework UI/API.

To generate an API Key and Secret, do the following:
   1. In the Lacework web interface, go to Settings -> API Keys
   2. Create a new API Key, or download information for an existing one.

### Environment Variables

The `account`, `subaccount`, `api_key`, and `api_secret` can also be set using environment variables.

| Environment Variable | Description | Required |
|----------------------|-------------|:--------:|
|`LW_ACCOUNT`|Lacework account/organization domain (i.e. `xxxxx`.lacework.net)|Y|
|`LW_SUBACCOUNT`|Lacework sub-account domain (i.e. `xxxxx`.lacework.net)|N|
|`LW_API_KEY`|Lacework API Access Key|Y|
|`LW_API_SECRET`|Lacework API Access Secret|Y|

## Installation

Installing and upgrading `laceworksdk` is easy:

**Install via PIP**

```$ pip install laceworksdk```

**Upgrading to the latest Version**

```$ pip install laceworksdk --upgrade```

## Examples

Are you looking for some sample scripts?  Check out the [examples](examples/) folder!

## Implemented APIs

### API v1

- [x] Compliance API
- [x] Custom Compliance Config API
- [x] Download File API
- [x] Events API
- [x] Integrations API
- [x] Run Reports API
- [x] Token API
- [x] Vulnerability API

### API v2

- [x] Access Tokens
- [x] Alert Channels
- [x] Audit Logs
- [x] CloudTrail
