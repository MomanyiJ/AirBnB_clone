#!/usr/bin/python3
"""Unittest for BaseModel Class
"""

import unittest
from models.base_model import BaseModel
#BaseModel = __import__("base_model").BaseModel


class TestBaseModelClass(unittest.TestCase):
    """Tests the methods in the BaseModel class
    """

    def setUp(self):
        """Sets up for the tests
        """

        self.object1 = BaseModel()
        self.object2 = BaseModel()

    def test_unique_id(self):
        """Tests whether unique ids are generated
        """

        self.assertNotEqual(self.object1.id, self.object2.id)

    def test_object_representation(self):
        """Tests the object representation from __str__
        """

        self.assertEqual(self.object1.__str__(),
                         "[BaseModel] ({}) {}".format(self.object1.id,
                                                      self.object1.__dict__))

    def test_save_method(self):
        """Tests that save changes the value of 'updated_at'
        """

        now = self.object1.updated_at
        self.object1.save()
        self.assertNotEqual(now, self.object1.updated_at)

    def test_initialisation_with_kwargs(self):
        """Tests for proper initialisation with a dict representation
        """

        self.object1.name = "John"
        dict_repr = self.object1.to_dict()
        self.object3 = BaseModel(**dict_repr)

        self.assertEqual(self.object1.id, self.object3.id)
        self.assertEqual(self.object1.created_at, self.object3.created_at)
        self.assertEqual(self.object1.updated_at, self.object3.updated_at)
        self.assertEqual(self.object1.name, self.object3.name)


    def test_to_dict_method(self):
        """Tests that 'to_dict' has the correct output
        """

        self.object1.name = "John"
        self.object1.id = 9

        correct_output = {'id': 9,
                          'created_at': self.object1.created_at.isoformat(),
                          'updated_at': self.object1.updated_at.isoformat(),
                          'name': 'John',
                          '__class__': 'BaseModel'}

        self.assertEqual(correct_output, self.object1.to_dict())
        self.assertEqual(correct_output, self.object1.to_dict())


