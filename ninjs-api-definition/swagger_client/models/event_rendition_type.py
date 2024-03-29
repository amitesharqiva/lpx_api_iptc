# coding: utf-8

"""
    LPX API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventRenditionType(object):
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
        'items': 'list[object]',
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
        'duration': 'float',
        'averagebitrate': 'float',
        'format': 'str',
        'originalfilename': 'str',
        'fileextension': 'str',
        'digest': 'str',
        'samplerate': 'float',
        'audiobitrate': 'float',
        'aspectratio': 'str',
        'colourspace': 'str',
        'backgroundcolour': 'str',
        'orientation': 'str',
        'videocodec': 'str',
        'videoscaling': 'str',
        'framerate': 'float',
        'resolution': 'str',
        'audiocodec': 'str',
        'scene': 'str',
        'poi': 'EventRenditionTypePoi'
    }

    attribute_map = {
        'items': 'items',
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
        'duration': 'duration',
        'averagebitrate': 'averagebitrate',
        'format': 'format',
        'originalfilename': 'originalfilename',
        'fileextension': 'fileextension',
        'digest': 'digest',
        'samplerate': 'samplerate',
        'audiobitrate': 'audiobitrate',
        'aspectratio': 'aspectratio',
        'colourspace': 'colourspace',
        'backgroundcolour': 'backgroundcolour',
        'orientation': 'orientation',
        'videocodec': 'videocodec',
        'videoscaling': 'videoscaling',
        'framerate': 'framerate',
        'resolution': 'resolution',
        'audiocodec': 'audiocodec',
        'scene': 'scene',
        'poi': 'poi'
    }

    def __init__(self, items=None, name=None, uri=None, version=None, versionguid=None, href=None, code=None, signal=None, contenttype=None, title=None, generated=None, height=None, width=None, sizeinbytes=None, duration=None, averagebitrate=None, format=None, originalfilename=None, fileextension=None, digest=None, samplerate=None, audiobitrate=None, aspectratio=None, colourspace=None, backgroundcolour=None, orientation=None, videocodec=None, videoscaling=None, framerate=None, resolution=None, audiocodec=None, scene=None, poi=None):  # noqa: E501
        """EventRenditionType - a model defined in Swagger"""  # noqa: E501
        self._items = None
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
        self._averagebitrate = None
        self._format = None
        self._originalfilename = None
        self._fileextension = None
        self._digest = None
        self._samplerate = None
        self._audiobitrate = None
        self._aspectratio = None
        self._colourspace = None
        self._backgroundcolour = None
        self._orientation = None
        self._videocodec = None
        self._videoscaling = None
        self._framerate = None
        self._resolution = None
        self._audiocodec = None
        self._scene = None
        self._poi = None
        self.discriminator = None
        if items is not None:
            self.items = items
        if name is not None:
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
        if averagebitrate is not None:
            self.averagebitrate = averagebitrate
        if format is not None:
            self.format = format
        if originalfilename is not None:
            self.originalfilename = originalfilename
        if fileextension is not None:
            self.fileextension = fileextension
        if digest is not None:
            self.digest = digest
        if samplerate is not None:
            self.samplerate = samplerate
        if audiobitrate is not None:
            self.audiobitrate = audiobitrate
        if aspectratio is not None:
            self.aspectratio = aspectratio
        if colourspace is not None:
            self.colourspace = colourspace
        if backgroundcolour is not None:
            self.backgroundcolour = backgroundcolour
        if orientation is not None:
            self.orientation = orientation
        if videocodec is not None:
            self.videocodec = videocodec
        if videoscaling is not None:
            self.videoscaling = videoscaling
        if framerate is not None:
            self.framerate = framerate
        if resolution is not None:
            self.resolution = resolution
        if audiocodec is not None:
            self.audiocodec = audiocodec
        if scene is not None:
            self.scene = scene
        if poi is not None:
            self.poi = poi

    @property
    def items(self):
        """Gets the items of this EventRenditionType.  # noqa: E501


        :return: The items of this EventRenditionType.  # noqa: E501
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this EventRenditionType.


        :param items: The items of this EventRenditionType.  # noqa: E501
        :type: list[object]
        """

        self._items = items

    @property
    def name(self):
        """Gets the name of this EventRenditionType.  # noqa: E501


        :return: The name of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventRenditionType.


        :param name: The name of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uri(self):
        """Gets the uri of this EventRenditionType.  # noqa: E501


        :return: The uri of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventRenditionType.


        :param uri: The uri of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def version(self):
        """Gets the version of this EventRenditionType.  # noqa: E501


        :return: The version of this EventRenditionType.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EventRenditionType.


        :param version: The version of this EventRenditionType.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def versionguid(self):
        """Gets the versionguid of this EventRenditionType.  # noqa: E501


        :return: The versionguid of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._versionguid

    @versionguid.setter
    def versionguid(self, versionguid):
        """Sets the versionguid of this EventRenditionType.


        :param versionguid: The versionguid of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._versionguid = versionguid

    @property
    def href(self):
        """Gets the href of this EventRenditionType.  # noqa: E501


        :return: The href of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this EventRenditionType.


        :param href: The href of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def code(self):
        """Gets the code of this EventRenditionType.  # noqa: E501


        :return: The code of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EventRenditionType.


        :param code: The code of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def signal(self):
        """Gets the signal of this EventRenditionType.  # noqa: E501


        :return: The signal of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """Sets the signal of this EventRenditionType.


        :param signal: The signal of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._signal = signal

    @property
    def contenttype(self):
        """Gets the contenttype of this EventRenditionType.  # noqa: E501


        :return: The contenttype of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._contenttype

    @contenttype.setter
    def contenttype(self, contenttype):
        """Sets the contenttype of this EventRenditionType.


        :param contenttype: The contenttype of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._contenttype = contenttype

    @property
    def title(self):
        """Gets the title of this EventRenditionType.  # noqa: E501


        :return: The title of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EventRenditionType.


        :param title: The title of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def generated(self):
        """Gets the generated of this EventRenditionType.  # noqa: E501


        :return: The generated of this EventRenditionType.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this EventRenditionType.


        :param generated: The generated of this EventRenditionType.  # noqa: E501
        :type: datetime
        """

        self._generated = generated

    @property
    def height(self):
        """Gets the height of this EventRenditionType.  # noqa: E501


        :return: The height of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this EventRenditionType.


        :param height: The height of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this EventRenditionType.  # noqa: E501


        :return: The width of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this EventRenditionType.


        :param width: The width of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def sizeinbytes(self):
        """Gets the sizeinbytes of this EventRenditionType.  # noqa: E501


        :return: The sizeinbytes of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._sizeinbytes

    @sizeinbytes.setter
    def sizeinbytes(self, sizeinbytes):
        """Sets the sizeinbytes of this EventRenditionType.


        :param sizeinbytes: The sizeinbytes of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._sizeinbytes = sizeinbytes

    @property
    def duration(self):
        """Gets the duration of this EventRenditionType.  # noqa: E501


        :return: The duration of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this EventRenditionType.


        :param duration: The duration of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def averagebitrate(self):
        """Gets the averagebitrate of this EventRenditionType.  # noqa: E501


        :return: The averagebitrate of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._averagebitrate

    @averagebitrate.setter
    def averagebitrate(self, averagebitrate):
        """Sets the averagebitrate of this EventRenditionType.


        :param averagebitrate: The averagebitrate of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._averagebitrate = averagebitrate

    @property
    def format(self):
        """Gets the format of this EventRenditionType.  # noqa: E501


        :return: The format of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this EventRenditionType.


        :param format: The format of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def originalfilename(self):
        """Gets the originalfilename of this EventRenditionType.  # noqa: E501


        :return: The originalfilename of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._originalfilename

    @originalfilename.setter
    def originalfilename(self, originalfilename):
        """Sets the originalfilename of this EventRenditionType.


        :param originalfilename: The originalfilename of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._originalfilename = originalfilename

    @property
    def fileextension(self):
        """Gets the fileextension of this EventRenditionType.  # noqa: E501


        :return: The fileextension of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._fileextension

    @fileextension.setter
    def fileextension(self, fileextension):
        """Sets the fileextension of this EventRenditionType.


        :param fileextension: The fileextension of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._fileextension = fileextension

    @property
    def digest(self):
        """Gets the digest of this EventRenditionType.  # noqa: E501


        :return: The digest of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this EventRenditionType.


        :param digest: The digest of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def samplerate(self):
        """Gets the samplerate of this EventRenditionType.  # noqa: E501


        :return: The samplerate of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._samplerate

    @samplerate.setter
    def samplerate(self, samplerate):
        """Sets the samplerate of this EventRenditionType.


        :param samplerate: The samplerate of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._samplerate = samplerate

    @property
    def audiobitrate(self):
        """Gets the audiobitrate of this EventRenditionType.  # noqa: E501


        :return: The audiobitrate of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._audiobitrate

    @audiobitrate.setter
    def audiobitrate(self, audiobitrate):
        """Sets the audiobitrate of this EventRenditionType.


        :param audiobitrate: The audiobitrate of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._audiobitrate = audiobitrate

    @property
    def aspectratio(self):
        """Gets the aspectratio of this EventRenditionType.  # noqa: E501


        :return: The aspectratio of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._aspectratio

    @aspectratio.setter
    def aspectratio(self, aspectratio):
        """Sets the aspectratio of this EventRenditionType.


        :param aspectratio: The aspectratio of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._aspectratio = aspectratio

    @property
    def colourspace(self):
        """Gets the colourspace of this EventRenditionType.  # noqa: E501


        :return: The colourspace of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._colourspace

    @colourspace.setter
    def colourspace(self, colourspace):
        """Sets the colourspace of this EventRenditionType.


        :param colourspace: The colourspace of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._colourspace = colourspace

    @property
    def backgroundcolour(self):
        """Gets the backgroundcolour of this EventRenditionType.  # noqa: E501


        :return: The backgroundcolour of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._backgroundcolour

    @backgroundcolour.setter
    def backgroundcolour(self, backgroundcolour):
        """Sets the backgroundcolour of this EventRenditionType.


        :param backgroundcolour: The backgroundcolour of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._backgroundcolour = backgroundcolour

    @property
    def orientation(self):
        """Gets the orientation of this EventRenditionType.  # noqa: E501


        :return: The orientation of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this EventRenditionType.


        :param orientation: The orientation of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._orientation = orientation

    @property
    def videocodec(self):
        """Gets the videocodec of this EventRenditionType.  # noqa: E501


        :return: The videocodec of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._videocodec

    @videocodec.setter
    def videocodec(self, videocodec):
        """Sets the videocodec of this EventRenditionType.


        :param videocodec: The videocodec of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._videocodec = videocodec

    @property
    def videoscaling(self):
        """Gets the videoscaling of this EventRenditionType.  # noqa: E501


        :return: The videoscaling of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._videoscaling

    @videoscaling.setter
    def videoscaling(self, videoscaling):
        """Sets the videoscaling of this EventRenditionType.


        :param videoscaling: The videoscaling of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._videoscaling = videoscaling

    @property
    def framerate(self):
        """Gets the framerate of this EventRenditionType.  # noqa: E501


        :return: The framerate of this EventRenditionType.  # noqa: E501
        :rtype: float
        """
        return self._framerate

    @framerate.setter
    def framerate(self, framerate):
        """Sets the framerate of this EventRenditionType.


        :param framerate: The framerate of this EventRenditionType.  # noqa: E501
        :type: float
        """

        self._framerate = framerate

    @property
    def resolution(self):
        """Gets the resolution of this EventRenditionType.  # noqa: E501


        :return: The resolution of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this EventRenditionType.


        :param resolution: The resolution of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def audiocodec(self):
        """Gets the audiocodec of this EventRenditionType.  # noqa: E501


        :return: The audiocodec of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._audiocodec

    @audiocodec.setter
    def audiocodec(self, audiocodec):
        """Sets the audiocodec of this EventRenditionType.


        :param audiocodec: The audiocodec of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._audiocodec = audiocodec

    @property
    def scene(self):
        """Gets the scene of this EventRenditionType.  # noqa: E501


        :return: The scene of this EventRenditionType.  # noqa: E501
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this EventRenditionType.


        :param scene: The scene of this EventRenditionType.  # noqa: E501
        :type: str
        """

        self._scene = scene

    @property
    def poi(self):
        """Gets the poi of this EventRenditionType.  # noqa: E501


        :return: The poi of this EventRenditionType.  # noqa: E501
        :rtype: EventRenditionTypePoi
        """
        return self._poi

    @poi.setter
    def poi(self, poi):
        """Sets the poi of this EventRenditionType.


        :param poi: The poi of this EventRenditionType.  # noqa: E501
        :type: EventRenditionTypePoi
        """

        self._poi = poi

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
        if issubclass(EventRenditionType, dict):
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
        if not isinstance(other, EventRenditionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
