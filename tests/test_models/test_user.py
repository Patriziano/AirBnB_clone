#!/usr/bin/env python3
"""Test for the user.py file"""
import unittest
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """Class contains various tests for User class"""
    user_1 = User()

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
        user_1.last_name = "Patrick Ojewande"
        self.assertEqual(type(user_1.email), str)
        self.assertEqual(type(user_1.first_name), str)
        self.assertEqual(type(user_1.password), str)
        self.assertEqual(type(user_1.last_name), str)

    def test_has_attributes(self):
        """Tests to verify if attributes exists"""
        user_1 = User()
        self.assertTrue(hasattr(user_1, 'email'))
        self.assertTrue(hasattr(user_1, 'password'))
        self.assertTrue(hasattr(user_1, 'first_name'))
        self.assertTrue(hasattr(user_1, 'last_name'))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        attributes_to_check = [
            "email", "password", "first_name", "last_name"
        ]
        for attribute in attributes_to_check:
            default_val = ""
            self.assertEqual(getattr(Test_User.user_1, attribute), default_val)

    def test_to_dict_type(self):
        """To check the data type of each attribute when converted to dict"""
        user_1 = User()
        new_dict = user_1.to_dict()
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], user_1.created_at.isoformat())
        self.assertEqual(new_dict["updated_at"], user_1.updated_at.isoformat())
        self.assertEqual(type(new_dict["__class__"]), str)
        self.assertEqual(new_dict["__class__"], "User")
