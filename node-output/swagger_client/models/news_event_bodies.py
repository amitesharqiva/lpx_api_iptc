# coding: utf-8

"""
    News Events API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NewsEventBodies(object):
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
        'charcount': 'int',
        'wordcount': 'int',
        'role': 'str',
        'value': 'str'
    }

    attribute_map = {
        'charcount': 'charcount',
        'wordcount': 'wordcount',
        'role': 'role',
        'value': 'value'
    }

    def __init__(self, charcount=None, wordcount=None, role=None, value=None):  # noqa: E501
        """NewsEventBodies - a model defined in Swagger"""  # noqa: E501
        self._charcount = None
        self._wordcount = None
        self._role = None
        self._value = None
        self.discriminator = None
        if charcount is not None:
            self.charcount = charcount
        if wordcount is not None:
            self.wordcount = wordcount
        if role is not None:
            self.role = role
        if value is not None:
            self.value = value

    @property
    def charcount(self):
        """Gets the charcount of this NewsEventBodies.  # noqa: E501


        :return: The charcount of this NewsEventBodies.  # noqa: E501
        :rtype: int
        """
        return self._charcount

    @charcount.setter
    def charcount(self, charcount):
        """Sets the charcount of this NewsEventBodies.


        :param charcount: The charcount of this NewsEventBodies.  # noqa: E501
        :type: int
        """

        self._charcount = charcount

    @property
    def wordcount(self):
        """Gets the wordcount of this NewsEventBodies.  # noqa: E501


        :return: The wordcount of this NewsEventBodies.  # noqa: E501
        :rtype: int
        """
        return self._wordcount

    @wordcount.setter
    def wordcount(self, wordcount):
        """Sets the wordcount of this NewsEventBodies.


        :param wordcount: The wordcount of this NewsEventBodies.  # noqa: E501
        :type: int
        """

        self._wordcount = wordcount

    @property
    def role(self):
        """Gets the role of this NewsEventBodies.  # noqa: E501


        :return: The role of this NewsEventBodies.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NewsEventBodies.


        :param role: The role of this NewsEventBodies.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def value(self):
        """Gets the value of this NewsEventBodies.  # noqa: E501


        :return: The value of this NewsEventBodies.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NewsEventBodies.


        :param value: The value of this NewsEventBodies.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(NewsEventBodies, dict):
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
        if not isinstance(other, NewsEventBodies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
