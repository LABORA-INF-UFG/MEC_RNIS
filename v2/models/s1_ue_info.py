# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.associate_id import AssociateId  # noqa: F401,E501
from v2.models.ecgi import Ecgi  # noqa: F401,E501
from v2.models.s1_bearer_info_detailed import S1BearerInfoDetailed  # noqa: F401,E501
from v2.models.temp_ue_id import TempUeId  # noqa: F401,E501
from v2 import util


class S1UeInfo(Model):

    def __init__(self, associate_id: List[AssociateId], ecgi: List[Ecgi], s1_bearer_info_detailed: List[S1BearerInfoDetailed], temp_ue_id: TempUeId):  # noqa: E501
        """S1UeInfo - a model defined in Swagger

        :param associate_id: The associate_id of this S1UeInfo.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this S1UeInfo.  # noqa: E501
        :type ecgi: List[Ecgi]
        :param s1_bearer_info_detailed: The s1_bearer_info_detailed of this S1UeInfo.  # noqa: E501
        :type s1_bearer_info_detailed: List[S1BearerInfoDetailed]
        :param temp_ue_id: The temp_ue_id of this S1UeInfo.  # noqa: E501
        :type temp_ue_id: TempUeId
        """

        self.associate_id = associate_id
        self.ecgi = ecgi
        self.s1_bearer_info_detailed = s1_bearer_info_detailed
        self.temp_ue_id = temp_ue_id

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            'associate_id': self.associate_id,
            'ecgi': self.ecgi,
            's1_bearer_info_detailed': self.s1_bearer_info_detailed,
            'temp_ue_id': self.temp_ue_id
        }

    @classmethod
    def from_dict(cls, dikt) -> 'S1UeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The S1UeInfo of this S1UeInfo.  # noqa: E501
        :rtype: S1UeInfo
        """
        return util.deserialize_model(dikt, cls)

#
#    Você pode definir propriedades com a sintaxe @property, que é mais compacta e legível.
#    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
#    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, 
#    para adicionar getters, setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar 
#    ou modificar os dados diretamente.

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this S1UeInfo.

        1 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this S1UeInfo.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this S1UeInfo.

        1 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this S1UeInfo.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> List[Ecgi]:
        """Gets the ecgi of this S1UeInfo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this S1UeInfo.
        :rtype: List[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: List[Ecgi]):
        """Sets the ecgi of this S1UeInfo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this S1UeInfo.
        :type ecgi: List[Ecgi]
        """

        # Chamo o construtor da classe Ecgi passando os parametros cell_id e plmn
        new_ecgi = Ecgi(**ecgi)
        
        # Chamo o método json da classe Ecgi para transformar os dados em json
        new_ecgi = new_ecgi.json()
        
        # Finalmente retorno o Json
        self._ecgi = new_ecgi

    @property
    def s1_bearer_info_detailed(self) -> List[S1BearerInfoDetailed]:
        """Gets the s1_bearer_info_detailed of this S1UeInfo.

        S1 bearer information as defined below.  # noqa: E501

        :return: The s1_bearer_info_detailed of this S1UeInfo.
        :rtype: List[S1BearerInfoDetailed]
        """
        return self._s1_bearer_info_detailed

    @s1_bearer_info_detailed.setter
    def s1_bearer_info_detailed(self, s1_bearer_info_detailed: List[S1BearerInfoDetailed]):
        """Sets the s1_bearer_info_detailed of this S1UeInfo.

        S1 bearer information as defined below.  # noqa: E501

        :param s1_bearer_info_detailed: The s1_bearer_info_detailed of this S1UeInfo.
        :type s1_bearer_info_detailed: List[S1BearerInfoDetailed]
        """
        # Chamo o construtor da classe S1BearerInfoDetailed passando os parametros enb_info, erab_id e s_gw_info
        new_s1_bearer_info_detailed = S1BearerInfoDetailed(**s1_bearer_info_detailed)
        
        # Chamo o método json da classe S1BearerInfoDetailed para transformar os dados em json
        new_s1_bearer_info_detailed = new_s1_bearer_info_detailed.json()
        
        # Finalmente retorno o Json
        self._s1_bearer_info_detailed = new_s1_bearer_info_detailed

    @property
    def temp_ue_id(self) -> TempUeId:
        """Gets the temp_ue_id of this S1UeInfo.


        :return: The temp_ue_id of this S1UeInfo.
        :rtype: TempUeId
        """
        return self._temp_ue_id

    @temp_ue_id.setter
    def temp_ue_id(self, temp_ue_id: TempUeId):
        """Sets the temp_ue_id of this S1UeInfo.


        :param temp_ue_id: The temp_ue_id of this S1UeInfo.
        :type temp_ue_id: TempUeId
        """
        # Chamo o construtor da classe TempUeId passando os parametros mmec e mtmsi
        new_temp_ue_id = TempUeId(**temp_ue_id)
        
        # Chamo o método json da classe TempUeId para transformar os dados em json
        new_temp_ue_id = new_temp_ue_id.json()
        
        # Finalmente retorno o Json
        self._temp_ue_id = new_temp_ue_id
