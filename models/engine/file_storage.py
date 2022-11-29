#!/usr/bin/python3
'''FileStorage Module'''

from models.base_model import BaseModel
import json

class FileStorage:
    '''Serializes instances to a JSON file and
    deserializes JSON file to instances
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets in __objects the obj
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file
        '''
        dict_add = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                dict_add[key] = value.to_dict()
            json.dump(dict_add, f)
        #with open(FileStorage.__file_path, 'w') as file:
        #    file.write(json.dumps(FileStorage.__objects))

    def reload(self):
        '''deserializes the JSON file to __objects
        '''
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for key, value in file_store.items():
                    if '__class__' in value:
                        val = classes[value['__class__']](**value)
                        self.__objects[key] = val
        except:
            pass
