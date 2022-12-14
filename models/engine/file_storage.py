#!/usr/bin/python3
"""Defines a FileStorage class"""

import json
from models.base_model import BaseModel

class FileStorage:
    
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        '''returns the `__objects` dict'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file '''

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        #try:
        #    with open(FileStorage.__file_path, 'r') as file:
        #        dicts = json.load(file)
        #        FileStorage.__objects = dicts

        #except Exception:
        #    pass
        try:
            with open(self.__file_path, 'r') as f:
                file_store = json.load(f)
                for value in file_store.values():
                    self.new(eval(value['__class__'])(**value))

        except Exception as e:
            pass
