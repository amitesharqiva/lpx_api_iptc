# coding: utf-8

"""
    Events API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventPeople(object):
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
        'name': 'str',
        'contactinfo': 'list[EventContactinfo1]',
        'relationship': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contactinfo': 'contactinfo',
        'relationship': 'relationship'
    }

    def __init__(self, name=None, contactinfo=None, relationship=None):  # noqa: E501
        """EventPeople - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._contactinfo = None
        self._relationship = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if contactinfo is not None:
            self.contactinfo = contactinfo
        if relationship is not None:
            self.relationship = relationship

    @property
    def name(self):
        """Gets the name of this EventPeople.  # noqa: E501


        :return: The name of this EventPeople.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventPeople.


        :param name: The name of this EventPeople.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def contactinfo(self):
        """Gets the contactinfo of this EventPeople.  # noqa: E501


        :return: The contactinfo of this EventPeople.  # noqa: E501
        :rtype: list[EventContactinfo1]
        """
        return self._contactinfo

    @contactinfo.setter
    def contactinfo(self, contactinfo):
        """Sets the contactinfo of this EventPeople.


        :param contactinfo: The contactinfo of this EventPeople.  # noqa: E501
        :type: list[EventContactinfo1]
        """

        self._contactinfo = contactinfo

    @property
    def relationship(self):
        """Gets the relationship of this EventPeople.  # noqa: E501


        :return: The relationship of this EventPeople.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this EventPeople.


        :param relationship: The relationship of this EventPeople.  # noqa: E501
        :type: str
        """

        self._relationship = relationship

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
        if issubclass(EventPeople, dict):
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
        if not isinstance(other, EventPeople):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
