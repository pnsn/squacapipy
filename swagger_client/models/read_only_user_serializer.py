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


class ReadOnlyUserSerializer(object):
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
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'is_staff': 'bool',
        'organization': 'str',
        'groups': 'list[Group]',
        'id': 'int'
    }

    attribute_map = {
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'is_staff': 'is_staff',
        'organization': 'organization',
        'groups': 'groups',
        'id': 'id'
    }

    def __init__(self, email=None, firstname=None, lastname=None, is_staff=None, organization=None, groups=None, id=None):  # noqa: E501
        """ReadOnlyUserSerializer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._firstname = None
        self._lastname = None
        self._is_staff = None
        self._organization = None
        self._groups = None
        self._id = None
        self.discriminator = None

        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if is_staff is not None:
            self.is_staff = is_staff
        self.organization = organization
        if groups is not None:
            self.groups = groups
        if id is not None:
            self.id = id

    @property
    def email(self):
        """Gets the email of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The email of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ReadOnlyUserSerializer.


        :param email: The email of this ReadOnlyUserSerializer.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The firstname of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this ReadOnlyUserSerializer.


        :param firstname: The firstname of this ReadOnlyUserSerializer.  # noqa: E501
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501
        if firstname is not None and len(firstname) > 255:
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `255`")  # noqa: E501
        if firstname is not None and len(firstname) < 1:
            raise ValueError("Invalid value for `firstname`, length must be greater than or equal to `1`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The lastname of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this ReadOnlyUserSerializer.


        :param lastname: The lastname of this ReadOnlyUserSerializer.  # noqa: E501
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501
        if lastname is not None and len(lastname) > 255:
            raise ValueError("Invalid value for `lastname`, length must be less than or equal to `255`")  # noqa: E501
        if lastname is not None and len(lastname) < 1:
            raise ValueError("Invalid value for `lastname`, length must be greater than or equal to `1`")  # noqa: E501

        self._lastname = lastname

    @property
    def is_staff(self):
        """Gets the is_staff of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The is_staff of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._is_staff

    @is_staff.setter
    def is_staff(self, is_staff):
        """Sets the is_staff of this ReadOnlyUserSerializer.


        :param is_staff: The is_staff of this ReadOnlyUserSerializer.  # noqa: E501
        :type: bool
        """

        self._is_staff = is_staff

    @property
    def organization(self):
        """Gets the organization of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The organization of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ReadOnlyUserSerializer.


        :param organization: The organization of this ReadOnlyUserSerializer.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501
        if organization is not None and len(organization) > 255:
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `255`")  # noqa: E501
        if organization is not None and len(organization) < 1:
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `1`")  # noqa: E501

        self._organization = organization

    @property
    def groups(self):
        """Gets the groups of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The groups of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ReadOnlyUserSerializer.


        :param groups: The groups of this ReadOnlyUserSerializer.  # noqa: E501
        :type: list[Group]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this ReadOnlyUserSerializer.  # noqa: E501


        :return: The id of this ReadOnlyUserSerializer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyUserSerializer.


        :param id: The id of this ReadOnlyUserSerializer.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(ReadOnlyUserSerializer, dict):
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
        if not isinstance(other, ReadOnlyUserSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
