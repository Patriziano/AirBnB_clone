#!/usr/bin/env python3
"""Test for the user.py file"""
import unittest
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """Class contains various tests for User class"""

    def test_is_subclass(self):
        """Tests if User is a subclass of BaseModel"""
        user_1 = User()
        self.assertTrue(issubclass(type(user_1), BaseModel))

    def test_is_instance(self):
        """Tests if an object is an instance of User"""
        user_1 = User()
        self.assertTrue(isinstance(user_1, User))

    def test_str(self):
        """Tests for data type of various attributes"""
        user_1 = User()
        user_1.email = "wedo@gmail.com"
        user_1.first_name = "John Audu"
        user_1.password = "theword"
        self.assertEqual(type(user_1.email), str)
        self.assertEqual(type(user_1.first_name), str)
        self.assertEqual(type(user_1.password), str)
