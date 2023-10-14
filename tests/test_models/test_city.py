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
