# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.ecgi import Ecgi  # noqa: F401,E501
from v2.models.ue_info import UeInfo  # noqa: F401,E501
from v2 import util

class CellUserInfo(Model):

    def __init__(self, ecgi: Ecgi, ue_info: List[UeInfo]):  # noqa: E501
        """CellUserInfo - a model defined in Swagger

        :param ecgi: The ecgi of this CellUserInfo.  # noqa: E501
        :type ecgi: Ecgi
        :param ue_info: The ue_info of this CellUserInfo.  # noqa: E501
        :type ue_info: List[UeInfo]
        """
        
        self.ecgi = ecgi
        self.ue_info = ue_info

    def json(self):
        return {
            "ecgi": self.ecgi,
            "ue_info": self.ue_info
        }


    @classmethod
    def from_dict(cls, dikt) -> 'CellUserInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CellUserInfo of this CellUserInfo.  # noqa: E501
        :rtype: CellUserInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this CellUserInfo.


        :return: The ecgi of this CellUserInfo.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this CellUserInfo.


        :param ecgi: The ecgi of this CellUserInfo.
        :type ecgi: Ecgi
        """
        # Chamo o construtor da classe Ecgi passando os parametros mcc e mnc
        new_ecgi = Ecgi(**ecgi)
        
        # Chamo o método json da classe Ecgi para transformar os dados em json
        new_ecgi = new_ecgi.json()

        # Finalmente retorno o Json
        self._ecgi = new_ecgi

    @property
    def ue_info(self) -> List[UeInfo]:
        """Gets the ue_info of this CellUserInfo.

        Information on UEs in the specific cell as defined below.  # noqa: E501

        :return: The ue_info of this CellUserInfo.
        :rtype: List[UeInfo]
        """
        return self._ue_info

    @ue_info.setter
    def ue_info(self, ue_info: List[UeInfo]):
        """Sets the ue_info of this CellUserInfo.

        Information on UEs in the specific cell as defined below.  # noqa: E501

        :param ue_info: The ue_info of this CellUserInfo.
        :type ue_info: List[UeInfo]
        """
        
        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if ue_info == "":
            raise ValueError("Invalid value for `ue_info`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe UeInfo passando os parametros mcc e mnc
        new_ue_info = UeInfo(**ue_info)
        
        # Chamo o método json da classe UeInfo para transformar os dados em json
        new_ue_info = new_ue_info.json()

        # Finalmente retorno o Json
        self._ue_info = new_ue_info
