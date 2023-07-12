# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.erab_qos_parameters import ErabQosParameters  # noqa: F401,E501
from v2 import util


class ErabInfo(Model):

    def __init__(self, erab_id: int, erab_qos_parameters: ErabQosParameters):  # noqa: E501
        """ErabInfo - a model

        :param erab_id: The erab_id of this ErabInfo.  # noqa: E501
        :type erab_id: int
        :param erab_qos_parameters: The erab_qos_parameters of this ErabInfo.  # noqa: E501
        :type erab_qos_parameters: ErabQosParameters
        """

        self.erab_id = erab_id
        self.erab_qos_parameters = erab_qos_parameters

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "erab_id": self.erab_id,
            "erab_qos_parameters": self.erab_qos_parameters
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ErabInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErabInfo of this ErabInfo.  # noqa: E501
        :rtype: ErabInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def erab_id(self) -> int:
        """Gets the erab_id of this ErabInfo.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this ErabInfo.
        :rtype: int
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id: int):
        """Sets the erab_id of this ErabInfo.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this ErabInfo.
        :type erab_id: int
        """

        self._erab_id = erab_id

    @property
    def erab_qos_parameters(self) -> ErabQosParameters:
        """Gets the erab_qos_parameters of this ErabInfo.


        :return: The erab_qos_parameters of this ErabInfo.
        :rtype: ErabQosParameters
        """
        return self._erab_qos_parameters

    @erab_qos_parameters.setter
    def erab_qos_parameters(self, erab_qos_parameters: ErabQosParameters):
        """Sets the erab_qos_parameters of this ErabInfo.

        :param erab_qos_parameters: The erab_qos_parameters of this ErabInfo.
        :type erab_qos_parameters: ErabQosParameters
        """
        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if erab_qos_parameters == "":
            raise ValueError("Invalid value for `ErabQosParameters`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe ErabQosParameters passando os parametros qci e qos_information
        new_erab_qos_parameters = ErabQosParameters(**erab_qos_parameters)
        
        # Chamo o método json da classe ErabQosParameters para transformar os dados em json
        new_erab_qos_parameters = new_erab_qos_parameters.json()

        # Finalmente retorno o Json
        self._erab_qos_parameters = new_erab_qos_parameters
