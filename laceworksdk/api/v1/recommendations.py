"""
Lacework Recommendations API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class RecommendationsAPI:
    """
    Lacework Recommendations API.
    """

    def __init__(self, session):
        """
        Initializes the RecommendationsAPI object.

        :param session: An instance of the HttpSession class

        :return RecommendationsAPI object.
        """

        super().__init__()

        self._session = session

    def get(self,
            type):
        """
        A method to get all compliance recommendations for the specified Cloud Service Provider.

        :param type: A string representing the type of CSP recommendations to retreive.
            ('aws', 'azure', or 'gcp')

        :return response json
        """

        logger.info(f"Getting {type} recommendations from Lacework...")

        # Build the Recommendations request URI
        api_uri = f"/api/v1/external/recommendations/{type}"

        response = self._session.get(api_uri)

        return response.json()

    def update(self,
               type,
               data):
        """
        A method to update compliance recommendations for the specified Cloud Service Provider.

        :param type: A string representing the type of CSP recommendations to update.
            ('aws', 'azure', or 'gcp')
        :param data: A JSON object representing which checks to enable/disable.

        :return response json
        """

        logger.info(f"Updating {type} recommendations in Lacework...")

        # Build the Recommendations request URI
        api_uri = f"/api/v1/external/recommendations/{type}"

        response = self._session.patch(api_uri, data=data)

        return response.json()
