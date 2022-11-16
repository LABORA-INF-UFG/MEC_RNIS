from __future__ import absolute_import
from datetime import date, datetime  

from typing import List, Dict  

from v2.models.base_model_ import Model
from v2 import util


class SGwInfo(Model):

    def __init__(self, ip_address: str, tunnel_id: str): 
        """SGwInfo - a model defined in Swagger

        :param ip_address: The ip_address of this SGwInfo. 
        :type ip_address: str
        :param tunnel_id: The tunnel_id of this SGwInfo.
        :type tunnel_id: str
        """

        self._ip_address = ip_address
        self._tunnel_id = tunnel_id

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            'ip_address': self.ip_address,
            'tunnel_id': self.tunnel_id
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SGwInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SGwInfo of this SGwInfo.  # noqa: E501
        :rtype: SGwInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_address(self) -> str:
        """Gets the ip_address of this SGwInfo.

        SGW transport layer address of this S1 bearer.  # noqa: E501

        :return: The ip_address of this SGwInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        """Sets the ip_address of this SGwInfo.

        SGW transport layer address of this S1 bearer.  # noqa: E501

        :param ip_address: The ip_address of this SGwInfo.
        :type ip_address: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def tunnel_id(self) -> str:
        """Gets the tunnel_id of this SGwInfo.

        SGW GTP-U TEID of this S1 bearer.  # noqa: E501

        :return: The tunnel_id of this SGwInfo.
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id: str):
        """Sets the tunnel_id of this SGwInfo.

        SGW GTP-U TEID of this S1 bearer.  # noqa: E501

        :param tunnel_id: The tunnel_id of this SGwInfo.
        :type tunnel_id: str
        """
        if tunnel_id is None:
            raise ValueError("Invalid value for `tunnel_id`, must not be `None`")  # noqa: E501

        self._tunnel_id = tunnel_id
