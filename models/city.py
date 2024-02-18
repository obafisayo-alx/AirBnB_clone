#!/usr/bin/python3
"""A City class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city.

    Attributes:
        state_id (str): State id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
