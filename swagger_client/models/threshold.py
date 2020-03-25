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


class Threshold(object):
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
        'url': 'str',
        'metric': 'int',
        'widget': 'int',
        'minval': 'float',
        'maxval': 'float',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'metric': 'metric',
        'widget': 'widget',
        'minval': 'minval',
        'maxval': 'maxval',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, id=None, url=None, metric=None, widget=None, minval=None, maxval=None, created_at=None, updated_at=None, user=None):  # noqa: E501
        """Threshold - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._metric = None
        self._widget = None
        self._minval = None
        self._maxval = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.metric = metric
        self.widget = widget
        if minval is not None:
            self.minval = minval
        if maxval is not None:
            self.maxval = maxval
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this Threshold.  # noqa: E501


        :return: The id of this Threshold.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Threshold.


        :param id: The id of this Threshold.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Threshold.  # noqa: E501


        :return: The url of this Threshold.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Threshold.


        :param url: The url of this Threshold.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def metric(self):
        """Gets the metric of this Threshold.  # noqa: E501


        :return: The metric of this Threshold.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Threshold.


        :param metric: The metric of this Threshold.  # noqa: E501
        :type: int
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def widget(self):
        """Gets the widget of this Threshold.  # noqa: E501


        :return: The widget of this Threshold.  # noqa: E501
        :rtype: int
        """
        return self._widget

    @widget.setter
    def widget(self, widget):
        """Sets the widget of this Threshold.


        :param widget: The widget of this Threshold.  # noqa: E501
        :type: int
        """
        if widget is None:
            raise ValueError("Invalid value for `widget`, must not be `None`")  # noqa: E501

        self._widget = widget

    @property
    def minval(self):
        """Gets the minval of this Threshold.  # noqa: E501


        :return: The minval of this Threshold.  # noqa: E501
        :rtype: float
        """
        return self._minval

    @minval.setter
    def minval(self, minval):
        """Sets the minval of this Threshold.


        :param minval: The minval of this Threshold.  # noqa: E501
        :type: float
        """

        self._minval = minval

    @property
    def maxval(self):
        """Gets the maxval of this Threshold.  # noqa: E501


        :return: The maxval of this Threshold.  # noqa: E501
        :rtype: float
        """
        return self._maxval

    @maxval.setter
    def maxval(self, maxval):
        """Sets the maxval of this Threshold.


        :param maxval: The maxval of this Threshold.  # noqa: E501
        :type: float
        """

        self._maxval = maxval

    @property
    def created_at(self):
        """Gets the created_at of this Threshold.  # noqa: E501


        :return: The created_at of this Threshold.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Threshold.


        :param created_at: The created_at of this Threshold.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Threshold.  # noqa: E501


        :return: The updated_at of this Threshold.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Threshold.


        :param updated_at: The updated_at of this Threshold.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Threshold.  # noqa: E501


        :return: The user of this Threshold.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Threshold.


        :param user: The user of this Threshold.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(Threshold, dict):
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
        if not isinstance(other, Threshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
