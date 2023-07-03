# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.nr_bn_cell_info import NrBNCellInfo  # noqa: F401,E501
from swagger_server import util


class NrBNCs(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nr_bn_cell_info: List[NrBNCellInfo]=None, nr_bn_cell_rsrp: int=None, nr_bn_cell_rsrq: int=None, nr_bn_cell_rssi: int=None):  # noqa: E501
        """NrBNCs - a model defined in Swagger

        :param nr_bn_cell_info: The nr_bn_cell_info of this NrBNCs.  # noqa: E501
        :type nr_bn_cell_info: List[NrBNCellInfo]
        :param nr_bn_cell_rsrp: The nr_bn_cell_rsrp of this NrBNCs.  # noqa: E501
        :type nr_bn_cell_rsrp: int
        :param nr_bn_cell_rsrq: The nr_bn_cell_rsrq of this NrBNCs.  # noqa: E501
        :type nr_bn_cell_rsrq: int
        :param nr_bn_cell_rssi: The nr_bn_cell_rssi of this NrBNCs.  # noqa: E501
        :type nr_bn_cell_rssi: int
        """
        self.swagger_types = {
            'nr_bn_cell_info': List[NrBNCellInfo],
            'nr_bn_cell_rsrp': int,
            'nr_bn_cell_rsrq': int,
            'nr_bn_cell_rssi': int
        }

        self.attribute_map = {
            'nr_bn_cell_info': 'nrBNCellInfo',
            'nr_bn_cell_rsrp': 'nrBNCellRsrp',
            'nr_bn_cell_rsrq': 'nrBNCellRsrq',
            'nr_bn_cell_rssi': 'nrBNCellRssi'
        }
        self._nr_bn_cell_info = nr_bn_cell_info
        self._nr_bn_cell_rsrp = nr_bn_cell_rsrp
        self._nr_bn_cell_rsrq = nr_bn_cell_rsrq
        self._nr_bn_cell_rssi = nr_bn_cell_rssi

    @classmethod
    def from_dict(cls, dikt) -> 'NrBNCs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrBNCs of this NrBNCs.  # noqa: E501
        :rtype: NrBNCs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nr_bn_cell_info(self) -> List[NrBNCellInfo]:
        """Gets the nr_bn_cell_info of this NrBNCs.

        Best neighbours of the secondary serving cell(s) info  # noqa: E501

        :return: The nr_bn_cell_info of this NrBNCs.
        :rtype: List[NrBNCellInfo]
        """
        return self._nr_bn_cell_info

    @nr_bn_cell_info.setter
    def nr_bn_cell_info(self, nr_bn_cell_info: List[NrBNCellInfo]):
        """Sets the nr_bn_cell_info of this NrBNCs.

        Best neighbours of the secondary serving cell(s) info  # noqa: E501

        :param nr_bn_cell_info: The nr_bn_cell_info of this NrBNCs.
        :type nr_bn_cell_info: List[NrBNCellInfo]
        """
        if nr_bn_cell_info is None:
            raise ValueError("Invalid value for `nr_bn_cell_info`, must not be `None`")  # noqa: E501

        self._nr_bn_cell_info = nr_bn_cell_info

    @property
    def nr_bn_cell_rsrp(self) -> int:
        """Gets the nr_bn_cell_rsrp of this NrBNCs.

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rsrp of this NrBNCs.
        :rtype: int
        """
        return self._nr_bn_cell_rsrp

    @nr_bn_cell_rsrp.setter
    def nr_bn_cell_rsrp(self, nr_bn_cell_rsrp: int):
        """Sets the nr_bn_cell_rsrp of this NrBNCs.

        Reference Signal Received Power measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rsrp: The nr_bn_cell_rsrp of this NrBNCs.
        :type nr_bn_cell_rsrp: int
        """

        self._nr_bn_cell_rsrp = nr_bn_cell_rsrp

    @property
    def nr_bn_cell_rsrq(self) -> int:
        """Gets the nr_bn_cell_rsrq of this NrBNCs.

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rsrq of this NrBNCs.
        :rtype: int
        """
        return self._nr_bn_cell_rsrq

    @nr_bn_cell_rsrq.setter
    def nr_bn_cell_rsrq(self, nr_bn_cell_rsrq: int):
        """Sets the nr_bn_cell_rsrq of this NrBNCs.

        Reference Signal Received Quality measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rsrq: The nr_bn_cell_rsrq of this NrBNCs.
        :type nr_bn_cell_rsrq: int
        """

        self._nr_bn_cell_rsrq = nr_bn_cell_rsrq

    @property
    def nr_bn_cell_rssi(self) -> int:
        """Gets the nr_bn_cell_rssi of this NrBNCs.

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :return: The nr_bn_cell_rssi of this NrBNCs.
        :rtype: int
        """
        return self._nr_bn_cell_rssi

    @nr_bn_cell_rssi.setter
    def nr_bn_cell_rssi(self, nr_bn_cell_rssi: int):
        """Sets the nr_bn_cell_rssi of this NrBNCs.

        Reference signal SINR measurement according to mapping table in ETSI TS 138.133 [i.14].  # noqa: E501

        :param nr_bn_cell_rssi: The nr_bn_cell_rssi of this NrBNCs.
        :type nr_bn_cell_rssi: int
        """

        self._nr_bn_cell_rssi = nr_bn_cell_rssi