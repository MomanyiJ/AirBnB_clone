#!/usr/bin/python3
"""Unittest for FileStorage class
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests the methods in the FileStorage Class
    """

    def test_all_method(self):
        """Tests if the all() method returns object dictionaries correctly
        """

        all_objs = storage.all()
        self.assertEqual({}, all_objs)



