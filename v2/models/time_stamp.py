from __future__ import absolute_import
from datetime import date, datetime

from typing import List, Dict

from v2.models.base_model_ import Model
from v2 import util


class TimeStamp(Model):

    def __init__(self, nano_seconds: int, seconds: int):  
        """TimeStamp - a model 

        :param nano_seconds: The nano_seconds of this TimeStamp.  
        :type nano_seconds: int
        :param seconds: The seconds of this TimeStamp.
        :type seconds: int
        """
        
        self._nano_seconds = nano_seconds
        self._seconds = seconds

    # Esta função pega um self e tranforma em dicionário
    # Pega o objeto e retorna ele em formato json
    def json(self):
        return {
            "nano_seconds": self.nano_seconds,
            "seconds": self.seconds
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TimeStamp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimeStamp of this TimeStamp.  # noqa: E501
        :rtype: TimeStamp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nano_seconds(self) -> int:
        """Gets the nano_seconds of this TimeStamp.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC.  # noqa: E501

        :return: The nano_seconds of this TimeStamp.
        :rtype: int
        """
        return self._nano_seconds

    @nano_seconds.setter
    def nano_seconds(self, nano_seconds: int):
        """Sets the nano_seconds of this TimeStamp.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC.  # noqa: E501

        :param nano_seconds: The nano_seconds of this TimeStamp.
        :type nano_seconds: int
        """
        if nano_seconds == "":
            raise ValueError("Invalid value for `nano_seconds`, must not be `None`")  # noqa: E501

        self._nano_seconds = nano_seconds

    @property
    def seconds(self) -> int:
        """Gets the seconds of this TimeStamp.

        The seconds part of the time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC.  # noqa: E501

        :return: The seconds of this TimeStamp.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        """Sets the seconds of this TimeStamp.

        The seconds part of the time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC.  # noqa: E501

        :param seconds: The seconds of this TimeStamp.
        :type seconds: int
        """
        if seconds  == "":
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds
