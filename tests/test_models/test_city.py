#!/usr/bin/env python3
"""Contains tests for city.py"""
import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """Class for tests on City class"""

    def test_is_subclass(self):
        """Tests if City is a subclass of BaseModel"""
        city_1 = City()
        self.assertTrue(issubclass(type(city_1), BaseModel))

    def test_is_instance(self):
        """Tests if an object is a subclass of City"""
        city_1 = City()
        self.assertTrue(isinstance(city_1, City))

    def test_attrs_type(self):
        """Tests the type of the attributes"""
        city_1 = City()
        city_1.state_id = "our_id"
        city_1.name = "Abuja"
        self.assertEqual(type(city_1.state_id), str)
        self.assertEqual(type(city_1.name), str)

    def test_to_dict_attrs(self):
        """Tests attributes when object is changed to dictionary"""
        city_1 = City()
        new_dict = city_1.to_dict()
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(new_dict["created_at"], city_1.created_at.isoformat())
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["updated_at"], city_1.updated_at.isoformat())
        self.assertEqual(new_dict["__class__"], "City")

    def test_has_attr(self):
        """Tests attributes for City class"""
        city_1 = City()
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertTrue(hasattr(city_1, "name"))

    def test_attr_type(self):
        """Tests attributes type"""
        city_1 = City()
        self.assertIsInstance(city_1.state_id, str)
        self.assertIsInstance(city_1.name, str)
