# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  

from typing import List, Dict  
from flask_restful import request

from v2.models.base_model_ import Model
from v2.models.plmn import Plmn  
from v2.models.time_stamp import TimeStamp  
from v2 import util


class PlmnInfoModel(Model):

    #Construtor
    def __init__(self, app_instance_id: str, plmn: List[Plmn], time_stamp: List[TimeStamp]): 

        """PlmnInfo - a model

            Plmn = Identidade de Rede Móvel Terrestre Pública

            :param app_instance_id: The app_instance_id of this PlmnInfo. 
            :type app_instance_id: str
            :param plmn: The plmn of this PlmnInfo.  
            :type plmn: List[Plmn]
            :param time_stamp: The time_stamp of this PlmnInfo.  
            :type time_stamp: TimeStamp
        """

        self.app_instance_id = app_instance_id
        self.plmn = plmn
        self.time_stamp = time_stamp
        
        
        
    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            'app_instance_id': self.app_instance_id,
            'plmn': self.plmn,
            'time_stamp': self.time_stamp
        }


    @classmethod
    def from_dict(cls, dikt) -> 'PlmnInfoModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PlmnInfo of this PlmnInfo.  # noqa: E501
        :rtype: PlmnInfo
        """

        return util.deserialize_model(dikt, cls)

#
#    Você pode definir propriedades com a sintaxe @property, que é mais compacta e legível.
#    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
#    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, 
#    para adicionar getters, setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar 
#    ou modificar os dados diretamente.

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this PlmnInfo.

            Identificador exclusivo para a instância do aplicativo MEC.

            :return: The app_instance_id of this PlmnInfo.
            :rtype: str
        """
        
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this PlmnInfo.

            Identificador exclusivo para a instância do aplicativo MEC.

            :param app_instance_id: The app_instance_id of this PlmnInfo.
            :type app_instance_id: str
        """
        
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  

        self._app_instance_id = app_instance_id

    @property
    def plmn(self) -> Plmn:
        """Gets the plmn of this PlmnInfo.

            Identidade de Rede Móvel Terrestre Pública.

            :return: The plmn of this PlmnInfo.
            :rtype: List[Plmn]
        """
        return self._plmn

    @plmn.setter
    def plmn(self, plmn: Plmn):


        """Sets the plmn of this PlmnInfo.

            Identidade de Rede Móvel Terrestre Pública.

            :param plmn: The plmn of this PlmnInfo.
            :type plmn: List[Plmn]
        """
       # Verifica se não é vazio porem ainda não tem tratamento de erro
        if plmn == "":
            raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

        # Chamo o construtor da classe Plmn passando os parametros mcc e mnc
        #new_plmn = Plmn(plmn['mcc'],plmn['mnc'])
        new_plmn = Plmn(**plmn)
        
        # Chamo o método json da classe Plmn para transformar os dados em json
        new_plmn = new_plmn.json()

        # Finalmente retorno o Json
        self._plmn = new_plmn

    @property
    def time_stamp(self) -> TimeStamp:
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):

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
