# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.filter_criteria_assoc_tri import FilterCriteriaAssocTri  # noqa: F401,E501
from swagger_server.models.inline_subscription import InlineSubscription  # noqa: F401,E501
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server.models.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server.models.websock_notif_config import WebsockNotifConfig  # noqa: F401,E501
from swagger_server import util


class MeasRepUeSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subscription_type: str=None, links: Links=None, callback_reference: str=None, websock_notif_config: WebsockNotifConfig=None, request_test_notification: bool=None, expiry_deadline: TimeStamp=None, filter_criteria_assoc_tri: FilterCriteriaAssocTri=None):  # noqa: E501
        """MeasRepUeSubscription - a model defined in Swagger

        :param subscription_type: The subscription_type of this MeasRepUeSubscription.  # noqa: E501
        :type subscription_type: str
        :param links: The links of this MeasRepUeSubscription.  # noqa: E501
        :type links: Links
        :param callback_reference: The callback_reference of this MeasRepUeSubscription.  # noqa: E501
        :type callback_reference: str
        :param websock_notif_config: The websock_notif_config of this MeasRepUeSubscription.  # noqa: E501
        :type websock_notif_config: WebsockNotifConfig
        :param request_test_notification: The request_test_notification of this MeasRepUeSubscription.  # noqa: E501
        :type request_test_notification: bool
        :param expiry_deadline: The expiry_deadline of this MeasRepUeSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param filter_criteria_assoc_tri: The filter_criteria_assoc_tri of this MeasRepUeSubscription.  # noqa: E501
        :type filter_criteria_assoc_tri: FilterCriteriaAssocTri
        """
        self.swagger_types = {
            'subscription_type': str,
            'links': Links,
            'callback_reference': str,
            'websock_notif_config': WebsockNotifConfig,
            'request_test_notification': bool,
            'expiry_deadline': TimeStamp,
            'filter_criteria_assoc_tri': FilterCriteriaAssocTri
        }

        self.attribute_map = {
            'subscription_type': 'subscriptionType',
            'links': '_links',
            'callback_reference': 'callbackReference',
            'websock_notif_config': 'websockNotifConfig',
            'request_test_notification': 'requestTestNotification',
            'expiry_deadline': 'expiryDeadline',
            'filter_criteria_assoc_tri': 'filterCriteriaAssocTri'
        }
        self._subscription_type = subscription_type
        self._links = links
        self._callback_reference = callback_reference
        self._websock_notif_config = websock_notif_config
        self._request_test_notification = request_test_notification
        self._expiry_deadline = expiry_deadline
        self._filter_criteria_assoc_tri = filter_criteria_assoc_tri

    @classmethod
    def from_dict(cls, dikt) -> 'MeasRepUeSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasRepUeSubscription of this MeasRepUeSubscription.  # noqa: E501
        :rtype: MeasRepUeSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this MeasRepUeSubscription.


        :return: The subscription_type of this MeasRepUeSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this MeasRepUeSubscription.


        :param subscription_type: The subscription_type of this MeasRepUeSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

    @property
    def links(self) -> Links:
        """Gets the links of this MeasRepUeSubscription.


        :return: The links of this MeasRepUeSubscription.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this MeasRepUeSubscription.


        :param links: The links of this MeasRepUeSubscription.
        :type links: Links
        """

        self._links = links

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this MeasRepUeSubscription.

        URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response. If not present, the service consumer is requesting the use of a Websocket for notifications. See note.  # noqa: E501

        :return: The callback_reference of this MeasRepUeSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this MeasRepUeSubscription.

        URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response. If not present, the service consumer is requesting the use of a Websocket for notifications. See note.  # noqa: E501

        :param callback_reference: The callback_reference of this MeasRepUeSubscription.
        :type callback_reference: str
        """

        self._callback_reference = callback_reference

    @property
    def websock_notif_config(self) -> WebsockNotifConfig:
        """Gets the websock_notif_config of this MeasRepUeSubscription.


        :return: The websock_notif_config of this MeasRepUeSubscription.
        :rtype: WebsockNotifConfig
        """
        return self._websock_notif_config

    @websock_notif_config.setter
    def websock_notif_config(self, websock_notif_config: WebsockNotifConfig):
        """Sets the websock_notif_config of this MeasRepUeSubscription.


        :param websock_notif_config: The websock_notif_config of this MeasRepUeSubscription.
        :type websock_notif_config: WebsockNotifConfig
        """

        self._websock_notif_config = websock_notif_config

    @property
    def request_test_notification(self) -> bool:
        """Gets the request_test_notification of this MeasRepUeSubscription.

        Set to TRUE by the service consumer to request a test notification on the callbackReference URI to determine if it is reachable by RNIS for notifications.  # noqa: E501

        :return: The request_test_notification of this MeasRepUeSubscription.
        :rtype: bool
        """
        return self._request_test_notification

    @request_test_notification.setter
    def request_test_notification(self, request_test_notification: bool):
        """Sets the request_test_notification of this MeasRepUeSubscription.

        Set to TRUE by the service consumer to request a test notification on the callbackReference URI to determine if it is reachable by RNIS for notifications.  # noqa: E501

        :param request_test_notification: The request_test_notification of this MeasRepUeSubscription.
        :type request_test_notification: bool
        """

        self._request_test_notification = request_test_notification

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this MeasRepUeSubscription.


        :return: The expiry_deadline of this MeasRepUeSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this MeasRepUeSubscription.


        :param expiry_deadline: The expiry_deadline of this MeasRepUeSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def filter_criteria_assoc_tri(self) -> FilterCriteriaAssocTri:
        """Gets the filter_criteria_assoc_tri of this MeasRepUeSubscription.


        :return: The filter_criteria_assoc_tri of this MeasRepUeSubscription.
        :rtype: FilterCriteriaAssocTri
        """
        return self._filter_criteria_assoc_tri

    @filter_criteria_assoc_tri.setter
    def filter_criteria_assoc_tri(self, filter_criteria_assoc_tri: FilterCriteriaAssocTri):
        """Sets the filter_criteria_assoc_tri of this MeasRepUeSubscription.


        :param filter_criteria_assoc_tri: The filter_criteria_assoc_tri of this MeasRepUeSubscription.
        :type filter_criteria_assoc_tri: FilterCriteriaAssocTri
        """
        if filter_criteria_assoc_tri is None:
            raise ValueError("Invalid value for `filter_criteria_assoc_tri`, must not be `None`")  # noqa: E501

        self._filter_criteria_assoc_tri = filter_criteria_assoc_tri
