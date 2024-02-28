#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file (default: "file.json").
        __objects (dict): Stores all objects by their key (<class name>.<id>).
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file exists)."""
        try:
            pass
        except:
            pass

    def save(self):
       """Serializes __objects to the JSON file (path: __file_path)."""
       temp_dict = {}
       for key, obj in self.__objects.items():
           temp_dict[key] = obj.to_dict()
       with open(self.__file_path, "w") as f:
           json.dump(temp_dict, f)
