<img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="600">

# Lacework Python SDK

![Build Status](https://github.com/lacework/python-sdk/actions/workflows/python-test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/laceworksdk)](https://pepy.tech/project/laceworksdk)

**laceworksdk** is a community developed Python library for interacting with the Lacework APIs.

The purpose of this library is to simplify the common tasks required for interacting with the Lacework API, and allow
users write simple code to automate tasks related to their Lacework instance(s). From data retrieval to configuration,
this library aims to expose all publicly available APIs. For example, the following code would authenticate,
fetch events, fetch host vulnerabilities, and fetch container vulnerabilities. The latest version of the SDK supports
expressive searches as enabled by v2 of the Lacework APIs.

For more information read the [documentation](https://lacework.github.io/python-sdk/)
```python
from laceworksdk import LaceworkClient

lw = LaceworkClient() # This would leverage your default Lacework CLI profile.
lw = LaceworkClient(account="ACCOUNT",
                    subaccount="SUBACCOUNT",
                    api_key="API KEY",
                    api_secret="API SECRET")

events = lw.events.search(json={
  "timeFilter": {
    "startTime": start_time,
    "endTime": end_time
  }
})

host_vulns = lw.vulnerabilities.hosts.search(json={
    "timeFilter": {
        "startTime": start_time,
        "endTime": end_time
    }
})

container_vulns = lw.vulnerabilities.containers.search(json={
    "timeFilter": {
        "startTime": start_time,
        "endTime": end_time
    },
    "filters": [
        {
            "field": "imageId",
            "expression": "eq",
            "value": "sha256:657922eb2d64b0a34fe7339f8b48afb9f2f44635d7d6eaa92af69591d29b3330"
        }
    ]
})
```

## Requirements

- Python 3.8 or higher
- Lacework API Credentials
  - Account Name
  - API Key
  - API Secret

## How-To

The following information is required to instantiate a LaceworkClient instance:

- `account`: The Lacework account/organization domain. (`xxxxx`.lacework.net)
- `api_key`: The API Key that was generated from the Lacework UI/API.
- `api_secret`: The API Secret that was generated from the Lacework UI/API.

Optionally, you can also set a Lacework Sub-Account using the `subaccount` parameter.

To generate API credentials, you'll need to do the following in Lacework:

1.  In the Lacework web interface, go to Settings -> API Keys
2.  Create a new API Key and download information the credentials.

## Environment Variables

If you wish to configure the LaceworkClient instance using environment variables, this module honors the same
variables used by the Lacework CLI. The `account`, `subaccount`, `api_key`, `api_secret`, and `profile` parameters
can all be configured as specified below.

| Environment Variable | Description                                                          | Required |
| -------------------- | -------------------------------------------------------------------- | :------: |
| `LW_PROFILE`         | Lacework CLI profile to use (configured at ~/.lacework.toml)         |    N     |
| `LW_ACCOUNT`         | Lacework account/organization domain (i.e. `<account>`.lacework.net) |    Y     |
| `LW_SUBACCOUNT`      | Lacework sub-account                                                 |    N     |
| `LW_API_KEY`         | Lacework API Access Key                                              |    Y     |
| `LW_API_SECRET`      | Lacework API Access Secret                                           |    Y     |

## Installation

Installing and upgrading `laceworksdk` is easy:

**Install via PIP**

`$ pip install laceworksdk`

**Upgrading to the latest Version**

`$ pip install laceworksdk --upgrade`

## Examples

Are you looking for some sample scripts? Check out the [examples](examples/) folder!

### [Contributing](CONTRIBUTING.md)
