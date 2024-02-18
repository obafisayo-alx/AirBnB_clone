#!/usr/bin/python3
"""A Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a review representation

    Atrributes:
        place_id (str): Place
        text (str): text of the review
        user_id (str): User id
    """

    place_id = ""
    user_id = ""
    text = ""
