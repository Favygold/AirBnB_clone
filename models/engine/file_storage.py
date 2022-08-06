#!/usr/bin/python3
"""Defines class Filestorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """Serialize instances to a JSON file and
       deserialize JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """"Set in __objects the obj with key <obj class name>.id

        Args:
            obj: object to be set
        """
        ocls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocls_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        objs = FileStorage.__objects
        obj_dict = {
            key: value.to_dict()
            for key, value in objs.items()
            }
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects
           only if the JSON file exists; otherwise, do nothing.
           If the file doesn’t exist, no exception is raised
        """
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
