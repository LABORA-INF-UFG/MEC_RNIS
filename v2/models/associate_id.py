
from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from v2.models.base_model_ import Model
from v2.models.type import Type  # noqa: F401,E501
from v2 import util


class AssociateId(Model):

    def __init__(self, type: Type, value: str):  # noqa: E501
        """AssociateId - a model defined in Swagger

        :param type: The type of this AssociateId.  # noqa: E501
        :type type: Type
        :param value: The value of this AssociateId.  # noqa: E501
        :type value: str
        """
        
        self._type = type
        self._value = value

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "type": self.type,
            "value": self.value
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AssociateId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssociateId of this AssociateId.  # noqa: E501
        :rtype: AssociateId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> Type:
        """Gets the type of this AssociateId.


        :return: The type of this AssociateId.
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type: Type):
        """Sets the type of this AssociateId.


        :param type: The type of this AssociateId.
        :type type: Type
        """

        # Chamo o construtor da classe Type
        new_type = Type(**type)
        
        # Chamo o método json da classe Type para transformar os dados em json
        new_type = new_type.json()

        # Finalmente retorno o Json
        self._type = new_type

    @property
    def value(self) -> str:
        """Gets the value of this AssociateId.

        Value for the identifier.  # noqa: E501

        :return: The value of this AssociateId.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this AssociateId.

        Value for the identifier.  # noqa: E501

        :param value: The value of this AssociateId.
        :type value: str
        """

        self._value = value
