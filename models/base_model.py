#!/usr/bin/python3

# & This module defines a base class for all models in our hbnb clone

# & Import necessary modules

import uuid

from datetime import datetime

import models





class BaseModel:

    """A base class for all hbnb models

    that defines all common attributes/methods

    for other classes"""

    # & Initialize a new BaseModel



    def __init__(self, *args, **kwargs):
        """
        If kwargs are provided, set them as attributes.
        Otherwise, set default attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                # & Ignore __class__ attribute
                if key == "__class__":
                    pass
                # & Convert string datetime to datetime object
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                # & Set other attributes
                else:
                    setattr(self, key, value)
        else:
            # & Set default attributes
            self.id = str(uuid.uuid4())  # & Create a unique UUID
            self.created_at = datetime.now()  # & Set the creation time to now
            self.updated_at = datetime.now()  # & Set the update time to now
            models.storage.new(self)  # & Add the new instance to storage


    # & Return a string representation of the BaseModel instance

    def __str__(self):

        return F"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"



    # & Update updated_at with the current datetime and save to storage

    def save(self):

        self.updated_at = datetime.now()

        models.storage.new(self)

        models.storage.save()



    # & Return a dictionary representation of the BaseModel instance

    def to_dict(self):

        """

        Convert datetime objects to ISO format strings.

        """

        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__

        # & Convert datetime objects to ISO format strings

        new_dict["created_at"] = self.created_at.isoformat()

        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
