# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meas_quantity_results_nr import MeasQuantityResultsNr  # noqa: F401,E501
from swagger_server.models.nrcgi import Nrcgi  # noqa: F401,E501
from swagger_server.models.rs_index_results import RsIndexResults  # noqa: F401,E501
from swagger_server import util


class NrNeighCellMeasInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr=None, meas_quantity_results_ssb_cell: MeasQuantityResultsNr=None, nrcgi: Nrcgi=None, rs_index_results: RsIndexResults=None):  # noqa: E501
        """NrNeighCellMeasInfo - a model defined in Swagger

        :param meas_quantity_results_csi_rs_cell: The meas_quantity_results_csi_rs_cell of this NrNeighCellMeasInfo.  # noqa: E501
        :type meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr
        :param meas_quantity_results_ssb_cell: The meas_quantity_results_ssb_cell of this NrNeighCellMeasInfo.  # noqa: E501
        :type meas_quantity_results_ssb_cell: MeasQuantityResultsNr
        :param nrcgi: The nrcgi of this NrNeighCellMeasInfo.  # noqa: E501
        :type nrcgi: Nrcgi
        :param rs_index_results: The rs_index_results of this NrNeighCellMeasInfo.  # noqa: E501
        :type rs_index_results: RsIndexResults
        """
        self.swagger_types = {
            'meas_quantity_results_csi_rs_cell': MeasQuantityResultsNr,
            'meas_quantity_results_ssb_cell': MeasQuantityResultsNr,
            'nrcgi': Nrcgi,
            'rs_index_results': RsIndexResults
        }

        self.attribute_map = {
            'meas_quantity_results_csi_rs_cell': 'measQuantityResultsCsiRsCell',
            'meas_quantity_results_ssb_cell': 'measQuantityResultsSsbCell',
            'nrcgi': 'nrcgi',
            'rs_index_results': 'rsIndexResults'
        }
        self._meas_quantity_results_csi_rs_cell = meas_quantity_results_csi_rs_cell
        self._meas_quantity_results_ssb_cell = meas_quantity_results_ssb_cell
        self._nrcgi = nrcgi
        self._rs_index_results = rs_index_results

    @classmethod
    def from_dict(cls, dikt) -> 'NrNeighCellMeasInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrNeighCellMeasInfo of this NrNeighCellMeasInfo.  # noqa: E501
        :rtype: NrNeighCellMeasInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meas_quantity_results_csi_rs_cell(self) -> MeasQuantityResultsNr:
        """Gets the meas_quantity_results_csi_rs_cell of this NrNeighCellMeasInfo.


        :return: The meas_quantity_results_csi_rs_cell of this NrNeighCellMeasInfo.
        :rtype: MeasQuantityResultsNr
        """
        return self._meas_quantity_results_csi_rs_cell

    @meas_quantity_results_csi_rs_cell.setter
    def meas_quantity_results_csi_rs_cell(self, meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr):
        """Sets the meas_quantity_results_csi_rs_cell of this NrNeighCellMeasInfo.


        :param meas_quantity_results_csi_rs_cell: The meas_quantity_results_csi_rs_cell of this NrNeighCellMeasInfo.
        :type meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr
        """

        self._meas_quantity_results_csi_rs_cell = meas_quantity_results_csi_rs_cell

    @property
    def meas_quantity_results_ssb_cell(self) -> MeasQuantityResultsNr:
        """Gets the meas_quantity_results_ssb_cell of this NrNeighCellMeasInfo.


        :return: The meas_quantity_results_ssb_cell of this NrNeighCellMeasInfo.
        :rtype: MeasQuantityResultsNr
        """
        return self._meas_quantity_results_ssb_cell

    @meas_quantity_results_ssb_cell.setter
    def meas_quantity_results_ssb_cell(self, meas_quantity_results_ssb_cell: MeasQuantityResultsNr):
        """Sets the meas_quantity_results_ssb_cell of this NrNeighCellMeasInfo.


        :param meas_quantity_results_ssb_cell: The meas_quantity_results_ssb_cell of this NrNeighCellMeasInfo.
        :type meas_quantity_results_ssb_cell: MeasQuantityResultsNr
        """

        self._meas_quantity_results_ssb_cell = meas_quantity_results_ssb_cell

    @property
    def nrcgi(self) -> Nrcgi:
        """Gets the nrcgi of this NrNeighCellMeasInfo.


        :return: The nrcgi of this NrNeighCellMeasInfo.
        :rtype: Nrcgi
        """
        return self._nrcgi

    @nrcgi.setter
    def nrcgi(self, nrcgi: Nrcgi):
        """Sets the nrcgi of this NrNeighCellMeasInfo.


        :param nrcgi: The nrcgi of this NrNeighCellMeasInfo.
        :type nrcgi: Nrcgi
        """
        if nrcgi is None:
            raise ValueError("Invalid value for `nrcgi`, must not be `None`")  # noqa: E501

        self._nrcgi = nrcgi

    @property
    def rs_index_results(self) -> RsIndexResults:
        """Gets the rs_index_results of this NrNeighCellMeasInfo.


        :return: The rs_index_results of this NrNeighCellMeasInfo.
        :rtype: RsIndexResults
        """
        return self._rs_index_results

    @rs_index_results.setter
    def rs_index_results(self, rs_index_results: RsIndexResults):
        """Sets the rs_index_results of this NrNeighCellMeasInfo.


        :param rs_index_results: The rs_index_results of this NrNeighCellMeasInfo.
        :type rs_index_results: RsIndexResults
        """

        self._rs_index_results = rs_index_results
