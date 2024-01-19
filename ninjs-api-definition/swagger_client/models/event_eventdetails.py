# coding: utf-8

"""
    Event API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventEventdetails(object):
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
        'dates': 'EventEventdetailsDates',
        'embargoed': 'datetime',
        'organiser': 'EventEventdetailsOrganiser',
        'usageterms': 'str',
        'pubstatus': 'list[str]',
        'copyrightholder': 'str',
        'copyrightnotice': 'str',
        'location': 'str',
        'infosource': 'list[EventEventdetailsInfosource]',
        'ednote': 'EventEventdetailsEdnote'
    }

    attribute_map = {
        'dates': 'dates',
        'embargoed': 'embargoed',
        'organiser': 'organiser',
        'usageterms': 'usageterms',
        'pubstatus': 'pubstatus',
        'copyrightholder': 'copyrightholder',
        'copyrightnotice': 'copyrightnotice',
        'location': 'location',
        'infosource': 'infosource',
        'ednote': 'ednote'
    }

    def __init__(self, dates=None, embargoed=None, organiser=None, usageterms=None, pubstatus=None, copyrightholder=None, copyrightnotice=None, location=None, infosource=None, ednote=None):  # noqa: E501
        """EventEventdetails - a model defined in Swagger"""  # noqa: E501
        self._dates = None
        self._embargoed = None
        self._organiser = None
        self._usageterms = None
        self._pubstatus = None
        self._copyrightholder = None
        self._copyrightnotice = None
        self._location = None
        self._infosource = None
        self._ednote = None
        self.discriminator = None
        if dates is not None:
            self.dates = dates
        if embargoed is not None:
            self.embargoed = embargoed
        if organiser is not None:
            self.organiser = organiser
        if usageterms is not None:
            self.usageterms = usageterms
        if pubstatus is not None:
            self.pubstatus = pubstatus
        if copyrightholder is not None:
            self.copyrightholder = copyrightholder
        if copyrightnotice is not None:
            self.copyrightnotice = copyrightnotice
        if location is not None:
            self.location = location
        if infosource is not None:
            self.infosource = infosource
        if ednote is not None:
            self.ednote = ednote

    @property
    def dates(self):
        """Gets the dates of this EventEventdetails.  # noqa: E501


        :return: The dates of this EventEventdetails.  # noqa: E501
        :rtype: EventEventdetailsDates
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this EventEventdetails.


        :param dates: The dates of this EventEventdetails.  # noqa: E501
        :type: EventEventdetailsDates
        """

        self._dates = dates

    @property
    def embargoed(self):
        """Gets the embargoed of this EventEventdetails.  # noqa: E501


        :return: The embargoed of this EventEventdetails.  # noqa: E501
        :rtype: datetime
        """
        return self._embargoed

    @embargoed.setter
    def embargoed(self, embargoed):
        """Sets the embargoed of this EventEventdetails.


        :param embargoed: The embargoed of this EventEventdetails.  # noqa: E501
        :type: datetime
        """

        self._embargoed = embargoed

    @property
    def organiser(self):
        """Gets the organiser of this EventEventdetails.  # noqa: E501


        :return: The organiser of this EventEventdetails.  # noqa: E501
        :rtype: EventEventdetailsOrganiser
        """
        return self._organiser

    @organiser.setter
    def organiser(self, organiser):
        """Sets the organiser of this EventEventdetails.


        :param organiser: The organiser of this EventEventdetails.  # noqa: E501
        :type: EventEventdetailsOrganiser
        """

        self._organiser = organiser

    @property
    def usageterms(self):
        """Gets the usageterms of this EventEventdetails.  # noqa: E501


        :return: The usageterms of this EventEventdetails.  # noqa: E501
        :rtype: str
        """
        return self._usageterms

    @usageterms.setter
    def usageterms(self, usageterms):
        """Sets the usageterms of this EventEventdetails.


        :param usageterms: The usageterms of this EventEventdetails.  # noqa: E501
        :type: str
        """

        self._usageterms = usageterms

    @property
    def pubstatus(self):
        """Gets the pubstatus of this EventEventdetails.  # noqa: E501


        :return: The pubstatus of this EventEventdetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._pubstatus

    @pubstatus.setter
    def pubstatus(self, pubstatus):
        """Sets the pubstatus of this EventEventdetails.


        :param pubstatus: The pubstatus of this EventEventdetails.  # noqa: E501
        :type: list[str]
        """

        self._pubstatus = pubstatus

    @property
    def copyrightholder(self):
        """Gets the copyrightholder of this EventEventdetails.  # noqa: E501


        :return: The copyrightholder of this EventEventdetails.  # noqa: E501
        :rtype: str
        """
        return self._copyrightholder

    @copyrightholder.setter
    def copyrightholder(self, copyrightholder):
        """Sets the copyrightholder of this EventEventdetails.


        :param copyrightholder: The copyrightholder of this EventEventdetails.  # noqa: E501
        :type: str
        """

        self._copyrightholder = copyrightholder

    @property
    def copyrightnotice(self):
        """Gets the copyrightnotice of this EventEventdetails.  # noqa: E501


        :return: The copyrightnotice of this EventEventdetails.  # noqa: E501
        :rtype: str
        """
        return self._copyrightnotice

    @copyrightnotice.setter
    def copyrightnotice(self, copyrightnotice):
        """Sets the copyrightnotice of this EventEventdetails.


        :param copyrightnotice: The copyrightnotice of this EventEventdetails.  # noqa: E501
        :type: str
        """

        self._copyrightnotice = copyrightnotice

    @property
    def location(self):
        """Gets the location of this EventEventdetails.  # noqa: E501


        :return: The location of this EventEventdetails.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EventEventdetails.


        :param location: The location of this EventEventdetails.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def infosource(self):
        """Gets the infosource of this EventEventdetails.  # noqa: E501


        :return: The infosource of this EventEventdetails.  # noqa: E501
        :rtype: list[EventEventdetailsInfosource]
        """
        return self._infosource

    @infosource.setter
    def infosource(self, infosource):
        """Sets the infosource of this EventEventdetails.


        :param infosource: The infosource of this EventEventdetails.  # noqa: E501
        :type: list[EventEventdetailsInfosource]
        """

        self._infosource = infosource

    @property
    def ednote(self):
        """Gets the ednote of this EventEventdetails.  # noqa: E501


        :return: The ednote of this EventEventdetails.  # noqa: E501
        :rtype: EventEventdetailsEdnote
        """
        return self._ednote

    @ednote.setter
    def ednote(self, ednote):
        """Sets the ednote of this EventEventdetails.


        :param ednote: The ednote of this EventEventdetails.  # noqa: E501
        :type: EventEventdetailsEdnote
        """

        self._ednote = ednote

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
        if issubclass(EventEventdetails, dict):
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
        if not isinstance(other, EventEventdetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
