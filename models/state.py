#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state with a name"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State instance."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
