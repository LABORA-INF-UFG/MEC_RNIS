# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.associate_id import AssociateId  # noqa: F401,E501
from v2.models.erab_info import ErabInfo  # noqa: F401,E501
from v2 import util


class UeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: List[AssociateId], erab_info: List[ErabInfo]):  # noqa: E501
        """UeInfo - a model defined in Swagger

        :param associate_id: The associate_id of this UeInfo.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param erab_info: The erab_info of this UeInfo.  # noqa: E501
        :type erab_info: List[ErabInfo]
        """

        self.associate_id = associate_id
        self.erab_info = erab_info

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "associate_id": self.associate_id,
            "erab_info": self.erab_info
        }


    @classmethod
    def from_dict(cls, dikt) -> 'UeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeInfo of this UeInfo.  # noqa: E501
        :rtype: UeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this UeInfo.

        0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this UeInfo.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this UeInfo.

        0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this UeInfo.
        :type associate_id: List[AssociateId]
        """

        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if associate_id == "":
            raise ValueError("Invalid value for `associate_id`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe associate_id passando os parametros type e value
        new_associate_id = AssociateId(**associate_id)
        
        # Chamo o método json da classe associate_id para transformar os dados em json
        new_associate_id = new_associate_id.json()

        # Finalmente retorno o Json
        self._associate_id = new_associate_id

    @property
    def erab_info(self) -> List[ErabInfo]:
        """Gets the erab_info of this UeInfo.

        Information on E-RAB as defined below.  # noqa: E501

        :return: The erab_info of this UeInfo.
        :rtype: List[ErabInfo]
        """
        return self._erab_info

    @erab_info.setter
    def erab_info(self, erab_info: List[ErabInfo]):
        """Sets the erab_info of this UeInfo.

        Information on E-RAB as defined below.  # noqa: E501

        :param erab_info: The erab_info of this UeInfo.
        :type erab_info: List[ErabInfo]
        """

        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if erab_info == "":
            raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe ErabInfo passando os parametros erab_id e erab_qos_parameters
        new_erab_info = ErabInfo(**erab_info)
        
        # Chamo o método json da classe ErabInfo para transformar os dados em json
        new_erab_info = new_erab_info.json()

        # Finalmente retorno o Json
        self._erab_info = new_erab_info
