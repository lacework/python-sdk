# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import laceworksdk


class TestLaceworkSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""

        # Lacework API Wrapper
        assert hasattr(laceworksdk, "LaceworkClient")

        # Lacework Exceptions
        assert hasattr(laceworksdk, "ApiError")
        assert hasattr(laceworksdk, "laceworksdkException")
