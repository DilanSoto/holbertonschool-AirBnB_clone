#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity with a name"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
