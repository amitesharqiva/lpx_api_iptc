# coding: utf-8

"""
    LPX API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ContactinfoTypeAddress(object):
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
        'lines': 'list[str]',
        'locality': 'str',
        'area': 'str',
        'postalcode': 'str',
        'country': 'str'
    }

    attribute_map = {
        'lines': 'lines',
        'locality': 'locality',
        'area': 'area',
        'postalcode': 'postalcode',
        'country': 'country'
    }

    def __init__(self, lines=None, locality=None, area=None, postalcode=None, country=None):  # noqa: E501
        """ContactinfoTypeAddress - a model defined in Swagger"""  # noqa: E501
        self._lines = None
        self._locality = None
        self._area = None
        self._postalcode = None
        self._country = None
        self.discriminator = None
        if lines is not None:
            self.lines = lines
        if locality is not None:
            self.locality = locality
        if area is not None:
            self.area = area
        if postalcode is not None:
            self.postalcode = postalcode
        if country is not None:
            self.country = country

    @property
    def lines(self):
        """Gets the lines of this ContactinfoTypeAddress.  # noqa: E501


        :return: The lines of this ContactinfoTypeAddress.  # noqa: E501
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this ContactinfoTypeAddress.


        :param lines: The lines of this ContactinfoTypeAddress.  # noqa: E501
        :type: list[str]
        """

        self._lines = lines

    @property
    def locality(self):
        """Gets the locality of this ContactinfoTypeAddress.  # noqa: E501


        :return: The locality of this ContactinfoTypeAddress.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this ContactinfoTypeAddress.


        :param locality: The locality of this ContactinfoTypeAddress.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def area(self):
        """Gets the area of this ContactinfoTypeAddress.  # noqa: E501


        :return: The area of this ContactinfoTypeAddress.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ContactinfoTypeAddress.


        :param area: The area of this ContactinfoTypeAddress.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def postalcode(self):
        """Gets the postalcode of this ContactinfoTypeAddress.  # noqa: E501


        :return: The postalcode of this ContactinfoTypeAddress.  # noqa: E501
        :rtype: str
        """
        return self._postalcode

    @postalcode.setter
    def postalcode(self, postalcode):
        """Sets the postalcode of this ContactinfoTypeAddress.


        :param postalcode: The postalcode of this ContactinfoTypeAddress.  # noqa: E501
        :type: str
        """

        self._postalcode = postalcode

    @property
    def country(self):
        """Gets the country of this ContactinfoTypeAddress.  # noqa: E501


        :return: The country of this ContactinfoTypeAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ContactinfoTypeAddress.


        :param country: The country of this ContactinfoTypeAddress.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(ContactinfoTypeAddress, dict):
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
        if not isinstance(other, ContactinfoTypeAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
