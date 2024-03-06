# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ecgi import Ecgi  # noqa: F401,E501
from swagger_server import util


class SecondaryCellRemove(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ecgi: Ecgi=None):  # noqa: E501
        """SecondaryCellRemove - a model defined in Swagger

        :param ecgi: The ecgi of this SecondaryCellRemove.  # noqa: E501
        :type ecgi: Ecgi
        """
        self.swagger_types = {
            'ecgi': Ecgi
        }

        self.attribute_map = {
            'ecgi': 'ecgi'
        }
        self._ecgi = ecgi

    @classmethod
    def from_dict(cls, dikt) -> 'SecondaryCellRemove':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SecondaryCellRemove of this SecondaryCellRemove.  # noqa: E501
        :rtype: SecondaryCellRemove
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this SecondaryCellRemove.


        :return: The ecgi of this SecondaryCellRemove.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this SecondaryCellRemove.


        :param ecgi: The ecgi of this SecondaryCellRemove.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi