# -*- coding: utf-8 -*-
"""
Package configuration.
"""

# Package Constants
DEFAULT_BASE_DOMAIN = "lacework.net"
DEFAULT_ACCESS_TOKEN_EXPIRATION = 3600
DEFAULT_SUCCESS_RESPONSE_CODES = [200, 201, 204]

# Environment Variable Definitions
LACEWORK_ACCOUNT_ENVIRONMENT_VARIABLE = "LW_ACCOUNT"
LACEWORK_SUBACCOUNT_ENVIRONMENT_VARIABLE = "LW_SUBACCOUNT"
LACEWORK_API_KEY_ENVIRONMENT_VARIABLE = "LW_API_KEY"
LACEWORK_API_SECRET_ENVIRONMENT_VARIABLE = "LW_API_SECRET"
LACEWORK_API_BASE_DOMAIN_ENVIRONMENT_VARIABLE = "LW_BASE_DOMAIN"
LACEWORK_API_CONFIG_SECTION_ENVIRONMENT_VARIABLE = "LW_PROFILE"

# Config file paths.
LACEWORK_CLI_CONFIG_RELATIVE_PATH = '.lacework.toml'
