# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2 import util


class QosInformation(Model):

    def __init__(self, erab_gbr_dl: int, erab_gbr_ul: int, erab_mbr_dl: int, erab_mbr_ul: int):  # noqa: E501
        """QosInformation - a model defined in Swagger

        :param erab_gbr_dl: The erab_gbr_dl of this QosInformation.  # noqa: E501
        :type erab_gbr_dl: int
        :param erab_gbr_ul: The erab_gbr_ul of this QosInformation.  # noqa: E501
        :type erab_gbr_ul: int
        :param erab_mbr_dl: The erab_mbr_dl of this QosInformation.  # noqa: E501
        :type erab_mbr_dl: int
        :param erab_mbr_ul: The erab_mbr_ul of this QosInformation.  # noqa: E501
        :type erab_mbr_ul: int
        """
        self.erab_gbr_dl = erab_gbr_dl
        self.erab_gbr_ul = erab_gbr_ul
        self.erab_mbr_dl = erab_mbr_dl
        self.erab_mbr_ul = erab_mbr_ul

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "erab_gbr_dl": self.erab_gbr_dl,
            "erab_gbr_ul": self.erab_gbr_ul,
            "erab_mbr_dl": self.erab_mbr_dl,
            "erab_mbr_ul": self.erab_mbr_ul
        }

    @classmethod
    def from_dict(cls, dikt) -> 'QosInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QosInformation of this QosInformation.  # noqa: E501
        :rtype: QosInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def erab_gbr_dl(self) -> int:
        """Gets the erab_gbr_dl of this QosInformation.

        This attribute indicates the guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_gbr_dl of this QosInformation.
        :rtype: int
        """
        return self._erab_gbr_dl

    @erab_gbr_dl.setter
    def erab_gbr_dl(self, erab_gbr_dl: int):
        """Sets the erab_gbr_dl of this QosInformation.

        This attribute indicates the guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_gbr_dl: The erab_gbr_dl of this QosInformation.
        :type erab_gbr_dl: int
        """
        if erab_gbr_dl is None:
            raise ValueError("Invalid value for `erab_gbr_dl`, must not be `None`")  # noqa: E501

        self._erab_gbr_dl = erab_gbr_dl

    @property
    def erab_gbr_ul(self) -> int:
        """Gets the erab_gbr_ul of this QosInformation.

        This attribute indicates the guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_gbr_ul of this QosInformation.
        :rtype: int
        """
        return self._erab_gbr_ul

    @erab_gbr_ul.setter
    def erab_gbr_ul(self, erab_gbr_ul: int):
        """Sets the erab_gbr_ul of this QosInformation.

        This attribute indicates the guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_gbr_ul: The erab_gbr_ul of this QosInformation.
        :type erab_gbr_ul: int
        """
        if erab_gbr_ul is None:
            raise ValueError("Invalid value for `erab_gbr_ul`, must not be `None`")  # noqa: E501

        self._erab_gbr_ul = erab_gbr_ul

    @property
    def erab_mbr_dl(self) -> int:
        """Gets the erab_mbr_dl of this QosInformation.

        This attribute indicates the maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_mbr_dl of this QosInformation.
        :rtype: int
        """
        return self._erab_mbr_dl

    @erab_mbr_dl.setter
    def erab_mbr_dl(self, erab_mbr_dl: int):
        """Sets the erab_mbr_dl of this QosInformation.

        This attribute indicates the maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_mbr_dl: The erab_mbr_dl of this QosInformation.
        :type erab_mbr_dl: int
        """
        if erab_mbr_dl is None:
            raise ValueError("Invalid value for `erab_mbr_dl`, must not be `None`")  # noqa: E501

        self._erab_mbr_dl = erab_mbr_dl

    @property
    def erab_mbr_ul(self) -> int:
        """Gets the erab_mbr_ul of this QosInformation.

        This attribute indicates the maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :return: The erab_mbr_ul of this QosInformation.
        :rtype: int
        """
        return self._erab_mbr_ul

    @erab_mbr_ul.setter
    def erab_mbr_ul(self, erab_mbr_ul: int):
        """Sets the erab_mbr_ul of this QosInformation.

        This attribute indicates the maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401 [i.4] for this bearer.  # noqa: E501

        :param erab_mbr_ul: The erab_mbr_ul of this QosInformation.
        :type erab_mbr_ul: int
        """
        if erab_mbr_ul is None:
            raise ValueError("Invalid value for `erab_mbr_ul`, must not be `None`")  # noqa: E501

        self._erab_mbr_ul = erab_mbr_ul
