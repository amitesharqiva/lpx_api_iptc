# coding: utf-8

"""
    LPX API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'eventstatus': 'EventStatus',
        'dates': 'DatesobjectType',
        'organiser': 'OrganisationType'
    }

    attribute_map = {
        'eventstatus': 'eventstatus',
        'dates': 'dates',
        'organiser': 'organiser'
    }

    def __init__(self, eventstatus=None, dates=None, organiser=None):  # noqa: E501
        """EventDetails - a model defined in Swagger"""  # noqa: E501
        self._eventstatus = None
        self._dates = None
        self._organiser = None
        self.discriminator = None
        if eventstatus is not None:
            self.eventstatus = eventstatus
        if dates is not None:
            self.dates = dates
        if organiser is not None:
            self.organiser = organiser

    @property
    def eventstatus(self):
        """Gets the eventstatus of this EventDetails.  # noqa: E501


        :return: The eventstatus of this EventDetails.  # noqa: E501
        :rtype: EventStatus
        """
        return self._eventstatus

    @eventstatus.setter
    def eventstatus(self, eventstatus):
        """Sets the eventstatus of this EventDetails.


        :param eventstatus: The eventstatus of this EventDetails.  # noqa: E501
        :type: EventStatus
        """

        self._eventstatus = eventstatus

    @property
    def dates(self):
        """Gets the dates of this EventDetails.  # noqa: E501


        :return: The dates of this EventDetails.  # noqa: E501
        :rtype: DatesobjectType
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this EventDetails.


        :param dates: The dates of this EventDetails.  # noqa: E501
        :type: DatesobjectType
        """

        self._dates = dates

    @property
    def organiser(self):
        """Gets the organiser of this EventDetails.  # noqa: E501


        :return: The organiser of this EventDetails.  # noqa: E501
        :rtype: OrganisationType
        """
        return self._organiser

    @organiser.setter
    def organiser(self, organiser):
        """Sets the organiser of this EventDetails.


        :param organiser: The organiser of this EventDetails.  # noqa: E501
        :type: OrganisationType
        """

        self._organiser = organiser

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EventDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
