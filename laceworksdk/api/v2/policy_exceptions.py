# -*- coding: utf-8 -*-
"""
Lacework Exceptions API wrapper.
"""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PolicyExceptionsAPI(CrudEndpoint):

    def __init__(self, session):
        """
        Initializes the PolicyExceptionsAPI object.

        :param session: An instance of the HttpSession class

        :return PolicyExceptionsAPI object.
        """

        super().__init__(session, "Exceptions")

    def create(self,
               policy_id,
               description,
               constraints,
               **request_params):
        """
        A method to create a new Exceptions object.

        :param policy_id: A string representing the object policy ID.
        :param description: A string representing the object description.
        :param constraints: A string representing the object contraints.
            :obj
                :param field_key: A string representing the contraint key
                    ('accountIds', 'resourceNames', 'regionNames' and 'resourceTags')
                :param field_values: An array of strings representing constraint values
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            policy_id=policy_id
        )

        return super().create(
            params=params,
            description=description,
            constraints=constraints,
            **request_params
        )

    def get(self,
            exception_id=None,
            policy_id=None):
        """
        A method to get Exceptions objects.

        :param exception_id: A string representing the exception ID.
        :param policy_id: A string representing the object policy ID.

        :return response json
        """

        return super().get(id=exception_id, policy_id=policy_id)

    def get_by_id(self,
                  exception_id,
                  policy_id):
        """
        A method to get a Exceptions object by policy ID.

        :param exception_id: A string representing the exception ID.
        :param policy_id: A string representing the object policy ID.

        :return response json
        """

        return self.get(
            exception_id=exception_id,
            policy_id=policy_id
        )

    def update(self,
               exception_id,
               policy_id,
               description=None,
               constraints=None,
               **request_params):
        """
        A method to create a new Exceptions object.

        :param exception_id: A string representing the exception ID.
        :param policy_id: A string representing the object policy ID.
        :param description: A string representing the object description.
        :param constraints: A string representing the object contraints.
            :obj
                :param field_key: A string representing the contraint key
                    ('accountIds', 'resourceNames', 'regionNames' and 'resourceTags')
                :param field_values: An array of strings representing constraint values
        :param request_params: Additional request parameters.
            (provides support for parameters that may be added in the future)

        :return response json
        """

        params = self.build_dict_from_items(
            policy_id=policy_id
        )

        return super().update(
            id=exception_id,
            params=params,
            description=description,
            constraints=constraints,
            **request_params
        )

    def delete(self,
               exception_id,
               policy_id):
        """
        A method to delete an Exceptions object.

        :param exception_id: A string representing the exception ID.
        :param policy_id: A string representing the object policy ID.

        :return response json
        """

        params = self.build_dict_from_items(
            policy_id=policy_id
        )

        return super().delete(id=exception_id, params=params)
