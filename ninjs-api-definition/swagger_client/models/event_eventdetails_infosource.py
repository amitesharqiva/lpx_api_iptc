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

class EventEventdetailsInfosource(object):
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
        'role': 'str',
        'uri': 'str',
        'literal': 'str',
        'contactinfo': 'list[EventEventdetailsContactinfo]'
    }

    attribute_map = {
        'name': 'name',
        'role': 'role',
        'uri': 'uri',
        'literal': 'literal',
        'contactinfo': 'contactinfo'
    }

    def __init__(self, name=None, role=None, uri=None, literal=None, contactinfo=None):  # noqa: E501
        """EventEventdetailsInfosource - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._role = None
        self._uri = None
        self._literal = None
        self._contactinfo = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if uri is not None:
            self.uri = uri
        if literal is not None:
            self.literal = literal
        if contactinfo is not None:
            self.contactinfo = contactinfo

    @property
    def name(self):
        """Gets the name of this EventEventdetailsInfosource.  # noqa: E501


        :return: The name of this EventEventdetailsInfosource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventEventdetailsInfosource.


        :param name: The name of this EventEventdetailsInfosource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this EventEventdetailsInfosource.  # noqa: E501


        :return: The role of this EventEventdetailsInfosource.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EventEventdetailsInfosource.


        :param role: The role of this EventEventdetailsInfosource.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def uri(self):
        """Gets the uri of this EventEventdetailsInfosource.  # noqa: E501


        :return: The uri of this EventEventdetailsInfosource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventEventdetailsInfosource.


        :param uri: The uri of this EventEventdetailsInfosource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def literal(self):
        """Gets the literal of this EventEventdetailsInfosource.  # noqa: E501


        :return: The literal of this EventEventdetailsInfosource.  # noqa: E501
        :rtype: str
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this EventEventdetailsInfosource.


        :param literal: The literal of this EventEventdetailsInfosource.  # noqa: E501
        :type: str
        """

        self._literal = literal

    @property
    def contactinfo(self):
        """Gets the contactinfo of this EventEventdetailsInfosource.  # noqa: E501


        :return: The contactinfo of this EventEventdetailsInfosource.  # noqa: E501
        :rtype: list[EventEventdetailsContactinfo]
        """
        return self._contactinfo

    @contactinfo.setter
    def contactinfo(self, contactinfo):
        """Sets the contactinfo of this EventEventdetailsInfosource.


        :param contactinfo: The contactinfo of this EventEventdetailsInfosource.  # noqa: E501
        :type: list[EventEventdetailsContactinfo]
        """

        self._contactinfo = contactinfo

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
        if issubclass(EventEventdetailsInfosource, dict):
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
        if not isinstance(other, EventEventdetailsInfosource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
