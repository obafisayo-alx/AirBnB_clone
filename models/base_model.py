#!/usr/bin/python3
"""This module contains the base class `BaseModel`"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel of the airbnb project"""
    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel.
        
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.
                                strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns a simple string representation of the instance created"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Saves the instance by updating the `updated_at` time-stamp"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """To convert the attributes of the object into a dictionary format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
