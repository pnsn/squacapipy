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


class ReadOnlyDashboardSerializer(object):
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
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user_id': 'str',
        'share_all': 'bool',
        'share_org': 'bool',
        'window_seconds': 'int',
        'starttime': 'datetime',
        'endtime': 'datetime',
        'organization': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user_id': 'user_id',
        'share_all': 'share_all',
        'share_org': 'share_org',
        'window_seconds': 'window_seconds',
        'starttime': 'starttime',
        'endtime': 'endtime',
        'organization': 'organization'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, user_id=None, share_all=None, share_org=None, window_seconds=None, starttime=None, endtime=None, organization=None):  # noqa: E501
        """ReadOnlyDashboardSerializer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._user_id = None
        self._share_all = None
        self._share_org = None
        self._window_seconds = None
        self._starttime = None
        self._endtime = None
        self._organization = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id
        if share_all is not None:
            self.share_all = share_all
        if share_org is not None:
            self.share_org = share_org
        if window_seconds is not None:
            self.window_seconds = window_seconds
        if starttime is not None:
            self.starttime = starttime
        if endtime is not None:
            self.endtime = endtime
        self.organization = organization

    @property
    def id(self):
        """Gets the id of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The id of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyDashboardSerializer.


        :param id: The id of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The name of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReadOnlyDashboardSerializer.


        :param name: The name of this ReadOnlyDashboardSerializer.  # noqa: E501
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
    def description(self):
        """Gets the description of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The description of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReadOnlyDashboardSerializer.


        :param description: The description of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyDashboardSerializer.


        :param created_at: The created_at of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The updated_at of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ReadOnlyDashboardSerializer.


        :param updated_at: The updated_at of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The user_id of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ReadOnlyDashboardSerializer.


        :param user_id: The user_id of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def share_all(self):
        """Gets the share_all of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The share_all of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._share_all

    @share_all.setter
    def share_all(self, share_all):
        """Sets the share_all of this ReadOnlyDashboardSerializer.


        :param share_all: The share_all of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: bool
        """

        self._share_all = share_all

    @property
    def share_org(self):
        """Gets the share_org of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The share_org of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._share_org

    @share_org.setter
    def share_org(self, share_org):
        """Sets the share_org of this ReadOnlyDashboardSerializer.


        :param share_org: The share_org of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: bool
        """

        self._share_org = share_org

    @property
    def window_seconds(self):
        """Gets the window_seconds of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The window_seconds of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: int
        """
        return self._window_seconds

    @window_seconds.setter
    def window_seconds(self, window_seconds):
        """Sets the window_seconds of this ReadOnlyDashboardSerializer.


        :param window_seconds: The window_seconds of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: int
        """
        if window_seconds is not None and window_seconds > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `window_seconds`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if window_seconds is not None and window_seconds < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `window_seconds`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._window_seconds = window_seconds

    @property
    def starttime(self):
        """Gets the starttime of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The starttime of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this ReadOnlyDashboardSerializer.


        :param starttime: The starttime of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: datetime
        """

        self._starttime = starttime

    @property
    def endtime(self):
        """Gets the endtime of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The endtime of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this ReadOnlyDashboardSerializer.


        :param endtime: The endtime of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: datetime
        """

        self._endtime = endtime

    @property
    def organization(self):
        """Gets the organization of this ReadOnlyDashboardSerializer.  # noqa: E501


        :return: The organization of this ReadOnlyDashboardSerializer.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ReadOnlyDashboardSerializer.


        :param organization: The organization of this ReadOnlyDashboardSerializer.  # noqa: E501
        :type: int
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

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
        if issubclass(ReadOnlyDashboardSerializer, dict):
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
        if not isinstance(other, ReadOnlyDashboardSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
