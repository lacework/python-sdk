# -*- coding: utf-8 -*-
"""Lacework Exceptions API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class PolicyExceptionsAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the PolicyExceptionsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return PolicyExceptionsAPI object.

        Returns:

        """
        super().__init__(session, "Exceptions")

    def create(self,
               policy_id,
               description,
               constraints,
               **request_params):
        """A method to create a new Exceptions object.

        Args:
          policy_id: A string representing the object policy ID.
          description: A string representing the object description.
          constraints: A string representing the object contraints.
        :obj
          field_key: A string representing the contraint key
        ('accountIds', 'resourceNames', 'regionNames' and 'resourceTags')
          field_values: An array of strings representing constraint values
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

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
        """A method to get Exceptions objects.

        Args:
          exception_id: A string representing the exception ID. (Default value = None)
          policy_id: A string representing the object policy ID.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=exception_id, policy_id=policy_id)

    def get_by_id(self,
                  exception_id,
                  policy_id):
        """A method to get a Exceptions object by policy ID.

        Args:
          exception_id: A string representing the exception ID.
          policy_id: A string representing the object policy ID.
        
        :return response json

        Returns:

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
        """A method to create a new Exceptions object.

        Args:
          exception_id: A string representing the exception ID.
          policy_id: A string representing the object policy ID.
          description: A string representing the object description. (Default value = None)
          constraints: A string representing the object contraints.
        :obj (Default value = None)
          field_key: A string representing the contraint key
        ('accountIds', 'resourceNames', 'regionNames' and 'resourceTags')
          field_values: An array of strings representing constraint values
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          **request_params: 

        Returns:

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
        """A method to delete an Exceptions object.

        Args:
          exception_id: A string representing the exception ID.
          policy_id: A string representing the object policy ID.
        
        :return response json

        Returns:

        """
        params = self.build_dict_from_items(
            policy_id=policy_id
        )

        return super().delete(id=exception_id, params=params)
