# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.filter_criteria_assoc import FilterCriteriaAssoc  # noqa: F401,E501
from v2.models.inline_subscription import InlineSubscription  # noqa: F401,E501
from v2.models.links import Links  # noqa: F401,E501
from v2.models.time_stamp import TimeStamp  # noqa: F401,E501
from v2.models.websock_notif_config import WebsockNotifConfig  # noqa: F401,E501
from v2 import util


class CaReconfSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subscription_type: str=None, links: Links=None, callback_reference: str=None, websock_notif_config: WebsockNotifConfig=None, request_test_notification: bool=None, expiry_deadline: TimeStamp=None, filter_criteria_assoc: FilterCriteriaAssoc=None):  # noqa: E501
        """CaReconfSubscription - a model defined in Swagger

        :param subscription_type: The subscription_type of this CaReconfSubscription.  # noqa: E501
        :type subscription_type: str
        :param links: The links of this CaReconfSubscription.  # noqa: E501
        :type links: Links
        :param callback_reference: The callback_reference of this CaReconfSubscription.  # noqa: E501
        :type callback_reference: str
        :param websock_notif_config: The websock_notif_config of this CaReconfSubscription.  # noqa: E501
        :type websock_notif_config: WebsockNotifConfig
        :param request_test_notification: The request_test_notification of this CaReconfSubscription.  # noqa: E501
        :type request_test_notification: bool
        :param expiry_deadline: The expiry_deadline of this CaReconfSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param filter_criteria_assoc: The filter_criteria_assoc of this CaReconfSubscription.  # noqa: E501
        :type filter_criteria_assoc: FilterCriteriaAssoc
        """
        self.swagger_types = {
            'subscription_type': str,
            'links': Links,
            'callback_reference': str,
            'websock_notif_config': WebsockNotifConfig,
            'request_test_notification': bool,
            'expiry_deadline': TimeStamp,
            'filter_criteria_assoc': FilterCriteriaAssoc
        }

        self.attribute_map = {
            'subscription_type': 'subscriptionType',
            'links': '_links',
            'callback_reference': 'callbackReference',
            'websock_notif_config': 'websockNotifConfig',
            'request_test_notification': 'requestTestNotification',
            'expiry_deadline': 'expiryDeadline',
            'filter_criteria_assoc': 'filterCriteriaAssoc'
        }
        self._subscription_type = subscription_type
        self._links = links
        self._callback_reference = callback_reference
        self._websock_notif_config = websock_notif_config
        self._request_test_notification = request_test_notification
        self._expiry_deadline = expiry_deadline
        self._filter_criteria_assoc = filter_criteria_assoc

    @classmethod
    def from_dict(cls, dikt) -> 'CaReconfSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CaReconfSubscription of this CaReconfSubscription.  # noqa: E501
        :rtype: CaReconfSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this CaReconfSubscription.


        :return: The subscription_type of this CaReconfSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this CaReconfSubscription.


        :param subscription_type: The subscription_type of this CaReconfSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

    @property
    def links(self) -> Links:
        """Gets the links of this CaReconfSubscription.


        :return: The links of this CaReconfSubscription.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this CaReconfSubscription.


        :param links: The links of this CaReconfSubscription.
        :type links: Links
        """

        self._links = links

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this CaReconfSubscription.

        URI exposed by the client on which to receive notifications via HTTP. See note.  # noqa: E501

        :return: The callback_reference of this CaReconfSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this CaReconfSubscription.

        URI exposed by the client on which to receive notifications via HTTP. See note.  # noqa: E501

        :param callback_reference: The callback_reference of this CaReconfSubscription.
        :type callback_reference: str
        """

        self._callback_reference = callback_reference

    @property
    def websock_notif_config(self) -> WebsockNotifConfig:
        """Gets the websock_notif_config of this CaReconfSubscription.


        :return: The websock_notif_config of this CaReconfSubscription.
        :rtype: WebsockNotifConfig
        """
        return self._websock_notif_config

    @websock_notif_config.setter
    def websock_notif_config(self, websock_notif_config: WebsockNotifConfig):
        """Sets the websock_notif_config of this CaReconfSubscription.


        :param websock_notif_config: The websock_notif_config of this CaReconfSubscription.
        :type websock_notif_config: WebsockNotifConfig
        """

        self._websock_notif_config = websock_notif_config

    @property
    def request_test_notification(self) -> bool:
        """Gets the request_test_notification of this CaReconfSubscription.

        Shall be set to TRUE by the service consumer to request a test notification via HTTP on the callbackReference URI, specified in ETSI GS MEC 009 [6], as described in clause 6.12a.  # noqa: E501

        :return: The request_test_notification of this CaReconfSubscription.
        :rtype: bool
        """
        return self._request_test_notification

    @request_test_notification.setter
    def request_test_notification(self, request_test_notification: bool):
        """Sets the request_test_notification of this CaReconfSubscription.

        Shall be set to TRUE by the service consumer to request a test notification via HTTP on the callbackReference URI, specified in ETSI GS MEC 009 [6], as described in clause 6.12a.  # noqa: E501

        :param request_test_notification: The request_test_notification of this CaReconfSubscription.
        :type request_test_notification: bool
        """

        self._request_test_notification = request_test_notification

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this CaReconfSubscription.


        :return: The expiry_deadline of this CaReconfSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this CaReconfSubscription.


        :param expiry_deadline: The expiry_deadline of this CaReconfSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def filter_criteria_assoc(self) -> FilterCriteriaAssoc:
        """Gets the filter_criteria_assoc of this CaReconfSubscription.


        :return: The filter_criteria_assoc of this CaReconfSubscription.
        :rtype: FilterCriteriaAssoc
        """
        return self._filter_criteria_assoc

    @filter_criteria_assoc.setter
    def filter_criteria_assoc(self, filter_criteria_assoc: FilterCriteriaAssoc):
        """Sets the filter_criteria_assoc of this CaReconfSubscription.


        :param filter_criteria_assoc: The filter_criteria_assoc of this CaReconfSubscription.
        :type filter_criteria_assoc: FilterCriteriaAssoc
        """
        if filter_criteria_assoc is None:
            raise ValueError("Invalid value for `filter_criteria_assoc`, must not be `None`")  # noqa: E501

        self._filter_criteria_assoc = filter_criteria_assoc
