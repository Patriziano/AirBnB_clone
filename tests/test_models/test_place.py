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

    def testHasAttributes(self):
        """verify if attributes exist"""
        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'city_id'))
        self.assertTrue(hasattr(place_1, 'user_id'))
        self.assertTrue(hasattr(place_1, 'name'))
        self.assertTrue(hasattr(place_1, 'description'))
        self.assertTrue(hasattr(place_1, 'number_rooms'))
        self.assertTrue(hasattr(place_1, 'number_bathrooms'))
        self.assertTrue(hasattr(place_1, 'max_guest'))
        self.assertTrue(hasattr(place_1, 'price_by_night'))
        self.assertTrue(hasattr(place_1, 'latitude'))
        self.assertTrue(hasattr(place_1, 'longitude'))
        self.assertTrue(hasattr(place_1, 'amenity_ids'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        place_1 = Place()
        self.assertIsInstance(place_1.city_id, str)
        self.assertIsInstance(place_1.user_id, str)
        self.assertIsInstance(place_1.name, str)
        self.assertIsInstance(place_1.description, str)
        self.assertIsInstance(place_1.number_rooms, int)
        self.assertIsInstance(place_1.number_bathrooms, int)
        self.assertIsInstance(place_1.max_guest, int)
        self.assertIsInstance(place_1.price_by_night, int)
        self.assertIsInstance(place_1.latitude, float)
        self.assertIsInstance(place_1.longitude, float)
        self.assertIsInstance(place_1.amenity_ids, list)

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
