# -*- coding: utf-8 -*-
"""
Lacework Queries API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class QueriesAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the QueriesAPI object.

        :param session: An instance of the HttpSession class

        :return QueriesAPI object.
        """

        super().__init__(session, "Queries")

    def create(self,
               query_id,
               query_text,
               evaluator_id=None,
               **request_params):
        """
        A method to create a new Queries object.

        :param query_id: A string representing the object query ID.
        :param query_text: A string representing the object query text.
        :param evaluator_id: A string representing the evaluator in which the
                query is to be run. This is an optional parameter, with the
                default behaviour of omitting the value while sending the API call.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().create(
            query_id=query_id,
            query_text=query_text,
            evaluator_id=evaluator_id,
            **request_params
        )

    def get(self,
            query_id=None):
        """
        A method to get Queries objects.

        :param query_id: A string representing the object query ID.

        :return response json
        """

        return super().get(id=query_id)

    def get_by_id(self,
                  query_id):
        """
        A method to get a Queries object by query ID.

        :param query_id: A string representing the object query ID.

        :return response json
        """

        return self.get(query_id=query_id)

    def execute(self,
                evaluator_id=None,
                query_id=None,
                query_text=None,
                arguments={}):
        """
        A method to execute a Queries object.

        :param evaluator_id: A string representing the evaluator in which the query object is to be run.
        :param query_id: A string representing the object query ID.
        :param query_text: A string representing the object query text.
        :param arguments: A dictionary of key/value pairs to be used as arguments in the query object.

        :return response json
        """

        json = {
            "arguments": []
        }

        # Build the Queries request URI
        if query_id is None:
            json["query"] = {
                "queryText": query_text
            }
            if evaluator_id:
                json["query"]["evaluatorId"] = evaluator_id

        for key, value in arguments.items():
            json["arguments"].append({
                "name": key,
                "value": value
            })

        response = self._session.post(self.build_url(action="execute"), json=json)

        return response.json()

    def execute_by_id(self,
                      query_id,
                      arguments={}):
        """
        A method to execute a Queries object by query ID.

        :param query_id: A string representing the object query ID.
        :param arguments: A dictionary of key/value pairs to be used as arguments in the query object.

        :return response json
        """

        json = {
            "arguments": []
        }

        for key, value in arguments.items():
            json["arguments"].append({
                "name": key,
                "value": value
            })

        response = self._session.post(self.build_url(resource=query_id, action="execute"), json=json)

        return response.json()

    def validate(self,
                 query_text,
                 evaluator_id=None,
                 **request_params):
        """
        A method to validate a Queries object.

        :param query_text: A string representing the object query text.
        :param evaluator_id: A string representing the evaluator in which the
                query is to be run. Optional parameter, defaults to omitting
                the evaluator from the validation request.

        :return response json
        """

        json = self.build_dict_from_items(
            request_params,
            query_text=query_text,
            evaluator_id=evaluator_id
        )

        response = self._session.post(self.build_url(action="validate"), json=json)

        return response.json()

    def update(self,
               query_id,
               query_text,
               **request_params):
        """
        A method to update a Queries object.

        :param query_id: A string representing the object query ID.
        :param query_text: A string representing the object query text.
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        return super().update(
            id=query_id,
            query_text=query_text,
            **request_params
        )

    def delete(self,
               query_id):
        """
        A method to delete a Queries object.

        :param query_id: A string representing the object query ID.

        :return response json
        """

        return super().delete(id=query_id)
