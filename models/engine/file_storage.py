import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            obj_id: obj.to_dict()
            for obj_id, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                class_name = obj_data['__class__']
                if class_name == 'BaseModel':
                    obj = BaseModel(**{k: v for k, v in
                                       obj_data.items() if k != '__class__'})
                self.__objects[obj_id] = obj
        except FileNotFoundError:
            pass
