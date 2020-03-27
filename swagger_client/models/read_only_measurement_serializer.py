# coding: utf-8

"""
    Squac API

    API for accessing squac data  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReadOnlyMeasurementSerializer(object):
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
        'id': 'int',
        'metric': 'int',
        'channel': 'int',
        'value': 'float',
        'starttime': 'datetime',
        'endtime': 'datetime',
        'created_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'metric': 'metric',
        'channel': 'channel',
        'value': 'value',
        'starttime': 'starttime',
        'endtime': 'endtime',
        'created_at': 'created_at',
        'user_id': 'user_id'
    }

    def __init__(self, id=None, metric=None, channel=None, value=None, starttime=None, endtime=None, created_at=None, user_id=None):  # noqa: E501
        """ReadOnlyMeasurementSerializer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._metric = None
        self._channel = None
        self._value = None
        self._starttime = None
        self._endtime = None
        self._created_at = None
        self._user_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.metric = metric
        self.channel = channel
        self.value = value
        self.starttime = starttime
        self.endtime = endtime
        if created_at is not None:
            self.created_at = created_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The id of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyMeasurementSerializer.


        :param id: The id of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def metric(self):
        """Gets the metric of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The metric of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ReadOnlyMeasurementSerializer.


        :param metric: The metric of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: int
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def channel(self):
        """Gets the channel of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The channel of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ReadOnlyMeasurementSerializer.


        :param channel: The channel of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: int
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def value(self):
        """Gets the value of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The value of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReadOnlyMeasurementSerializer.


        :param value: The value of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def starttime(self):
        """Gets the starttime of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The starttime of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this ReadOnlyMeasurementSerializer.


        :param starttime: The starttime of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: datetime
        """
        if starttime is None:
            raise ValueError("Invalid value for `starttime`, must not be `None`")  # noqa: E501

        self._starttime = starttime

    @property
    def endtime(self):
        """Gets the endtime of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The endtime of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this ReadOnlyMeasurementSerializer.


        :param endtime: The endtime of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: datetime
        """
        if endtime is None:
            raise ValueError("Invalid value for `endtime`, must not be `None`")  # noqa: E501

        self._endtime = endtime

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyMeasurementSerializer.


        :param created_at: The created_at of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def user_id(self):
        """Gets the user_id of this ReadOnlyMeasurementSerializer.  # noqa: E501


        :return: The user_id of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ReadOnlyMeasurementSerializer.


        :param user_id: The user_id of this ReadOnlyMeasurementSerializer.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(ReadOnlyMeasurementSerializer, dict):
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
        if not isinstance(other, ReadOnlyMeasurementSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
