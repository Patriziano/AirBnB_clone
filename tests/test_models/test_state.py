#!/usr/bin/env python3
"""This tests for state.py file"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Class for State class test"""

    def test_is_subclass(self):
        """Tests if State is a subclass of BaseModel"""
        state_1 = State()
        self.assertTrue(issubclass(type(state_1), BaseModel))

    def test_is_instance(self):
        """Tests if object is an instance of State"""
        state_1 = State()
        self.assertIsInstance(state_1, State)

    def test_name_is_string(self):
        """Tests if attribute name is a string"""
        state_1 = State()
        state_1.name = "John"
        self.assertEqual(type(state_1.name), str)

    def test_to_dict_attr(self):
        """Tests attributes of an object when changed to dictionary"""
        state_1 = State()
        new_dict = state_1.to_dict()
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         state_1.created_at.isoformat())
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["updated_at"],
                         state_1.updated_at.isoformat())
        self.assertEqual(new_dict["__class__"], "State")

    def test_has_attr(self):
        """Tests if state has the required attributes"""
        state_1 = State()
        self.assertTrue(hasattr(state_1, "name"))

    def test_attr_type(self):
        """Tests attributes types"""
        state_1 = State()
        self.assertIsInstance(state_1.name, str)

    def test_attr_value(self):
        """Tests attributes value"""
        state_1 = State()
        self.assertEqual(getattr(state_1, "name"), "")
