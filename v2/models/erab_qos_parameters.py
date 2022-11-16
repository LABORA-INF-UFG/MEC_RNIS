# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.qos_information import QosInformation  # noqa: F401,E501
from v2 import util


class ErabQosParameters(Model):

    def __init__(self, qci: int, qos_information: QosInformation):  # noqa: E501
        """ErabQosParameters - a model defined in Swagger

        :param qci: The qci of this ErabQosParameters.  # noqa: E501
        :type qci: int
        :param qos_information: The qos_information of this ErabQosParameters.  # noqa: E501
        :type qos_information: QosInformation
        """
        
        self.qci = qci
        self.qos_information = qos_information
    
    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "qci": self.qci,
            "qos_information": self.qos_information
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ErabQosParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErabQosParameters of this ErabQosParameters.  # noqa: E501
        :rtype: ErabQosParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def qci(self) -> int:
        """Gets the qci of this ErabQosParameters.

        QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

        :return: The qci of this ErabQosParameters.
        :rtype: int
        """
        return self._qci

    @qci.setter
    def qci(self, qci: int):
        """Sets the qci of this ErabQosParameters.

        QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

        :param qci: The qci of this ErabQosParameters.
        :type qci: int
        """
        if qci is None:
            raise ValueError("Invalid value for `qci`, must not be `None`")  # noqa: E501

        self._qci = qci

    @property
    def qos_information(self) -> QosInformation:
        """Gets the qos_information of this ErabQosParameters.


        :return: The qos_information of this ErabQosParameters.
        :rtype: QosInformation
        """
        return self._qos_information

    @qos_information.setter
    def qos_information(self, qos_information: QosInformation):
        """Sets the qos_information of this ErabQosParameters.


        :param qos_information: The qos_information of this ErabQosParameters.
        :type qos_information: QosInformation
        """
        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if qos_information == "":
            raise ValueError("Invalid value for `qos_information`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe QosInformation passando os parametros erab_gbr_dl, erab_gbr_ul, erab_mbr_dl, erab_mbr_ul, 
        new_qos_information = QosInformation(**qos_information)
        
        # Chamo o método json da classe QosInformation para transformar os dados em json
        new_qos_information = new_qos_information.json()

        # Finalmente retorno o Json

        self._qos_information = new_qos_information
