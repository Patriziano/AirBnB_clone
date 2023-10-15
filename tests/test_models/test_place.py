#!/usr/bin/env python3
"""This tests for place.py file"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Class for Place class test"""

    def test_is_subclass(self):
        """Tests if Place is a subclass of BaseModel"""
        place_1 = Place()
        self.assertTrue(issubclass(type(place_1), BaseModel))

    def test_is_instance(self):
        """Tests if object is an instance of Place"""
        place_1 = Place()
        self.assertIsInstance(place_1, Place)

    def test_name_is_string(self):
        """Tests if attribute name is a string"""
        place_1 = Place()
        place_1.name = "John"
        self.assertEqual(type(place_1.name), str)

    def test_to_dict_attr(self):
        """Tests attributes of an object when changed to dictionary"""
        place_1 = Place()
        new_dict = place_1.to_dict()
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         place_1.created_at.isoformat())
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["updated_at"],
                         place_1.updated_at.isoformat())
        self.assertEqual(new_dict["__class__"], "Place")
