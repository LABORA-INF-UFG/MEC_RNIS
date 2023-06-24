# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.associate_id import AssociateId  # noqa: F401,E501
from swagger_server.models.nrcgi import Nrcgi  # noqa: F401,E501
from swagger_server.models.trigger_nr import TriggerNr  # noqa: F401,E501
from swagger_server import util


class FilterCriteriaNrMrs(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: str=None, associate_id: List[AssociateId]=None, nrcgi: List[Nrcgi]=None, trigger_nr: List[TriggerNr]=None):  # noqa: E501
        """FilterCriteriaNrMrs - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this FilterCriteriaNrMrs.  # noqa: E501
        :type app_instance_id: str
        :param associate_id: The associate_id of this FilterCriteriaNrMrs.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param nrcgi: The nrcgi of this FilterCriteriaNrMrs.  # noqa: E501
        :type nrcgi: List[Nrcgi]
        :param trigger_nr: The trigger_nr of this FilterCriteriaNrMrs.  # noqa: E501
        :type trigger_nr: List[TriggerNr]
        """
        self.swagger_types = {
            'app_instance_id': str,
            'associate_id': List[AssociateId],
            'nrcgi': List[Nrcgi],
            'trigger_nr': List[TriggerNr]
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'associate_id': 'associateId',
            'nrcgi': 'nrcgi',
            'trigger_nr': 'triggerNr'
        }
        self._app_instance_id = app_instance_id
        self._associate_id = associate_id
        self._nrcgi = nrcgi
        self._trigger_nr = trigger_nr

    @classmethod
    def from_dict(cls, dikt) -> 'FilterCriteriaNrMrs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FilterCriteriaNrMrs of this FilterCriteriaNrMrs.  # noqa: E501
        :rtype: FilterCriteriaNrMrs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this FilterCriteriaNrMrs.

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this FilterCriteriaNrMrs.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this FilterCriteriaNrMrs.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this FilterCriteriaNrMrs.
        :type app_instance_id: str
        """

        self._app_instance_id = app_instance_id

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this FilterCriteriaNrMrs.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this FilterCriteriaNrMrs.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this FilterCriteriaNrMrs.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this FilterCriteriaNrMrs.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def nrcgi(self) -> List[Nrcgi]:
        """Gets the nrcgi of this FilterCriteriaNrMrs.

        NR Cell Global Identier.  # noqa: E501

        :return: The nrcgi of this FilterCriteriaNrMrs.
        :rtype: List[Nrcgi]
        """
        return self._nrcgi

    @nrcgi.setter
    def nrcgi(self, nrcgi: List[Nrcgi]):
        """Sets the nrcgi of this FilterCriteriaNrMrs.

        NR Cell Global Identier.  # noqa: E501

        :param nrcgi: The nrcgi of this FilterCriteriaNrMrs.
        :type nrcgi: List[Nrcgi]
        """

        self._nrcgi = nrcgi

    @property
    def trigger_nr(self) -> List[TriggerNr]:
        """Gets the trigger_nr of this FilterCriteriaNrMrs.

        Corresponds to a specific 5G UE Measurement Report trigger.  # noqa: E501

        :return: The trigger_nr of this FilterCriteriaNrMrs.
        :rtype: List[TriggerNr]
        """
        return self._trigger_nr

    @trigger_nr.setter
    def trigger_nr(self, trigger_nr: List[TriggerNr]):
        """Sets the trigger_nr of this FilterCriteriaNrMrs.

        Corresponds to a specific 5G UE Measurement Report trigger.  # noqa: E501

        :param trigger_nr: The trigger_nr of this FilterCriteriaNrMrs.
        :type trigger_nr: List[TriggerNr]
        """

        self._trigger_nr = trigger_nr
