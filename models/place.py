#!/usr/bin/pyton3
"""A Place class module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Rresent a place

       Attributes:
            city_id (str): City id.
            user_id (str): User id.
            name (str): Name of the place.
            description (str): Description of the place.
            number_rooms (int): Number of rooms of the place.
            number_bathrooms (int): Number of bathrooms of the place.
            max_guest (int): Maximum number of guests of the place.
            price_by_night (int): Price per night of the place.
            latitude (float): latitude of the place.
            longitude (float): longitude of the place.
            amenity_ids (list): list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
