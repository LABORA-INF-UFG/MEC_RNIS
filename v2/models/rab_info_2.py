# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime
# import imp
# from math import degrees  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.cell_user_info import CellUserInfo  # noqa: F401,E501
from v2.models.time_stamp import TimeStamp  # noqa: F401,E501
from v2 import util


class RabInfoModel(Model):

    
    #Construtor
    def __init__(self, app_instance_id: str=None, cell_user_info: List[CellUserInfo]=None, request_id: str=None, time_stamp: TimeStamp=None):  # noqa: E501
       
        self.swagger_types = {
            'app_instance_id': str,
            'cell_user_info': List[CellUserInfo],
            'request_id': str,
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'cell_user_info': 'cellUserInfo',
            'request_id': 'requestId',
            'time_stamp': 'timeStamp'
        }
        self._app_instance_id = app_instance_id
        self._cell_user_info = cell_user_info
        self._request_id = request_id
        self._time_stamp = time_stamp

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            'app_instance_id': self.app_instance_id,
            'cell_user_info': self.cell_user_info,
            'request_id': self.request_id,
            'time_stamp': self.time_stamp,
        }

    @classmethod
    def from_dict(cls, dikt) -> 'RabInfoModel':
        
        return util.deserialize_model(dikt, cls)

#
#    Você pode definir propriedades com a sintaxe @property, que é mais compacta e legível.
#    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
#    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, 
#    para adicionar getters, setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar 
#    ou modificar os dados diretamente.

    @property
    def app_instance_id(self) -> str:
       
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this RabInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this RabInfo.
        :type app_instance_id: str
        """
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

        self._app_instance_id = app_instance_id

    @property
    def cell_user_info(self) -> List[CellUserInfo]:
        """Gets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :return: The cell_user_info of this RabInfo.
        :rtype: List[CellUserInfo]
        """
        return self._cell_user_info

    @cell_user_info.setter
    def cell_user_info(self, cell_user_info: List[CellUserInfo]):
        """Sets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :param cell_user_info: The cell_user_info of this RabInfo.
        :type cell_user_info: List[CellUserInfo]
        """

        self._cell_user_info = cell_user_info

    @property
    def request_id(self) -> str:
        """Gets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :return: The request_id of this RabInfo.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :param request_id: The request_id of this RabInfo.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this RabInfo.


        :return: The time_stamp of this RabInfo.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):



    
        """Sets the time_stamp of this RabInfo.


        :param time_stamp: The time_stamp of this RabInfo.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp

