# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_subscription import InlineSubscription  # noqa: F401,E501
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server.models.s1_bearer_subscription_criteria import S1BearerSubscriptionCriteria  # noqa: F401,E501
from swagger_server.models.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server.models.websock_notif_config import WebsockNotifConfig  # noqa: F401,E501
from swagger_server import util


class S1BearerSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subscription_type: str=None, links: Links=None, callback_reference: str=None, websock_notif_config: WebsockNotifConfig=None, request_test_notification: bool=None, s1_bearer_subscription_criteria: S1BearerSubscriptionCriteria=None, event_type: List[int]=None, expiry_deadline: TimeStamp=None):  # noqa: E501
        """S1BearerSubscription - a model defined in Swagger

        :param subscription_type: The subscription_type of this S1BearerSubscription.  # noqa: E501
        :type subscription_type: str
        :param links: The links of this S1BearerSubscription.  # noqa: E501
        :type links: Links
        :param callback_reference: The callback_reference of this S1BearerSubscription.  # noqa: E501
        :type callback_reference: str
        :param websock_notif_config: The websock_notif_config of this S1BearerSubscription.  # noqa: E501
        :type websock_notif_config: WebsockNotifConfig
        :param request_test_notification: The request_test_notification of this S1BearerSubscription.  # noqa: E501
        :type request_test_notification: bool
        :param s1_bearer_subscription_criteria: The s1_bearer_subscription_criteria of this S1BearerSubscription.  # noqa: E501
        :type s1_bearer_subscription_criteria: S1BearerSubscriptionCriteria
        :param event_type: The event_type of this S1BearerSubscription.  # noqa: E501
        :type event_type: List[int]
        :param expiry_deadline: The expiry_deadline of this S1BearerSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        """
        self.swagger_types = {
            'subscription_type': str,
            'links': Links,
            'callback_reference': str,
            'websock_notif_config': WebsockNotifConfig,
            'request_test_notification': bool,
            's1_bearer_subscription_criteria': S1BearerSubscriptionCriteria,
            'event_type': List[int],
            'expiry_deadline': TimeStamp
        }

        self.attribute_map = {
            'subscription_type': 'subscriptionType',
            'links': '_links',
            'callback_reference': 'callbackReference',
            'websock_notif_config': 'websockNotifConfig',
            'request_test_notification': 'requestTestNotification',
            's1_bearer_subscription_criteria': 'S1BearerSubscriptionCriteria',
            'event_type': 'eventType',
            'expiry_deadline': 'expiryDeadline'
        }
        self._subscription_type = subscription_type
        self._links = links
        self._callback_reference = callback_reference
        self._websock_notif_config = websock_notif_config
        self._request_test_notification = request_test_notification
        self._s1_bearer_subscription_criteria = s1_bearer_subscription_criteria
        self._event_type = event_type
        self._expiry_deadline = expiry_deadline

    @classmethod
    def from_dict(cls, dikt) -> 'S1BearerSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The S1BearerSubscription of this S1BearerSubscription.  # noqa: E501
        :rtype: S1BearerSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this S1BearerSubscription.


        :return: The subscription_type of this S1BearerSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this S1BearerSubscription.


        :param subscription_type: The subscription_type of this S1BearerSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

    @property
    def links(self) -> Links:
        """Gets the links of this S1BearerSubscription.


        :return: The links of this S1BearerSubscription.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this S1BearerSubscription.


        :param links: The links of this S1BearerSubscription.
        :type links: Links
        """

        self._links = links

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this S1BearerSubscription.

        URI exposed by the client on which to receive notifications via HTTP. See note.  # noqa: E501

        :return: The callback_reference of this S1BearerSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this S1BearerSubscription.

        URI exposed by the client on which to receive notifications via HTTP. See note.  # noqa: E501

        :param callback_reference: The callback_reference of this S1BearerSubscription.
        :type callback_reference: str
        """

        self._callback_reference = callback_reference

    @property
    def websock_notif_config(self) -> WebsockNotifConfig:
        """Gets the websock_notif_config of this S1BearerSubscription.


        :return: The websock_notif_config of this S1BearerSubscription.
        :rtype: WebsockNotifConfig
        """
        return self._websock_notif_config

    @websock_notif_config.setter
    def websock_notif_config(self, websock_notif_config: WebsockNotifConfig):
        """Sets the websock_notif_config of this S1BearerSubscription.


        :param websock_notif_config: The websock_notif_config of this S1BearerSubscription.
        :type websock_notif_config: WebsockNotifConfig
        """

        self._websock_notif_config = websock_notif_config

    @property
    def request_test_notification(self) -> bool:
        """Gets the request_test_notification of this S1BearerSubscription.

        Shall be set to TRUE by the service consumer to request a test notification via HTTP on the callbackReference URI, specified in ETSI GS MEC 009 [6], as described in clause 6.12a.  # noqa: E501

        :return: The request_test_notification of this S1BearerSubscription.
        :rtype: bool
        """
        return self._request_test_notification

    @request_test_notification.setter
    def request_test_notification(self, request_test_notification: bool):
        """Sets the request_test_notification of this S1BearerSubscription.

        Shall be set to TRUE by the service consumer to request a test notification via HTTP on the callbackReference URI, specified in ETSI GS MEC 009 [6], as described in clause 6.12a.  # noqa: E501

        :param request_test_notification: The request_test_notification of this S1BearerSubscription.
        :type request_test_notification: bool
        """

        self._request_test_notification = request_test_notification

    @property
    def s1_bearer_subscription_criteria(self) -> S1BearerSubscriptionCriteria:
        """Gets the s1_bearer_subscription_criteria of this S1BearerSubscription.


        :return: The s1_bearer_subscription_criteria of this S1BearerSubscription.
        :rtype: S1BearerSubscriptionCriteria
        """
        return self._s1_bearer_subscription_criteria

    @s1_bearer_subscription_criteria.setter
    def s1_bearer_subscription_criteria(self, s1_bearer_subscription_criteria: S1BearerSubscriptionCriteria):
        """Sets the s1_bearer_subscription_criteria of this S1BearerSubscription.


        :param s1_bearer_subscription_criteria: The s1_bearer_subscription_criteria of this S1BearerSubscription.
        :type s1_bearer_subscription_criteria: S1BearerSubscriptionCriteria
        """
        if s1_bearer_subscription_criteria is None:
            raise ValueError("Invalid value for `s1_bearer_subscription_criteria`, must not be `None`")  # noqa: E501

        self._s1_bearer_subscription_criteria = s1_bearer_subscription_criteria

    @property
    def event_type(self) -> List[int]:
        """Gets the event_type of this S1BearerSubscription.

        Description of the subscribed event. The event is included both in the request and in the response. \\nFor the eventType, the following values are currently defined: <p>0 = RESERVED. <p>1 = S1_BEARER_ESTABLISH. <p>2 = S1_BEARER_MODIFY. <p>3 = S1_BEARER_RELEASE.  # noqa: E501

        :return: The event_type of this S1BearerSubscription.
        :rtype: List[int]
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: List[int]):
        """Sets the event_type of this S1BearerSubscription.

        Description of the subscribed event. The event is included both in the request and in the response. \\nFor the eventType, the following values are currently defined: <p>0 = RESERVED. <p>1 = S1_BEARER_ESTABLISH. <p>2 = S1_BEARER_MODIFY. <p>3 = S1_BEARER_RELEASE.  # noqa: E501

        :param event_type: The event_type of this S1BearerSubscription.
        :type event_type: List[int]
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this S1BearerSubscription.


        :return: The expiry_deadline of this S1BearerSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this S1BearerSubscription.


        :param expiry_deadline: The expiry_deadline of this S1BearerSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline
