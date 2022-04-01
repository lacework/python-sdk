# -*- coding: utf-8 -*-
"""
HttpSession class for package HTTP functions.
"""

import json
import logging
import requests

from datetime import datetime, timezone
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from laceworksdk import version
from laceworksdk.config import (
    DEFAULT_BASE_DOMAIN,
    DEFAULT_ACCESS_TOKEN_EXPIRATION,
    DEFAULT_SUCCESS_RESPONSE_CODES,
    RATE_LIMIT_RESPONSE_CODE
)
from laceworksdk.exceptions import ApiError, MalformedResponse, RateLimitError

logger = logging.getLogger(__name__)


class HttpSession:
    """
    Package HttpSession class.
    """

    _access_token = None
    _access_token_expiry = None

    def __init__(self, account, subaccount, api_key, api_secret, base_domain):
        """
        Initializes the HttpSession object.

        :param account: a Lacework Account name
        :param subaccount: a Lacework Sub-account name
        :param api_key: a Lacework API Key
        :param api_secret: a Lacework API Secret
        :param base_domain: a Lacework Domain (defaults to "lacework.net")

        :return HttpSession object.
        """

        super().__init__()

        # Create a requests session
        self._session = self._retry_session()

        # Set the base parameters
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_domain = base_domain or DEFAULT_BASE_DOMAIN
        self._base_url = f"https://{account}.{self._base_domain}"
        self._subaccount = subaccount
        self._org_level_access = False

        # Get an access token
        self._check_access_token()

    def _retry_session(self,
                       retries=3,
                       backoff_factor=0.3,
                       status_forcelist=(500, 502, 503, 504),
                       allowed_methods=None):
        """
        A method to set up automatic retries on HTTP requests that fail.
        """

        # Create a new requests session
        session = requests.Session()

        # Establish the retry criteria
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=allowed_methods,
            raise_on_status=False
        )

        # Build the adapter with the retry criteria
        adapter = HTTPAdapter(max_retries=retry_strategy)

        # Bind the adapter to HTTP/HTTPS calls
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _check_access_token(self):
        """
        A method to check the validity of the access token.
        """

        if self._access_token is None or self._access_token_expiry < datetime.now(timezone.utc):

            response = self._get_access_token()

            # Parse and restructure the returned date (necessary for Python 3.6)
            expiry_date = response.json()["expiresAt"].replace("Z", "+0000")

            # Update the access token and expiration
            self._access_token_expiry = datetime.strptime(expiry_date, "%Y-%m-%dT%H:%M:%S.%f%z")
            self._access_token = response.json()["token"]

    def _check_response_code(self, response, expected_response_codes):
        """
        Check the requests.response.status_code to make sure it's one that we expected.
        """
        if response.status_code in expected_response_codes:
            pass
        elif response.status_code == RATE_LIMIT_RESPONSE_CODE:
            raise RateLimitError(response)
        else:
            raise ApiError(response)

    def _print_debug_response(self, response):
        """
        Print the debug logging, based on the returned content type.
        """

        logger.debug(response.headers)

        # If it's supposed to be a JSON response, parse and log, otherwise, log the raw text
        if "application/json" in response.headers.get("Content-Type", "").lower():
            try:
                if response.status_code != 204:
                    logger.debug(json.dumps(response.json(), indent=2))
                else:
                    logger.debug("204 No Content Returned")
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

        response = None

        try:
            response = self._session.post(uri, json=data, headers=headers)

            # Validate the response
            self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

            self._print_debug_response(response)

        except Exception:
            if response:
                raise ApiError(response)

            logger.error("Call to _get_access_token() returned no response.")
            raise

        return response

    def _get_request_headers(self, org_access=False):
        """
        A method to build the HTTP request headers for Lacework.

        :param org_access: boolean representing whether the request should be performed at the Organization level
        """

        # Build the request headers
        headers = self._session.headers

        headers["Authorization"] = f"Bearer {self._access_token}"
        headers["Org-Access"] = "true" if self._org_level_access or org_access else "false"
        headers["User-Agent"] = f"laceworksdk-python-client/{version}"

        if self._subaccount:
            headers["Account-Name"] = self._subaccount

        logger.debug("Request headers: \n" + json.dumps(dict(headers), indent=2))

        return headers

    def _request(self, method, uri, **kwargs):
        """
        A method to abstract building requests to Lacework.

        :param method: string representing the HTTP request method ("GET", "POST", ...)
        :param uri: string representing the URI of the API endpoint
        :param kwargs: passed on to the requests package

        :return: response json

        :raises: ApiError if anything but expected response code is returned
        """

        self._check_access_token()

        # Strip the protocol/host if provided
        domain_begin = uri.find(self._base_domain)
        if domain_begin >= 0:
            domain_end = domain_begin + len(self._base_domain)
            uri = uri[domain_end:]

        uri = f"{self._base_url}{uri}"

        logger.info(f"{method} request to URI: {uri}")

        # Check for 'org' - if True, make an organization-level API call
        # TODO: Remove this on v1.0 release - this is done for back compat
        org = kwargs.pop("org", None)
        headers = self._get_request_headers(org_access=org)

        # Check for 'data' or 'json'
        data = kwargs.get("data", "")
        json = kwargs.get("json", "")
        if data or json:
            logger.debug(f"{method} request data:\nData: {data}\nJSON: {json}")

        # TODO: Remove this on v1.0 release - this is done for back compat
        if data and not json:
            kwargs["json"] = data
            kwargs.pop("data")

        # Make the HTTP request to the API endpoint
        response = self._session.request(method, uri, headers=headers, **kwargs)

        # Validate the response
        self._check_response_code(response, DEFAULT_SUCCESS_RESPONSE_CODES)

        self._print_debug_response(response)

        # Fix for when Lacework returns a 204 with no data on searches
        if method != "DELETE" and response.status_code == 204:
            try:
                response.json()
            except Exception:
                response._content = b'{"data": []}'

        return response

    def get(self, uri, params=None, **kwargs):
        """
        A method to build a GET request to interact with Lacework.

        :param uri: uri to send the HTTP GET request to
        :param params: dict of parameters for the HTTP request
        :param kwargs: passed on to the requests package

        :return: response json

        :raises: ApiError if anything but expected response code is returned
        """

        # Perform a GET request
        response = self._request("GET", uri, params=params, **kwargs)

        return response

    def get_pages(self, uri, params=None, **kwargs):
        """
        A method to build a GET request that yields pages of data returned by Lacework.

        :param uri: uri to send the initial HTTP GET request to
        :param params: dict of parameters for the HTTP request
        :param kwargs: passed on to the requests package

        :return: a generator that yields pages of data

        :raises: ApiError if anything but expected response code is returned
        """

        response = self.get(uri, params=params, **kwargs)

        while True:
            yield response

            try:
                response_json = response.json()
                next_page = response_json.get("paging", {}).get("urls", {}).get("nextPage")
            except json.JSONDecodeError:
                logger.error("Failed to decode response from Lacework as JSON.", exc_info=True)
                logger.debug(f"Response text: {response.text}")
                next_page = None

            if next_page:
                response = self.get(next_page, params=params, **kwargs)
            else:
                break

    def get_data_items(self, uri, params=None, **kwargs):
        """
        A method to build a GET request that yields individual objects as returned by Lacework.

        :param uri: uri to send the initial HTTP GET request to
        :param params: dict of parameters for the HTTP request
        :param kwargs: passed on to the requests package

        :return: a generator that yields individual objects from pages of data

        :raises: ApiError if anything but expected response code is returned
        :raises: MalformedResponse if the returned response does not contain a
                top-level dictionary with an "data" key.
        """

        # Get generator for pages of JSON data
        pages = self.get_pages(uri, params=params, **kwargs)

        for page in pages:
            page = page.json()
            assert isinstance(page, dict)

            items = page.get("data")

            if items is None:
                error_message = f"'data' key not found in JSON data:\n{page}"
                raise MalformedResponse(error_message)

            for item in items:
                yield item

    def patch(self, uri, data=None, json=None, **kwargs):
        """
        A method to build a PATCH request to interact with Lacework.

        :param uri: uri to send the HTTP POST request to
        :param data: data to be sent in the body of the request
        :param json: data to be sent in JSON format in the body of the request
        :param kwargs: passed on to the requests package

        :return: response json

        :raises: ApiError if anything but expected response code is returned
        """

        # Perform a PATCH request
        response = self._request("PATCH", uri, data=data, json=json, **kwargs)

        return response

    def post(self, uri, data=None, json=None, **kwargs):
        """
        A method to build a POST request to interact with Lacework.

        :param uri: uri to send the HTTP POST request to
        :param data: data to be sent in the body of the request
        :param json: data to be sent in JSON format in the body of the request
        :param kwargs: passed on to the requests package

        :return: response json

        :raises: ApiError if anything but expected response code is returned
        """

        # Perform a POST request
        response = self._request("POST", uri, data=data, json=json, **kwargs)

        return response

    def put(self, uri, data=None, json=None, **kwargs):
        """
        A method to build a PUT request to interact with Lacework.

        :param uri: uri to send the HTTP POST request to
        :param data: data to be sent in the body of the request
        :param json: data to be sent in JSON format in the body of the request
        :param kwargs: passed on to the requests package

        :return: response json

        :raises: ApiError if anything but expected response code is returned
        """

        # Perform a PUT request
        response = self._request("PUT", uri, data=data, json=json, **kwargs)

        return response

    def delete(self, uri, data=None, json=None, **kwargs):
        """
        A method to build a DELETE request to interact with Lacework.

        :param uri: uri to send the http DELETE request to
        :param data: data to be sent in the body of the request
        :param json: data to be sent in JSON format in the body of the request
        :param kwargs: passed on to the requests package

        :response: reponse json

        :raises: ApiError if anything but expected response code is returned
        """

        # Perform a DELETE request
        response = self._request("DELETE", uri, data=data, json=json, **kwargs)

        return response
