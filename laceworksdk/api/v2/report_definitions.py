# -*- coding: utf-8 -*-
"""Lacework ReportDefinitions API wrapper."""

from laceworksdk.api.crud_endpoint import CrudEndpoint


class ReportDefinitionsAPI(CrudEndpoint):

    def __init__(self, session):
        """Initializes the ReportDefinitionsAPI object.

        Args:
          session: An instance of the HttpSession class

        :return ReportDefinitionsAPI object.

        Returns:

        """
        super().__init__(session, "ReportDefinitions")

    def create(self,
               report_name,
               report_type,
               sub_report_type,
               report_definition,
               props,
               alert_channels,
               distribution_type,
               frequency,
               **request_params):
        """A method to create a new ReportDefinitions object.

        Args:
          report_name: A string representing the name of the report definition.
          report_type: A string representing the type of the report definition.
          sub_report_name: A string representing the sub-type of the report definition.
        ("AWS", "GCP", "Azure")
          report_definition: An object representing the the report definition.
        obj:
          sections: An array of objects representing the sections of the report definition.
          category: A string representing the section's category.
          title: A string representing the section's title.
          policies: An array of strings representing the section's policies.
          overrides: An array of objects representing the overrides of the report definition.
          title: A string representing the policy's title.
          policy: A string representing the policy ID.
          props: An object representing metadata about the report definition.
        obj:
          engine: A string representing the evaluation engine used for the report.
          integrations: An array of strings representing integrations (e.g. AWS Account IDs)
          resource_groups: An array of strings representing resource group IDs.
          alert_channels: An array of strings representing the alert channels for report distribution.
          distribution_type: A string representing the report format.
        ("csv", "html", "pdf")
          frequency: A string representing the frequency of report distribution.
        ("daily", "weekly")
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          sub_report_type: 
          **request_params: 

        Returns:

        """
        return super().create(
            report_name=report_name,
            report_type=report_type,
            sub_report_type=sub_report_type,
            report_definition=report_definition,
            props=props,
            alert_channels=alert_channels,
            distribution_type=distribution_type,
            frequency=frequency,
            **request_params
        )

    def get(self,
            id=None):
        """A method to get ReportDefinitions objects.

        Args:
          id: A string representing the object ID.
        
        :return response json (Default value = None)

        Returns:

        """
        return super().get(id=id)

    def get_by_id(self,
                  id):
        """A method to get a ReportDefinitions object by ID.

        Args:
          id: A string representing the object ID.
        
        :return response json

        Returns:

        """
        return self.get(id=id)

    def search(self, **request_params):
        """A method to 'pass' when attempting to search ReportDefinitions objects.
        
        Search functionality is not yet implemented for Alert Profiles.

        Args:
          **request_params: 

        Returns:

        """
        pass

    def update(self,
               id,
               report_name,
               report_type,
               sub_report_type,
               report_definition,
               props=None,
               alert_channels=None,
               distribution_type=None,
               frequency=None,
               update_type=None,
               **request_params):
        """A method to update an ReportDefinitions object.

        Args:
          id: A string representing the object ID.
          report_name: A string representing the name of the report definition.
          report_type: A string representing the type of the report definition.
          sub_report_name: A string representing the sub-type of the report definition.
        ("AWS", "GCP", "Azure")
          report_definition: An object representing the the report definition.
        obj:
          sections: An array of objects representing the sections of the report definition.
          category: A string representing the section's category.
          title: A string representing the section's title.
          policies: An array of strings representing the section's policies.
          overrides: An array of objects representing the overrides of the report definition.
          title: A string representing the policy's title.
          policy: A string representing the policy ID.
          props: An object representing metadata about the report definition.
        obj: (Default value = None)
          engine: A string representing the evaluation engine used for the report.
          integrations: An array of strings representing integrations (e.g. AWS Account IDs)
          resource_groups: An array of strings representing resource group IDs.
          alert_channels: An array of strings representing the alert channels for report distribution. (Default value = None)
          distribution_type: A string representing the report format.
        ("csv", "html", "pdf") (Default value = None)
          frequency: A string representing the frequency of report distribution.
        ("daily", "weekly") (Default value = None)
          update_type: A string representing the type of update for the report definition.
        ("Update", "Revert") (Default value = None)
          request_params: Additional request parameters.
        (provides support for parameters that may be added in the future)
        
        :return response json
          sub_report_type: 
          **request_params: 

        Returns:

        """
        json = self.build_dict_from_items(
            report_name=report_name,
            report_type=report_type,
            sub_report_type=sub_report_type,
            report_definition=report_definition,
            props=props,
            alert_channels=alert_channels,
            distribution_type=distribution_type,
            frequency=frequency,
            update_type=update_type,
            **request_params
        )

        response = self._session.put(self.build_url(id=id), json=json)

        return response.json()

    def delete(self,
               id):
        """A method to delete a ReportDefinitions object.

        Args:
          guid: A string representing the object ID.
        
        :return response json
          id: 

        Returns:

        """
        return super().delete(id=id)
