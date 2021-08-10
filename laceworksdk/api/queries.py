# -*- coding: utf-8 -*-
"""
Lacework Queries API wrapper.
"""

import logging

logger = logging.getLogger(__name__)


class QueriesAPI(object):

    def __init__(self, session):
        """
        Initializes the QueriesAPI object.

        :param session: An instance of the HttpSession class

        :return QueriesAPI object.
        """

        super(QueriesAPI, self).__init__()

        self._session = session

    def create(self,
               evaluator_id,
               query_id,
               query_text,
               org=False):
        """
        A method to create a new Lacework Query Language (LQL) query.

        :param evaluator_id: A string representing the evaluator in which the policy is to be run.
        :param query_id: A string representing the LQL query ID.
        :param query_text: A string representing the LQL query text.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Creating LQL query in Lacework...")

        # Build the Queries request URI
        api_uri = "/api/v2/Queries"

        data = {
            "evaluatorId": evaluator_id,
            "queryId": query_id,
            "queryText": query_text
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def get(self,
            query_id=None,
            org=False):
        """
        A method to get LQL queries.

        :param query_id: A string representing the LQL query ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Getting LQL query info from Lacework...")

        # Build the Queries request URI
        if query_id:
            api_uri = f"/api/v2/Queries/{query_id}"
        else:
            api_uri = "/api/v2/Queries"

        response = self._session.get(api_uri, org=org)

        return response.json()

    def get_by_id(self,
                  query_id,
                  org=False):
        """
        A method to get an LQL query by query ID.

        :param query_id: A string representing the LQL query ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.get(query_id=query_id, org=org)

    def execute(self,
                evaluator_id=None,
                query_id=None,
                query_text=None,
                arguments={},
                org=False):
        """
        A method to execute a Lacework Query Language (LQL) query.

        :param evaluator_id: A string representing the evaluator in which the policy is to be run.
        :param query_id: A string representing the LQL query ID.
        :param query_text: A string representing the LQL query text.
        :param arguments: A dictionary of key/value pairs to be used as arguments in the LQL query.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Executing LQL query in Lacework...")

        data = {
            "arguments": []
        }

        # Build the Queries request URI
        if query_id:
            api_uri = f"/api/v2/Queries/{query_id}/execute"
        else:
            api_uri = "/api/v2/Queries/execute"

            data["query"] = {
                "evaluatorId": evaluator_id,
                "queryText": query_text
            }

        for key, value in arguments.items():
            data["arguments"].append({
                "name": key,
                "value": value
            })

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def execute_by_id(self,
                      query_id,
                      arguments={},
                      org=False):
        """
        A method to execute a Lacework Query Language (LQL) query.

        :param query_id: A string representing the LQL query ID.
        :param arguments: A dictionary of key/value pairs to be used as arguments in the LQL query.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        return self.execute(query_id=query_id, arguments=arguments, org=org)

    def validate(self,
                 evaluator_id,
                 query_text,
                 org=False):
        """
        A method to validate a Lacework Query Language (LQL) query.

        :param evaluator_id: A string representing the evaluator in which the policy is to be run.
        :param query_text: A string representing the LQL query text.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Validating LQL query in Lacework...")

        # Build the Queries request URI
        api_uri = "/api/v2/Queries/validate"

        data = {
            "evaluatorId": evaluator_id,
            "queryText": query_text
        }

        response = self._session.post(api_uri, org=org, data=data)

        return response.json()

    def update(self,
               query_id,
               query_text,
               org=False):
        """
        A method to update a Lacework Query Language (LQL) query.

        :param query_id: A string representing the LQL query ID.
        :param query_text: A string representing the LQL query text.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Updating LQL query in Lacework...")

        # Build the Queries request URI
        api_uri = f"/api/v2/Queries/{query_id}"

        data = {
            "queryText": query_text
        }

        response = self._session.patch(api_uri, org=org, data=data)

        return response.json()

    def delete(self,
               query_id,
               org=False):
        """
        A method to delete a Lacework Query Language (LQL) query.

        :param query_id: A string representing the LQL query ID.
        :param org: A boolean representing whether the request should be performed
            at the Organization level

        :return response json
        """

        logger.info("Deleting LQL query in Lacework...")

        # Build the Queries request URI
        api_uri = f"/api/v2/Queries/{query_id}"

        response = self._session.delete(api_uri, org=org)

        if response.status_code == 204:
            return response
        else:
            return response.json()
