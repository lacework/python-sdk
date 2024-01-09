# -*- coding: utf-8 -*-
"""Lacework Queries API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class QueriesAPI(CrudEndpoint):
    """A class used to represent the `Queries API endpoint <https://docs.lacework.net/api/v2/docs/#tag/Queries>`_

    Queries are the mechanism used to interactively request information from a specific curated datasource. \
    Queries have a defined structure for authoring detections.
    """

    def __init__(self, session):
        """Initializes the QueriesAPI object.

        Args:
          session (HttpSession): An instance of the HttpSession class

        Returns:
            QueriesAPI: An instance of this class

        """
        super().__init__(session, "Queries")

    def create(self, query_id, query_text, evaluator_id=None, **request_params):
        """A method to create a new Queries object.

        Args:
          query_id (str): Name of the new query.
          query_text (str): The object query text.
          evaluator_id (str, optional): A string representing the evaluator in which the \
          query is to be run.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The newly created query

        """
        return super().create(
            query_id=query_id,
            query_text=query_text,
            evaluator_id=evaluator_id,
            **request_params,
        )

    def get(self, query_id=None):
        """A method to get registered queries. Using no args will get all registered queries.

        Args:
          query_id (str, optional): The query ID to get.

        Returns:
            dict: The requested querie(s)

        """
        return super().get(id=query_id)

    def get_by_id(self, query_id):
        """A method to get a Queries object by query ID.

        Args:
          query_id (str): The query ID to get.

        Returns:
            dict: The requested querie(s)

        """
        return self.get(query_id=query_id)

    def execute(self, evaluator_id=None, query_id=None, query_text=None, arguments={}):
        """A method to execute a Queries object.

        Args:
          evaluator_id (str, optional): The evaluator in which the query object is to be run.
          query_id (str, optional): The query ID.
          query_text (str): The query text.
          arguments (dict of str: str): A dictionary of key/value pairs to be used as arguments in the query object.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The query results

        """
        json = {"arguments": []}

        # Build the Queries request URI
        if query_id is None:
            json["query"] = {"queryText": query_text}
            if evaluator_id:
                json["query"]["evaluatorId"] = evaluator_id

        for key, value in arguments.items():
            json["arguments"].append({"name": key, "value": value})

        response = self._session.post(self._build_url(action="execute"), json=json)

        return response.json()

    def execute_by_id(self, query_id, arguments={}):
        """A method to execute a Queries object by query ID.

        Args:
          query_id (str): The query ID to execute
          arguments (dict of str: str): A dictionary of key/value pairs to be used as arguments in the query object.

        Returns:
            dict: The query results
        """
        json = {"arguments": []}

        for key, value in arguments.items():
            json["arguments"].append({"name": key, "value": value})

        response = self._session.post(
            self._build_url(resource=query_id, action="execute"), json=json
        )

        return response.json()

    def validate(self, query_text, evaluator_id=None, **request_params):
        """A method to validate a Queries object.

        Args:
          query_text (str): The query text to validate
          evaluator_id (str, optional): The evaluator in which the query is to be run.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: Validation Results
        """
        json = self._build_dict_from_items(
            request_params, query_text=query_text, evaluator_id=evaluator_id
        )

        response = self._session.post(self._build_url(action="validate"), json=json)

        return response.json()

    def update(self, query_id, query_text, **request_params):
        """A method to update a Queries object.

        Args:
          query_id (str): Name of the new query.
          query_text (str, optional): The object query text.
          request_params (dict, optional): Use to pass any additional parameters the API

        Returns:
            dict: The updated created query

        """
        return super().update(id=query_id, query_text=query_text, **request_params)

    def delete(self, query_id):
        """A method to delete a query.

        Args:
          query_id (str): The ID of the query to delete

        Returns:
            requests.models.Response: a Requests response object containing the response code

        """
        return super().delete(id=query_id)
