#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place with attributes like city ID, user ID, name, etc."""
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

    def __init__(self, *args, **kwargs):
        """ Initializes Place instance """
        super().__init__(*args, **kwargs)
        if 'city_id' in kwargs:
            self.city_id = kwargs['city_id']
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
