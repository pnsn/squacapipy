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


class Metric(object):
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
        'name': 'str',
        'code': 'str',
        'url': 'str',
        'description': 'str',
        'unit': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'default_minval': 'float',
        'default_maxval': 'float',
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'url': 'url',
        'description': 'description',
        'unit': 'unit',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'default_minval': 'default_minval',
        'default_maxval': 'default_maxval',
        'user': 'user'
    }

    def __init__(self, id=None, name=None, code=None, url=None, description=None, unit=None, created_at=None, updated_at=None, default_minval=None, default_maxval=None, user=None):  # noqa: E501
        """Metric - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._code = None
        self._url = None
        self._description = None
        self._unit = None
        self._created_at = None
        self._updated_at = None
        self._default_minval = None
        self._default_maxval = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.code = code
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        self.unit = unit
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if default_minval is not None:
            self.default_minval = default_minval
        if default_maxval is not None:
            self.default_maxval = default_maxval
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this Metric.  # noqa: E501


        :return: The id of this Metric.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metric.


        :param id: The id of this Metric.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Metric.  # noqa: E501


        :return: The name of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metric.


        :param name: The name of this Metric.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this Metric.  # noqa: E501


        :return: The code of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Metric.


        :param code: The code of this Metric.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 255:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `255`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def url(self):
        """Gets the url of this Metric.  # noqa: E501


        :return: The url of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Metric.


        :param url: The url of this Metric.  # noqa: E501
        :type: str
        """
        if url is not None and len(url) > 255:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `255`")  # noqa: E501

        self._url = url

    @property
    def description(self):
        """Gets the description of this Metric.  # noqa: E501


        :return: The description of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Metric.


        :param description: The description of this Metric.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def unit(self):
        """Gets the unit of this Metric.  # noqa: E501


        :return: The unit of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Metric.


        :param unit: The unit of this Metric.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        if unit is not None and len(unit) > 255:
            raise ValueError("Invalid value for `unit`, length must be less than or equal to `255`")  # noqa: E501
        if unit is not None and len(unit) < 1:
            raise ValueError("Invalid value for `unit`, length must be greater than or equal to `1`")  # noqa: E501

        self._unit = unit

    @property
    def created_at(self):
        """Gets the created_at of this Metric.  # noqa: E501


        :return: The created_at of this Metric.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Metric.


        :param created_at: The created_at of this Metric.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Metric.  # noqa: E501


        :return: The updated_at of this Metric.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Metric.


        :param updated_at: The updated_at of this Metric.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def default_minval(self):
        """Gets the default_minval of this Metric.  # noqa: E501


        :return: The default_minval of this Metric.  # noqa: E501
        :rtype: float
        """
        return self._default_minval

    @default_minval.setter
    def default_minval(self, default_minval):
        """Sets the default_minval of this Metric.


        :param default_minval: The default_minval of this Metric.  # noqa: E501
        :type: float
        """

        self._default_minval = default_minval

    @property
    def default_maxval(self):
        """Gets the default_maxval of this Metric.  # noqa: E501


        :return: The default_maxval of this Metric.  # noqa: E501
        :rtype: float
        """
        return self._default_maxval

    @default_maxval.setter
    def default_maxval(self, default_maxval):
        """Sets the default_maxval of this Metric.


        :param default_maxval: The default_maxval of this Metric.  # noqa: E501
        :type: float
        """

        self._default_maxval = default_maxval

    @property
    def user(self):
        """Gets the user of this Metric.  # noqa: E501


        :return: The user of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Metric.


        :param user: The user of this Metric.  # noqa: E501
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
        if issubclass(Metric, dict):
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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
