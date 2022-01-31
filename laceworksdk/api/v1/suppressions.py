"""
Lacework Suppressions API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class SuppressionsAPI:
    """
    Lacework Suppressions API.
    """

    def __init__(self, session):
        """
        Initializes the SuppressionsAPI object.

        :param session: An instance of the HttpSession class

        :return SuppressionsAPI object.
        """

        super().__init__()

        self._session = session

    def create(self,
               type,
               data):
        """
        A method to create supressions.

        :param type: A string representing the type of CSP supression(s) to create.
            ('aws', 'azure', or 'gcp')
        :param data: A JSON object containing the supression(s) to create

        :return response json
        """

        logger.info("Creating supression(s) in Lacework...")

        # Build the Suppressions request URI
        api_uri = f"/api/v1/external/suppressions/{type}"

        response = self._session.post(api_uri, data=data)

        return response.json()

    def get(self,
            type,
            recommendation_id=None):
        """
        A method to get supressions.

        :param type: A string representing the type of CSP suppression(s) to retreive.
            ('aws', 'azure', or 'gcp')
        :param recommendation_id: A string representing the recommendation ID to retreive.

        :return response json
        """

        # Log/Build the Suppressions request URI
        if recommendation_id:
            logger.info(f"Getting {type} suppression {recommendation_id} from Lacework...")
            api_uri = f"/api/v1/external/suppressions/{type}/allExceptions/{recommendation_id}"
        else:
            logger.info(f"Getting {type} suppressions from Lacework...")
            api_uri = f"/api/v1/external/suppressions/{type}/allExceptions"

        response = self._session.get(api_uri)

        return response.json()

    def delete(self,
               type,
               data):
        """
        A method to delete supressions.

        :param type: A string representing the type of CSP suppression(s) to delete.
            ('aws', 'azure', or 'gcp')
        :param data: A JSON object containing the supression(s) to create

        :return response json
        """

        logger.info("Deleting supression(s) in Lacework...")

        # Build the Suppressions request URI
        api_uri = f"/api/v1/external/suppressions/{type}"

        response = self._session.delete(api_uri, data=data)

        if response.status_code == 204:
            return response
        else:
            return response.json()
