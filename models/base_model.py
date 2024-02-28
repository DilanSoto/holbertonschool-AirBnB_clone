#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        valid_attrs = ["id", "created_at", "updated_at", "name", "my_number"]

        if kwargs:
            for key, value in kwargs.items():
                if key in valid_attrs:
                    if key in ["created_at", "updated_at"]:
                        try:
                            value = datetime.fromisoformat(value)
                        except ValueError:
                            continue
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        # Import here to avoid circular import issues
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        result_dict = dict(self.__dict__)
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict
