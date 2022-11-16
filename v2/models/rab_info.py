# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime
from math import degrees  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.cell_user_info import CellUserInfo  # noqa: F401,E501
from v2.models.time_stamp import TimeStamp  # noqa: F401,E501
from v2 import util

class RabInfoModel(Model):

    #Construtor
    def __init__(self, app_instance_id: str, cell_user_info: List[CellUserInfo], request_id: str, time_stamp: TimeStamp):  # noqa: E501
       
        """RabInfo - a model

        :param app_instance_id: The app_instance_id of this RabInfo.  # noqa: E501
        :type app_instance_id: str
        :param cell_user_info: The cell_user_info of this RabInfo.  # noqa: E501
        :type cell_user_info: List[CellUserInfo]
        :param request_id: The request_id of this RabInfo.  # noqa: E501
        :type request_id: str
        :param time_stamp: The time_stamp of this RabInfo.  # noqa: E501
        :type time_stamp: TimeStamp
        """

        self.app_instance_id = app_instance_id
        self.cell_user_info = cell_user_info
        self.request_id = request_id
        self.time_stamp = time_stamp

 
    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "app_instance_id": self.app_instance_id,
            "cell_user_info": self.cell_user_info,
            "request_id": self.request_id,
            "time_stamp": self.time_stamp
        }

    @classmethod
    def from_dict(cls, dikt) -> 'RabInfoModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabInfo of this RabInfo.  # noqa: E501
        :rtype: RabInfo
        """
        return util.deserialize_model(dikt, cls)


#
#    Você pode definir propriedades com a sintaxe @property, que é mais compacta e legível.
#    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
#    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, 
#    para adicionar getters, setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar 
#    ou modificar os dados diretamente.

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this RabInfo.

            Unique identifier for the MEC application instance. 

        :return: The app_instance_id of this RabInfo.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this RabInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this RabInfo.
        :type app_instance_id: str
        """
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

        self._app_instance_id = app_instance_id

    @property
    def cell_user_info(self):
        """Gets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :return: The cell_user_info of this RabInfo.
        :rtype: List[CellUserInfo]
        """
        return self._cell_user_info

    @cell_user_info.setter
    def cell_user_info(self, cell_user_info):
        """Sets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :param cell_user_info: The cell_user_info of this RabInfo.
        :type cell_user_info: List[CellUserInfo]
        """
        # Verifica se não é vazio porem ainda não tem tratamento de erro
        if cell_user_info == "":
            raise ValueError("Invalid value for `cell_user_info`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe CellUserInfo passando os parametros mcc e mnc
        new_cell_user_info = CellUserInfo(**cell_user_info)
        
        # Chamo o método json da classe CellUserInfo para transformar os dados em json
        new_cell_user_info = new_cell_user_info.json()
        
        # Finalmente retorno o Json
        self._cell_user_info = new_cell_user_info

    @property
    def request_id(self):
        """Gets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :return: The request_id of this RabInfo.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :param request_id: The request_id of this RabInfo.
        :type request_id: str
        """
        if request_id == "":
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def time_stamp(self):
        """Gets the time_stamp of this RabInfo.

        :return: The time_stamp of this RabInfo.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):

        """Sets the time_stamp of this RabInfo.

        :param time_stamp: The time_stamp of this RabInfo.
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
        self._time_stamp = new_time_stamp



