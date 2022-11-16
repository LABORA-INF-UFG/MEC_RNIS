# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.s1_ue_info import S1UeInfo  # noqa: F401,E501
from v2.models.time_stamp import TimeStamp  # noqa: F401,E501
from v2 import util


class S1BearerInfoModel(Model):
   
    def __init__(self, s1_ue_info: List[S1UeInfo], time_stamp: TimeStamp):  # noqa: E501
        """S1BearerInfo - a model defined in Swagger

        :param s1_ue_info: The s1_ue_info of this S1BearerInfo.  # noqa: E501
        :type s1_ue_info: List[S1UeInfo]
        :param time_stamp: The time_stamp of this S1BearerInfo.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.s1_ue_info = s1_ue_info
        self.time_stamp = time_stamp

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            's1_ue_info': self.s1_ue_info,
            'time_stamp': self.time_stamp
        }

    @classmethod
    def from_dict(cls, dikt) -> 'S1BearerInfoModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The S1BearerInfo of this S1BearerInfo.  # noqa: E501
        :rtype: S1BearerInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s1_ue_info(self) -> List[S1UeInfo]:
        """Gets the s1_ue_info of this S1BearerInfo.

        Information on a specific UE as defined below.  # noqa: E501

        :return: The s1_ue_info of this S1BearerInfo.
        :rtype: List[S1UeInfo]
        """
        return self._s1_ue_info

    @s1_ue_info.setter
    def s1_ue_info(self, s1_ue_info: List[S1UeInfo]):
        """Sets the s1_ue_info of this S1BearerInfo.

        Information on a specific UE as defined below.  # noqa: E501

        :param s1_ue_info: The s1_ue_info of this S1BearerInfo.
        :type s1_ue_info: List[S1UeInfo]
        """
        if s1_ue_info == "":
            raise ValueError("Invalid value for `s1_ue_info`, must not be `None`")  # noqa: E501

         # Chamo o construtor da classe S1UeInfo passando os parametros associate_id, ecgi, s1_bearer_info_detailed, temp_ue_id
        new_s1_ue_info = S1UeInfo(**s1_ue_info)
        
        # Chamo o método json da classe S1UeInfo para transformar os dados em json
        new_s1_ue_info = new_s1_ue_info.json()

        # Finalmente retorno o Json
        self._s1_ue_info = new_s1_ue_info

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this S1BearerInfo.


        :return: The time_stamp of this S1BearerInfo.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this S1BearerInfo.


        :param time_stamp: The time_stamp of this S1BearerInfo.
        :type time_stamp: TimeStamp
        """
        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if time_stamp == "":
            raise ValueError("Invalid value for `time_stamp`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe TimeStamp passando os parametros nano_seconds e seconds
        #new_time_stamp =  TimeStamp(time_stamp['nano_seconds'],time_stamp['seconds'])   
        new_time_stamp = TimeStamp(**time_stamp)
 
        # Chamo o método json da classe TimeStamp para transformar os dados em json
        new_time_stamp = new_time_stamp.json()
       
        # Finalmente retorno o Json
        self._time_stamp = time_stamp
