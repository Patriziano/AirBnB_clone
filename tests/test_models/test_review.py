#!/usr/bin/env python3
"""Contains tests for review.py"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """class for the tests on Review class"""

    def test_is_subclass(self):
        """Tests if Review is a subclass of BaseModel"""
        review_1 = Review()
        self.assertTrue(issubclass(type(review_1), BaseModel))

    def test_is_instance(self):
        """Tests if an object is an instance of Review"""
        review_1 = Review()
        self.assertTrue(isinstance(review_1, Review))

    def test_attrs_type(self):
        """Tests the attributes data type"""
        review_1 = Review()
        review_1.user_id = "the user id"
        review_1.place_id = "the place id"
        review_1.text = "the message"
        self.assertEqual(type(review_1.user_id), str)
        self.assertEqual(type(review_1.place_id), str)
        self.assertEqual(type(review_1.text), str)
