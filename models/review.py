#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review with a place ID, user ID, and text"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
