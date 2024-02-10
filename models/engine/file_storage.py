#!/usr/bin/python3
"""This module contains a class for the file storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        Serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            Serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(Serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                Serialized_objects = json.load(f)
            for key, value in Serialized_objects.items():
                class_name, obj_id = key.split('.')
                class_obj = eval(class_name)
                obj = class_obj(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
