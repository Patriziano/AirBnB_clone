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
