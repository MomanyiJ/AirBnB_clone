#!/usr/bin/python3
"""Contains the file storage class
"""

import json


class FileStorage:
    """Class to serialise and deserialise instances to and fro a JSON file

    Attributes:
        file_path (str): path to the JSON file
        objects (dict): stores all object by <class name>.id
    """

    __file_path = "airbnb_objects_file.json"
    __objects = {}

    def all(self):
        """Returns the objects dictionary
        """

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to the objects dictionary
        """

        key = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialises __objects to the JSON file
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserialises the JSON file to __objects
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
