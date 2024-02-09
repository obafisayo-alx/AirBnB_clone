#!/usr/bin/python3
"""This module contains the base class `BaseModel`"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel of the airbnb project"""
    def __init__(self) -> None:
        """Initializes the basemodel to assign the `id`,
            `created_at` and `updated_at` time-stamp
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns a simple string representation of the instance created"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Saves the instance by updating the `updated_at` time-stamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """To convert the attributes of the object into a dictionary format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
