#!/usr/bin/python3
"""User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that manages the data of users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
