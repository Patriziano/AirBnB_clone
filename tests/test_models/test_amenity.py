#!/usr/bin/env python3
"""Contains tests for amenity.py"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Tests for the Amenity class"""

    amenity_1 = Amenity()

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

    def test_to_dict_attr_type(self):
        """Test the type of each attribute when object is changed to dict"""
        amenity_1 = Amenity()
        new_dict = amenity_1.to_dict()
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         amenity_1.updated_at.isoformat())
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["updated_at"],
                         amenity_1.updated_at.isoformat())
        self.assertEqual(new_dict["__class__"], "Amenity")

    def test_has_attr(self):
        """Tests attributes of Amenity class"""
        amenity_1 = Amenity()
        self.assertTrue(hasattr(amenity_1, "name"))

    def test_attr_type(self):
        """Tests attributes type"""
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)

    def test_attr_value(self):
        """Tests for attribute value"""
        self.assertEqual(getattr(Test_Amenity.amenity_1, "name"), "")
