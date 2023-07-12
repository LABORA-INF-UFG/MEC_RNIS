# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ecgi import Ecgi  # noqa: F401,E501
from swagger_server import util


class EutraNeighCellMeasInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ecgi: Ecgi=None, rsrp: int=None, rsrq: int=None, sinr: int=None):  # noqa: E501
        """EutraNeighCellMeasInfo - a model defined in Swagger

        :param ecgi: The ecgi of this EutraNeighCellMeasInfo.  # noqa: E501
        :type ecgi: Ecgi
        :param rsrp: The rsrp of this EutraNeighCellMeasInfo.  # noqa: E501
        :type rsrp: int
        :param rsrq: The rsrq of this EutraNeighCellMeasInfo.  # noqa: E501
        :type rsrq: int
        :param sinr: The sinr of this EutraNeighCellMeasInfo.  # noqa: E501
        :type sinr: int
        """
        self.swagger_types = {
            'ecgi': Ecgi,
            'rsrp': int,
            'rsrq': int,
            'sinr': int
        }

        self.attribute_map = {
            'ecgi': 'ecgi',
            'rsrp': 'rsrp',
            'rsrq': 'rsrq',
            'sinr': 'sinr'
        }
        self._ecgi = ecgi
        self._rsrp = rsrp
        self._rsrq = rsrq
        self._sinr = sinr

    @classmethod
    def from_dict(cls, dikt) -> 'EutraNeighCellMeasInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EutraNeighCellMeasInfo of this EutraNeighCellMeasInfo.  # noqa: E501
        :rtype: EutraNeighCellMeasInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this EutraNeighCellMeasInfo.


        :return: The ecgi of this EutraNeighCellMeasInfo.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this EutraNeighCellMeasInfo.


        :param ecgi: The ecgi of this EutraNeighCellMeasInfo.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def rsrp(self) -> int:
        """Gets the rsrp of this EutraNeighCellMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The rsrp of this EutraNeighCellMeasInfo.
        :rtype: int
        """
        return self._rsrp

    @rsrp.setter
    def rsrp(self, rsrp: int):
        """Sets the rsrp of this EutraNeighCellMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param rsrp: The rsrp of this EutraNeighCellMeasInfo.
        :type rsrp: int
        """

        self._rsrp = rsrp

    @property
    def rsrq(self) -> int:
        """Gets the rsrq of this EutraNeighCellMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The rsrq of this EutraNeighCellMeasInfo.
        :rtype: int
        """
        return self._rsrq

    @rsrq.setter
    def rsrq(self, rsrq: int):
        """Sets the rsrq of this EutraNeighCellMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param rsrq: The rsrq of this EutraNeighCellMeasInfo.
        :type rsrq: int
        """

        self._rsrq = rsrq

    @property
    def sinr(self) -> int:
        """Gets the sinr of this EutraNeighCellMeasInfo.

        Reference Signal plus Interference Noise Ratio as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The sinr of this EutraNeighCellMeasInfo.
        :rtype: int
        """
        return self._sinr

    @sinr.setter
    def sinr(self, sinr: int):
        """Sets the sinr of this EutraNeighCellMeasInfo.

        Reference Signal plus Interference Noise Ratio as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param sinr: The sinr of this EutraNeighCellMeasInfo.
        :type sinr: int
        """

        self._sinr = sinr
