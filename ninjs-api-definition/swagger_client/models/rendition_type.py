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

class RenditionType(object):
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
        'uri': 'str',
        'version': 'int',
        'versionguid': 'str',
        'href': 'str',
        'code': 'str',
        'signal': 'str',
        'contenttype': 'str',
        'title': 'str',
        'generated': 'datetime',
        'height': 'float',
        'width': 'float',
        'sizeinbytes': 'float',
        'duration': 'float'
    }

    attribute_map = {
        'name': 'name',
        'uri': 'uri',
        'version': 'version',
        'versionguid': 'versionguid',
        'href': 'href',
        'code': 'code',
        'signal': 'signal',
        'contenttype': 'contenttype',
        'title': 'title',
        'generated': 'generated',
        'height': 'height',
        'width': 'width',
        'sizeinbytes': 'sizeinbytes',
        'duration': 'duration'
    }

    def __init__(self, name=None, uri=None, version=None, versionguid=None, href=None, code=None, signal=None, contenttype=None, title=None, generated=None, height=None, width=None, sizeinbytes=None, duration=None):  # noqa: E501
        """RenditionType - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._uri = None
        self._version = None
        self._versionguid = None
        self._href = None
        self._code = None
        self._signal = None
        self._contenttype = None
        self._title = None
        self._generated = None
        self._height = None
        self._width = None
        self._sizeinbytes = None
        self._duration = None
        self.discriminator = None
        self.name = name
        if uri is not None:
            self.uri = uri
        if version is not None:
            self.version = version
        if versionguid is not None:
            self.versionguid = versionguid
        if href is not None:
            self.href = href
        if code is not None:
            self.code = code
        if signal is not None:
            self.signal = signal
        if contenttype is not None:
            self.contenttype = contenttype
        if title is not None:
            self.title = title
        if generated is not None:
            self.generated = generated
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if sizeinbytes is not None:
            self.sizeinbytes = sizeinbytes
        if duration is not None:
            self.duration = duration

    @property
    def name(self):
        """Gets the name of this RenditionType.  # noqa: E501

        The name of this object in the array of renditions. For example 'thumbnail'  # noqa: E501

        :return: The name of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RenditionType.

        The name of this object in the array of renditions. For example 'thumbnail'  # noqa: E501

        :param name: The name of this RenditionType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uri(self):
        """Gets the uri of this RenditionType.  # noqa: E501

        The identifier for this rendition.  # noqa: E501

        :return: The uri of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RenditionType.

        The identifier for this rendition.  # noqa: E501

        :param uri: The uri of this RenditionType.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def version(self):
        """Gets the version of this RenditionType.  # noqa: E501

        Version of this rendition, identified by the uri.  # noqa: E501

        :return: The version of this RenditionType.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RenditionType.

        Version of this rendition, identified by the uri.  # noqa: E501

        :param version: The version of this RenditionType.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def versionguid(self):
        """Gets the versionguid of this RenditionType.  # noqa: E501

        The globally unique identifier of the target item (guid) which also includes the version identifier.  # noqa: E501

        :return: The versionguid of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._versionguid

    @versionguid.setter
    def versionguid(self, versionguid):
        """Sets the versionguid of this RenditionType.

        The globally unique identifier of the target item (guid) which also includes the version identifier.  # noqa: E501

        :param versionguid: The versionguid of this RenditionType.  # noqa: E501
        :type: str
        """

        self._versionguid = versionguid

    @property
    def href(self):
        """Gets the href of this RenditionType.  # noqa: E501

        The URL for accessing the rendition as a resource.  # noqa: E501

        :return: The href of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this RenditionType.

        The URL for accessing the rendition as a resource.  # noqa: E501

        :param href: The href of this RenditionType.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def code(self):
        """Gets the code of this RenditionType.  # noqa: E501

        Code for this rendition.  # noqa: E501

        :return: The code of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RenditionType.

        Code for this rendition.  # noqa: E501

        :param code: The code of this RenditionType.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def signal(self):
        """Gets the signal of this RenditionType.  # noqa: E501

        Signal in remote content.  # noqa: E501

        :return: The signal of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """Sets the signal of this RenditionType.

        Signal in remote content.  # noqa: E501

        :param signal: The signal of this RenditionType.  # noqa: E501
        :type: str
        """

        self._signal = signal

    @property
    def contenttype(self):
        """Gets the contenttype of this RenditionType.  # noqa: E501

        A media type which applies to this rendition.  # noqa: E501

        :return: The contenttype of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._contenttype

    @contenttype.setter
    def contenttype(self, contenttype):
        """Sets the contenttype of this RenditionType.

        A media type which applies to this rendition.  # noqa: E501

        :param contenttype: The contenttype of this RenditionType.  # noqa: E501
        :type: str
        """

        self._contenttype = contenttype

    @property
    def title(self):
        """Gets the title of this RenditionType.  # noqa: E501

        A title for the link to the rendition resource  # noqa: E501

        :return: The title of this RenditionType.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RenditionType.

        A title for the link to the rendition resource  # noqa: E501

        :param title: The title of this RenditionType.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def generated(self):
        """Gets the generated of this RenditionType.  # noqa: E501

        The date/time when the specific Content Rendition was generated by the Content Generator.  # noqa: E501

        :return: The generated of this RenditionType.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this RenditionType.

        The date/time when the specific Content Rendition was generated by the Content Generator.  # noqa: E501

        :param generated: The generated of this RenditionType.  # noqa: E501
        :type: datetime
        """

        self._generated = generated

    @property
    def height(self):
        """Gets the height of this RenditionType.  # noqa: E501


        :return: The height of this RenditionType.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this RenditionType.


        :param height: The height of this RenditionType.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this RenditionType.  # noqa: E501


        :return: The width of this RenditionType.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this RenditionType.


        :param width: The width of this RenditionType.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def sizeinbytes(self):
        """Gets the sizeinbytes of this RenditionType.  # noqa: E501

        The size of the rendition resource in bytes  # noqa: E501

        :return: The sizeinbytes of this RenditionType.  # noqa: E501
        :rtype: float
        """
        return self._sizeinbytes

    @sizeinbytes.setter
    def sizeinbytes(self, sizeinbytes):
        """Sets the sizeinbytes of this RenditionType.

        The size of the rendition resource in bytes  # noqa: E501

        :param sizeinbytes: The sizeinbytes of this RenditionType.  # noqa: E501
        :type: float
        """

        self._sizeinbytes = sizeinbytes

    @property
    def duration(self):
        """Gets the duration of this RenditionType.  # noqa: E501

        The total time duration of the content in seconds.  # noqa: E501

        :return: The duration of this RenditionType.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RenditionType.

        The total time duration of the content in seconds.  # noqa: E501

        :param duration: The duration of this RenditionType.  # noqa: E501
        :type: float
        """

        self._duration = duration

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
        if issubclass(RenditionType, dict):
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
        if not isinstance(other, RenditionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
