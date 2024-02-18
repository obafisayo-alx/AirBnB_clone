#!/usr/bin/python3
"""Amenity class module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Representation of an amenity

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
