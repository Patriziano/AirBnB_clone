#!/usr/bin/env python3
"""Contains tests for amenity.py"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_is_subclass(self):
        """Tests if Amenity is a subclass of BaseModel"""
        amenity_1 = Amenity()
        self.assertTrue(issubclass(type(amenity_1), BaseModel))

    def test_is_instance(self):
        """Tests if an object is an instance of Amenity"""
        amenity_1 = Amenity()
        self.assertTrue(isinstance(amenity_1, Amenity))

    def test_attrs_type(self):
        """Tests if an attribute is of the required type"""
        amenity_1 = Amenity()
        amenity_1.name = "John Audu"
        self.assertEqual(type(amenity_1.name), str)
