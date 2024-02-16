# coding: utf-8

"""
    LPX API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrganisationType(object):
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
        'literal': 'str',
        'symbols': 'list[object]',
        'contactinfo': 'list[ContactinfoType]'
    }

    attribute_map = {
        'name': 'name',
        'rel': 'rel',
        'uri': 'uri',
        'literal': 'literal',
        'symbols': 'symbols',
        'contactinfo': 'contactinfo'
    }

    def __init__(self, name=None, rel=None, uri=None, literal=None, symbols=None, contactinfo=None):  # noqa: E501
        """OrganisationType - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._rel = None
        self._uri = None
        self._literal = None
        self._symbols = None
        self._contactinfo = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if rel is not None:
            self.rel = rel
        if uri is not None:
            self.uri = uri
        if literal is not None:
            self.literal = literal
        if symbols is not None:
            self.symbols = symbols
        if contactinfo is not None:
            self.contactinfo = contactinfo

    @property
    def name(self):
        """Gets the name of this OrganisationType.  # noqa: E501


        :return: The name of this OrganisationType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganisationType.


        :param name: The name of this OrganisationType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rel(self):
        """Gets the rel of this OrganisationType.  # noqa: E501


        :return: The rel of this OrganisationType.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this OrganisationType.


        :param rel: The rel of this OrganisationType.  # noqa: E501
        :type: str
        """

        self._rel = rel

    @property
    def uri(self):
        """Gets the uri of this OrganisationType.  # noqa: E501


        :return: The uri of this OrganisationType.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this OrganisationType.


        :param uri: The uri of this OrganisationType.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def literal(self):
        """Gets the literal of this OrganisationType.  # noqa: E501


        :return: The literal of this OrganisationType.  # noqa: E501
        :rtype: str
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this OrganisationType.


        :param literal: The literal of this OrganisationType.  # noqa: E501
        :type: str
        """

        self._literal = literal

    @property
    def symbols(self):
        """Gets the symbols of this OrganisationType.  # noqa: E501


        :return: The symbols of this OrganisationType.  # noqa: E501
        :rtype: list[object]
        """
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        """Sets the symbols of this OrganisationType.


        :param symbols: The symbols of this OrganisationType.  # noqa: E501
        :type: list[object]
        """

        self._symbols = symbols

    @property
    def contactinfo(self):
        """Gets the contactinfo of this OrganisationType.  # noqa: E501


        :return: The contactinfo of this OrganisationType.  # noqa: E501
        :rtype: list[ContactinfoType]
        """
        return self._contactinfo

    @contactinfo.setter
    def contactinfo(self, contactinfo):
        """Sets the contactinfo of this OrganisationType.


        :param contactinfo: The contactinfo of this OrganisationType.  # noqa: E501
        :type: list[ContactinfoType]
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
        if issubclass(OrganisationType, dict):
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
        if not isinstance(other, OrganisationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
