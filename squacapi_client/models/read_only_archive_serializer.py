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


class ReadOnlyArchiveSerializer(object):
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
        'id': 'str',
        'channel': 'int',
        'metric': 'int',
        'archive_type': 'str',
        'min': 'float',
        'max': 'float',
        'mean': 'float',
        'median': 'float',
        'stdev': 'float',
        'num_samps': 'int',
        'starttime': 'datetime',
        'endtime': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'channel': 'channel',
        'metric': 'metric',
        'archive_type': 'archive_type',
        'min': 'min',
        'max': 'max',
        'mean': 'mean',
        'median': 'median',
        'stdev': 'stdev',
        'num_samps': 'num_samps',
        'starttime': 'starttime',
        'endtime': 'endtime',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, channel=None, metric=None, archive_type=None, min=None, max=None, mean=None, median=None, stdev=None, num_samps=None, starttime=None, endtime=None, created_at=None, updated_at=None):  # noqa: E501
        """ReadOnlyArchiveSerializer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._channel = None
        self._metric = None
        self._archive_type = None
        self._min = None
        self._max = None
        self._mean = None
        self._median = None
        self._stdev = None
        self._num_samps = None
        self._starttime = None
        self._endtime = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.channel = channel
        self.metric = metric
        self.archive_type = archive_type
        self.min = min
        self.max = max
        self.mean = mean
        self.median = median
        self.stdev = stdev
        self.num_samps = num_samps
        self.starttime = starttime
        self.endtime = endtime
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The id of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyArchiveSerializer.


        :param id: The id of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def channel(self):
        """Gets the channel of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The channel of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ReadOnlyArchiveSerializer.


        :param channel: The channel of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: int
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def metric(self):
        """Gets the metric of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The metric of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ReadOnlyArchiveSerializer.


        :param metric: The metric of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: int
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def archive_type(self):
        """Gets the archive_type of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The archive_type of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: str
        """
        return self._archive_type

    @archive_type.setter
    def archive_type(self, archive_type):
        """Sets the archive_type of this ReadOnlyArchiveSerializer.


        :param archive_type: The archive_type of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: str
        """
        if archive_type is None:
            raise ValueError("Invalid value for `archive_type`, must not be `None`")  # noqa: E501
        allowed_values = ["day", "week", "month", "year"]  # noqa: E501
        if archive_type not in allowed_values:
            raise ValueError(
                "Invalid value for `archive_type` ({0}), must be one of {1}"  # noqa: E501
                .format(archive_type, allowed_values)
            )

        self._archive_type = archive_type

    @property
    def min(self):
        """Gets the min of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The min of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ReadOnlyArchiveSerializer.


        :param min: The min of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The max of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ReadOnlyArchiveSerializer.


        :param max: The max of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def mean(self):
        """Gets the mean of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The mean of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ReadOnlyArchiveSerializer.


        :param mean: The mean of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: float
        """
        if mean is None:
            raise ValueError("Invalid value for `mean`, must not be `None`")  # noqa: E501

        self._mean = mean

    @property
    def median(self):
        """Gets the median of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The median of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this ReadOnlyArchiveSerializer.


        :param median: The median of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: float
        """
        if median is None:
            raise ValueError("Invalid value for `median`, must not be `None`")  # noqa: E501

        self._median = median

    @property
    def stdev(self):
        """Gets the stdev of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The stdev of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: float
        """
        return self._stdev

    @stdev.setter
    def stdev(self, stdev):
        """Sets the stdev of this ReadOnlyArchiveSerializer.


        :param stdev: The stdev of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: float
        """
        if stdev is None:
            raise ValueError("Invalid value for `stdev`, must not be `None`")  # noqa: E501

        self._stdev = stdev

    @property
    def num_samps(self):
        """Gets the num_samps of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The num_samps of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: int
        """
        return self._num_samps

    @num_samps.setter
    def num_samps(self, num_samps):
        """Sets the num_samps of this ReadOnlyArchiveSerializer.


        :param num_samps: The num_samps of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: int
        """
        if num_samps is None:
            raise ValueError("Invalid value for `num_samps`, must not be `None`")  # noqa: E501
        if num_samps is not None and num_samps > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `num_samps`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if num_samps is not None and num_samps < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `num_samps`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._num_samps = num_samps

    @property
    def starttime(self):
        """Gets the starttime of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The starttime of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this ReadOnlyArchiveSerializer.


        :param starttime: The starttime of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: datetime
        """
        if starttime is None:
            raise ValueError("Invalid value for `starttime`, must not be `None`")  # noqa: E501

        self._starttime = starttime

    @property
    def endtime(self):
        """Gets the endtime of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The endtime of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this ReadOnlyArchiveSerializer.


        :param endtime: The endtime of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: datetime
        """
        if endtime is None:
            raise ValueError("Invalid value for `endtime`, must not be `None`")  # noqa: E501

        self._endtime = endtime

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyArchiveSerializer.


        :param created_at: The created_at of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ReadOnlyArchiveSerializer.  # noqa: E501


        :return: The updated_at of this ReadOnlyArchiveSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ReadOnlyArchiveSerializer.


        :param updated_at: The updated_at of this ReadOnlyArchiveSerializer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(ReadOnlyArchiveSerializer, dict):
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
        if not isinstance(other, ReadOnlyArchiveSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other