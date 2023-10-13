#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    The FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Function returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        dict_obj = {}
        for key, obj in self.__objects.items():
            dict_obj[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing).
        If the file doesn't exist, no exception should be raised.

        In this code, globals().get(class_name) looks up the class based on
        its name as a string, and if it exists, it creates an instance
        of that class with the provided data.
        """
        try:
            with open(self.__file_path, 'r') as f:
                file_contents = f.read()
                if file_contents:
                    obj_dict = json.loads(file_contents)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        model_class = globals().get(class_name)
                        if model_class:
                            obj = model_class(**value)
                            self.__objects[key] = obj
        except FileNotFoundError:
            pass
