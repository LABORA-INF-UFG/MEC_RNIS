# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime

from typing import List, Dict

from v2.models.base_model_ import Model
from v2 import util


class Plmn(Model):

    def __init__(self, mcc: str, mnc: str):

        """Plmn - a model 

        :param mcc: The mcc of this Plmn.  # noqa: E501
        :type mcc: str
        :param mnc: The mnc of this Plmn.  # noqa: E501
        :type mnc: str
        """
        self.mcc = mcc
        self.mnc = mnc

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "mcc": self.mcc,
            "mnc": self.mnc
        }
    @classmethod
    def from_dict(cls, dikt) -> 'Plmn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Plmn of this Plmn.  # noqa: E501
        :rtype: Plmn
        """
        return util.deserialize_model(dikt, cls)

    #    O uso de @property pode ser considerada a maneira "pytônica" de definir getters, setters e deleters.
    #    Ao definir propriedades, você pode alterar a implementação interna de uma classe sem afetar o programa, 
    #    para adicionar getters, setters e deleters que atuam como intermediários "nos bastidores" para evitar acessar 
    #    ou modificar os dados diretamente.


    @property
    def mcc(self):
        """Gets the mcc of this Plmn.

        O Código do País Móvel faz parte da Identidade PLMN conforme definido em ETSI TS 136 413 [i.3].

        :return: The mcc of this Plmn.
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        
        """Sets the mcc of this Plmn.

        O Código do País Móvel faz parte da Identidade PLMN conforme definido em ETSI TS 136 413 [i.3].

        :param mcc: The mcc of this Plmn.
        :type mcc: str
        """
       # Verifica se não é vazio porem ainda não tem tratamento de erro
        if mcc == "":
            raise ValueError("Invalid value for `mcc`, must not be `None`")

        self._mcc =  mcc

    @property
    def mnc(self) -> str:
        """Gets the mnc of this Plmn.

        The Mobile Network Code part of PLMN Identity as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The mnc of this Plmn.
        :rtype: str
        """
        return self._mnc

    @mnc.setter
    def mnc(self, mnc: str):
        """Sets the mnc of this Plmn.

        The Mobile Network Code part of PLMN Identity as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param mnc: The mnc of this Plmn.
        :type mnc: str
        """
       # Verifica se não é vazio porem ainda não tem tratamento de erro
        if mnc == "":
            raise ValueError("Invalid value for `mnc`, must not be `None`")
        self._mnc = mnc
