# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.associate_id import AssociateId  # noqa: F401,E501
from v2.models_notification.ca_reconf_notification_links import CaReconfNotificationLinks  # noqa: F401,E501
from v2.models.ecgi import Ecgi  # noqa: F401,E501
from v2.models.erab_qos_parameters2 import ErabQosParameters2  # noqa: F401,E501
from v2.models_notification.inline_notification import InlineNotification  # noqa: F401,E501
from v2.models.time_stamp import TimeStamp  # noqa: F401,E501
from v2 import util


class RabModNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notification_type: str=None, associate_id: List[AssociateId]=None, ecgi: Ecgi=None, erab_id: int=None, erab_qos_parameters: ErabQosParameters2=None, time_stamp: TimeStamp=None, links: CaReconfNotificationLinks=None):  # noqa: E501
        """RabModNotification - a model defined in Swagger

        :param notification_type: The notification_type of this RabModNotification.  # noqa: E501
        :type notification_type: str
        :param associate_id: The associate_id of this RabModNotification.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this RabModNotification.  # noqa: E501
        :type ecgi: Ecgi
        :param erab_id: The erab_id of this RabModNotification.  # noqa: E501
        :type erab_id: int
        :param erab_qos_parameters: The erab_qos_parameters of this RabModNotification.  # noqa: E501
        :type erab_qos_parameters: ErabQosParameters2
        :param time_stamp: The time_stamp of this RabModNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        :param links: The links of this RabModNotification.  # noqa: E501
        :type links: CaReconfNotificationLinks
        """
        self.swagger_types = {
            'notification_type': str,
            'associate_id': List[AssociateId],
            'ecgi': Ecgi,
            'erab_id': int,
            'erab_qos_parameters': ErabQosParameters2,
            'time_stamp': TimeStamp,
            'links': CaReconfNotificationLinks
        }

        self.attribute_map = {
            'notification_type': 'notificationType',
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'erab_id': 'erabId',
            'erab_qos_parameters': 'erabQosParameters',
            'time_stamp': 'timeStamp',
            'links': '_links'
        }
        self._notification_type = notification_type
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._erab_id = erab_id
        self._erab_qos_parameters = erab_qos_parameters
        self._time_stamp = time_stamp
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'RabModNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabModNotification of this RabModNotification.  # noqa: E501
        :rtype: RabModNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this RabModNotification.


        :return: The notification_type of this RabModNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this RabModNotification.


        :param notification_type: The notification_type of this RabModNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this RabModNotification.

        0 to N identifiers to bind the event for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this RabModNotification.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this RabModNotification.

        0 to N identifiers to bind the event for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this RabModNotification.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this RabModNotification.


        :return: The ecgi of this RabModNotification.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this RabModNotification.


        :param ecgi: The ecgi of this RabModNotification.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def erab_id(self) -> int:
        """Gets the erab_id of this RabModNotification.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this RabModNotification.
        :rtype: int
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id: int):
        """Sets the erab_id of this RabModNotification.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this RabModNotification.
        :type erab_id: int
        """
        if erab_id is None:
            raise ValueError("Invalid value for `erab_id`, must not be `None`")  # noqa: E501

        self._erab_id = erab_id

    @property
    def erab_qos_parameters(self) -> ErabQosParameters2:
        """Gets the erab_qos_parameters of this RabModNotification.


        :return: The erab_qos_parameters of this RabModNotification.
        :rtype: ErabQosParameters2
        """
        return self._erab_qos_parameters

    @erab_qos_parameters.setter
    def erab_qos_parameters(self, erab_qos_parameters: ErabQosParameters2):
        """Sets the erab_qos_parameters of this RabModNotification.


        :param erab_qos_parameters: The erab_qos_parameters of this RabModNotification.
        :type erab_qos_parameters: ErabQosParameters2
        """

        self._erab_qos_parameters = erab_qos_parameters

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this RabModNotification.


        :return: The time_stamp of this RabModNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this RabModNotification.


        :param time_stamp: The time_stamp of this RabModNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp

    @property
    def links(self) -> CaReconfNotificationLinks:
        """Gets the links of this RabModNotification.


        :return: The links of this RabModNotification.
        :rtype: CaReconfNotificationLinks
        """
        return self._links

    @links.setter
    def links(self, links: CaReconfNotificationLinks):
        """Sets the links of this RabModNotification.


        :param links: The links of this RabModNotification.
        :type links: CaReconfNotificationLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links