# -*- coding: utf-8 -*-
"""
HttpSession class for package HTTP functions.
"""

import json
import logging
import requests

from datetime import datetime, timezone
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from laceworksdk import version
from laceworksdk.config import (
    DEFAULT_BASE_DOMAIN,
    DEFAULT_ACCESS_TOKEN_EXPIRATION,
    DEFAULT_SUCCESS_RESPONSE_CODES
)
from laceworksdk.exceptions import ApiError

logger = logging.getLogger(__name__)


class HttpSession(object):
    """
    Package HttpSession class.
    """

    _access_token = None
    _access_token_expiry = None

    def __init__(self, account, subaccount, api_key, api_secret):
        """
        Initializes the HttpSession object.

        :param account: a Lacework Account name
        :param subaccount: a Lacework Sub-account name
        :param api_key: a Lacework API Key
        :param api_secret: a Lacework API Secret

        :return HttpSession object.
        """

        super(HttpSession, self).__init__()

        # Create a requests session
        self._session = self._retry_session()

        # Set the base parameters
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_url = f"https://{account}.{DEFAULT_BASE_DOMAIN}"
        self._subaccount = subaccount

        # Get an access token
        self._check_access_token()

    def _retry_session(self,
                       retries=3,
                       backoff_factor=0.3,
                       status_forcelist=(500, 502, 504)):
        """
        A method to set up automatic retries on HTTP requests that fail.
        """

        # Create a new requests session
        session = requests.Session()

        # Establish the retry criteria
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            status=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )

        # Build the adapter with the retry criteria
        adapter = HTTPAdapter(max_retries=retry)

        # Bind the adapter to HTTP/HTTPS calls
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return session

    def _check_access_token(self):
        """
        A method to check the validity of the access token.
        """

        if self._access_token is None or self._access_token_expiry < datetime.now(timezone.utc):

            response = self._get_access_token()

            # Parse and restructure the returned date (necessary for Python 3.6)
            expiry_date = response.json()["expiresAt"].replace('Z', '+0000')

            # Update the access token and expiration
            self._access_token_expiry = datetime.strptime(expiry_date, "%Y-%m-%dT%H:%M:%S.%f%z")
            self._access_token = response.json()["token"]

    def _check_response_code(self, response, expected_response_codes):
        """
        Check the requests.response.status_code to make sure it's on that we expected.
        """
        if response.status_code in expected_response_codes:
            pass
        else:
            raise ApiError(response)

    def _print_debug_response(self, response):
        """
        Print the debug logging, based on the returned content type.
        """

        # If it's supposed to be a JSON response, parse and log, otherwise, log the raw text
        if "application/json" in response.headers.get("Content-Type", "").lower():
            try:
                logger.debug(json.dumps(response.json(), indent=2))
            except ValueError:
                logger.warning("Error parsing JSON response body")
        else:
            logger.debug(response.text)

    def _get_access_token(self):
        """
        A method to fetch a new access token from Lacework.

        :return requests response
        """

        logger.info("Creating Access Token in Lacework...")

        uri = f"{self._base_url}/api/v2/access/tokens"

        # Build the access token request headers
        headers = {
            "X-LW-UAKS": self._api_secret,
            "Content-Type": "application/json",
            "User-Agent": f"laceworksdk-python-client/{version}"
        }

        # Build the access token request data
        data = {
            "keyId": self._api_key,
            "expiryTime": DEFAULT_ACCESS_TOKEN_EXPIRATION
        }

        try:
            response = self._session.post(uri, json=data, headers=headers)

            # Validate the response
            self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

            self._print_debug_response(response)

        except Exception:
            raise ApiError(response)

        return response

    def _get_request_headers(self, org_access=False):
        """
        A method to build the HTTP request headers for Lacework.

        :param org_access: boolean representing whether the request should be performed at the Organization level
        """

        # Build the request headers
        headers = self._session.headers

        headers["Authorization"] = self._access_token
        headers["Org-Access"] = "true" if org_access else "false"
        headers["User-Agent"] = f"laceworksdk-python-client/{version}"

        if self._subaccount:
            headers["Account-Name"] = self._subaccount

        logger.debug("Request headers: \n" + json.dumps(dict(headers), indent=2))

        return headers

    def get(self, uri, org=False):
        """
        :param uri: uri to send the HTTP GET request to
        :param org: boolean representing whether the request should be performed at the Organization level

        :return: response json

        :raises: ApiError if unable to get a connection
        """

        self._check_access_token()

        uri = f"{self._base_url}{uri}"

        logger.info(f"GET request to URI: {uri}")

        # Perform a GET request
        response = self._session.get(uri, headers=self._get_request_headers(org_access=org))

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        return response

    def patch(self, uri, org=False, data=None, param=None):
        """
        :param uri: uri to send the HTTP POST request to
        :param org: boolean representing whether the request should be performed at the Organization level
        :param data: json object containing the data
        :param param: python object containing the parameters

        :return: response json

        :raises: ApiError if unable to get a connection
        """

        self._check_access_token()

        uri = f"{self._base_url}{uri}"

        logger.info(f"PATCH request to URI: {uri}")
        logger.info(f"PATCH request data:\n{data}")

        # Perform a PATCH request
        response = self._session.patch(uri, params=param, json=data, headers=self._get_request_headers(org_access=org))

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        return response

    def post(self, uri, org=False, data=None, param=None):
        """
        :param uri: uri to send the HTTP POST request to
        :param org: boolean representing whether the request should be performed at the Organization level
        :param data: json object containing the data
        :param param: python object containing the parameters

        :return: response json

        :raises: ApiError if unable to get a connection
        """

        self._check_access_token()

        uri = f"{self._base_url}{uri}"

        logger.info(f"POST request to URI: {uri}")
        logger.info(f"POST request data:\n{data}")

        # Perform a POST request
        response = self._session.post(uri, params=param, json=data, headers=self._get_request_headers(org_access=org))

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        return response

    def put(self, uri, org=False, data=None, param=None):
        """
        :param uri: uri to send the HTTP POST request to
        :param org: boolean representing whether the request should be performed at the Organization level
        :param data: json object containing the data
        :param param: python object containing the parameters

        :return: response json

        :raises: ApiError if unable to get a connection
        """

        self._check_access_token()

        uri = f"{self._base_url}{uri}"

        logger.info(f"PUT request to URI: {uri}")
        logger.info(f"PUT request data:\n{data}")

        # Perform a PUT request
        response = self._session.put(uri, params=param, json=data, headers=self._get_request_headers(org_access=org))

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        return response

    def delete(self, uri, org=False):
        """
        :param uri: uri to send the http DELETE request to
        :param org: boolean representing whether the request should be performed at the Organization level

        :response: reponse json

        :raises: ApiError if unable to get a connection
        """

        self._check_access_token()

        uri = f"{self._base_url}{uri}"

        logger.info(f"DELETE request to URI: {uri}")

        # Perform a DELETE request
        response = self._session.delete(uri, headers=self._get_request_headers(org_access=org))

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        return response
