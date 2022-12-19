#!/usr/bin/python3
"""Defines a place class"""

from models.base_model import BaseModel

class State(BaseModel):
    """Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = 0.0
    longitude =  0.0
    amenity_ids = ""

