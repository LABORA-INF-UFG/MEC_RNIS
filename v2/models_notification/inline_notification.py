# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notification_type: str=None):  # noqa: E501
        """InlineNotification - a model defined in Swagger

        :param notification_type: The notification_type of this InlineNotification.  # noqa: E501
        :type notification_type: str
        """
        self.swagger_types = {
            'notification_type': str
        }

        self.attribute_map = {
            'notification_type': 'notificationType'
        }
        self._notification_type = notification_type

    @classmethod
    def from_dict(cls, dikt) -> 'InlineNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InlineNotification of this InlineNotification.  # noqa: E501
        :rtype: InlineNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this InlineNotification.


        :return: The notification_type of this InlineNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this InlineNotification.


        :param notification_type: The notification_type of this InlineNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type