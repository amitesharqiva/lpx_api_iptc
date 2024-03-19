# coding: utf-8

"""
    LPX API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventObjects(object):
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
        'rel': 'str',
        'uri': 'str',
        'literal': 'str'
    }

    attribute_map = {
        'name': 'name',
        'rel': 'rel',
        'uri': 'uri',
        'literal': 'literal'
    }

    def __init__(self, name=None, rel=None, uri=None, literal=None):  # noqa: E501
        """EventObjects - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._rel = None
        self._uri = None
        self._literal = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if rel is not None:
            self.rel = rel
        if uri is not None:
            self.uri = uri
        if literal is not None:
            self.literal = literal

    @property
    def name(self):
        """Gets the name of this EventObjects.  # noqa: E501


        :return: The name of this EventObjects.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventObjects.


        :param name: The name of this EventObjects.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rel(self):
        """Gets the rel of this EventObjects.  # noqa: E501


        :return: The rel of this EventObjects.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this EventObjects.


        :param rel: The rel of this EventObjects.  # noqa: E501
        :type: str
        """

        self._rel = rel

    @property
    def uri(self):
        """Gets the uri of this EventObjects.  # noqa: E501


        :return: The uri of this EventObjects.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventObjects.


        :param uri: The uri of this EventObjects.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def literal(self):
        """Gets the literal of this EventObjects.  # noqa: E501


        :return: The literal of this EventObjects.  # noqa: E501
        :rtype: str
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this EventObjects.


        :param literal: The literal of this EventObjects.  # noqa: E501
        :type: str
        """

        self._literal = literal

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
        if issubclass(EventObjects, dict):
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
        if not isinstance(other, EventObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
