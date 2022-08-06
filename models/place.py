#!/usr/bin/python3
"""Defines the Place class"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Defines a place

    Attributes:
        city_id (str): empty string. This will be the City.id
        user_id (str): empty string. This will be the User.id
        name (str): empty string.
        description (str): empty string.
        number_rooms (integer)
        number_bathrooms (integer)
        max_guest (integer)
        price_by_night (integer)
        latitude (float)
        longitude (float)
        amenity_ids (list of string): empty list.
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
