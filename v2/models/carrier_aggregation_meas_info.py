# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CarrierAggregationMeasInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cell_id_nei: str=None, cell_id_srv: str=None, rsrp_nei: int=None, rsrp_srv: int=None, rsrq_nei: int=None, rsrq_srv: int=None):  # noqa: E501
        """CarrierAggregationMeasInfo - a model defined in Swagger

        :param cell_id_nei: The cell_id_nei of this CarrierAggregationMeasInfo.  # noqa: E501
        :type cell_id_nei: str
        :param cell_id_srv: The cell_id_srv of this CarrierAggregationMeasInfo.  # noqa: E501
        :type cell_id_srv: str
        :param rsrp_nei: The rsrp_nei of this CarrierAggregationMeasInfo.  # noqa: E501
        :type rsrp_nei: int
        :param rsrp_srv: The rsrp_srv of this CarrierAggregationMeasInfo.  # noqa: E501
        :type rsrp_srv: int
        :param rsrq_nei: The rsrq_nei of this CarrierAggregationMeasInfo.  # noqa: E501
        :type rsrq_nei: int
        :param rsrq_srv: The rsrq_srv of this CarrierAggregationMeasInfo.  # noqa: E501
        :type rsrq_srv: int
        """
        self.swagger_types = {
            'cell_id_nei': str,
            'cell_id_srv': str,
            'rsrp_nei': int,
            'rsrp_srv': int,
            'rsrq_nei': int,
            'rsrq_srv': int
        }

        self.attribute_map = {
            'cell_id_nei': 'cellIdNei',
            'cell_id_srv': 'cellIdSrv',
            'rsrp_nei': 'rsrpNei',
            'rsrp_srv': 'rsrpSrv',
            'rsrq_nei': 'rsrqNei',
            'rsrq_srv': 'rsrqSrv'
        }
        self._cell_id_nei = cell_id_nei
        self._cell_id_srv = cell_id_srv
        self._rsrp_nei = rsrp_nei
        self._rsrp_srv = rsrp_srv
        self._rsrq_nei = rsrq_nei
        self._rsrq_srv = rsrq_srv

    @classmethod
    def from_dict(cls, dikt) -> 'CarrierAggregationMeasInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CarrierAggregationMeasInfo of this CarrierAggregationMeasInfo.  # noqa: E501
        :rtype: CarrierAggregationMeasInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cell_id_nei(self) -> str:
        """Gets the cell_id_nei of this CarrierAggregationMeasInfo.

        String representing the E-UTRAN Cell Identity. Encoded as a bit string (size (28)) as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The cell_id_nei of this CarrierAggregationMeasInfo.
        :rtype: str
        """
        return self._cell_id_nei

    @cell_id_nei.setter
    def cell_id_nei(self, cell_id_nei: str):
        """Sets the cell_id_nei of this CarrierAggregationMeasInfo.

        String representing the E-UTRAN Cell Identity. Encoded as a bit string (size (28)) as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param cell_id_nei: The cell_id_nei of this CarrierAggregationMeasInfo.
        :type cell_id_nei: str
        """
        if cell_id_nei is None:
            raise ValueError("Invalid value for `cell_id_nei`, must not be `None`")  # noqa: E501

        self._cell_id_nei = cell_id_nei

    @property
    def cell_id_srv(self) -> str:
        """Gets the cell_id_srv of this CarrierAggregationMeasInfo.

        String representing the E-UTRAN Cell Identity. Encoded as a bit string (size (28)) as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The cell_id_srv of this CarrierAggregationMeasInfo.
        :rtype: str
        """
        return self._cell_id_srv

    @cell_id_srv.setter
    def cell_id_srv(self, cell_id_srv: str):
        """Sets the cell_id_srv of this CarrierAggregationMeasInfo.

        String representing the E-UTRAN Cell Identity. Encoded as a bit string (size (28)) as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param cell_id_srv: The cell_id_srv of this CarrierAggregationMeasInfo.
        :type cell_id_srv: str
        """
        if cell_id_srv is None:
            raise ValueError("Invalid value for `cell_id_srv`, must not be `None`")  # noqa: E501

        self._cell_id_srv = cell_id_srv

    @property
    def rsrp_nei(self) -> int:
        """Gets the rsrp_nei of this CarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrp_nei of this CarrierAggregationMeasInfo.
        :rtype: int
        """
        return self._rsrp_nei

    @rsrp_nei.setter
    def rsrp_nei(self, rsrp_nei: int):
        """Sets the rsrp_nei of this CarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrp_nei: The rsrp_nei of this CarrierAggregationMeasInfo.
        :type rsrp_nei: int
        """

        self._rsrp_nei = rsrp_nei

    @property
    def rsrp_srv(self) -> int:
        """Gets the rsrp_srv of this CarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrp_srv of this CarrierAggregationMeasInfo.
        :rtype: int
        """
        return self._rsrp_srv

    @rsrp_srv.setter
    def rsrp_srv(self, rsrp_srv: int):
        """Sets the rsrp_srv of this CarrierAggregationMeasInfo.

        Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrp_srv: The rsrp_srv of this CarrierAggregationMeasInfo.
        :type rsrp_srv: int
        """

        self._rsrp_srv = rsrp_srv

    @property
    def rsrq_nei(self) -> int:
        """Gets the rsrq_nei of this CarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrq_nei of this CarrierAggregationMeasInfo.
        :rtype: int
        """
        return self._rsrq_nei

    @rsrq_nei.setter
    def rsrq_nei(self, rsrq_nei: int):
        """Sets the rsrq_nei of this CarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrq_nei: The rsrq_nei of this CarrierAggregationMeasInfo.
        :type rsrq_nei: int
        """

        self._rsrq_nei = rsrq_nei

    @property
    def rsrq_srv(self) -> int:
        """Gets the rsrq_srv of this CarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :return: The rsrq_srv of this CarrierAggregationMeasInfo.
        :rtype: int
        """
        return self._rsrq_srv

    @rsrq_srv.setter
    def rsrq_srv(self, rsrq_srv: int):
        """Sets the rsrq_srv of this CarrierAggregationMeasInfo.

        Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

        :param rsrq_srv: The rsrq_srv of this CarrierAggregationMeasInfo.
        :type rsrq_srv: int
        """

        self._rsrq_srv = rsrq_srv