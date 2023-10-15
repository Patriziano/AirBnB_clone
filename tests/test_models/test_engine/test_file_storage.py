#!/usr/bin/env python3
"""Tests for file_storage.py"""
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_is_subclass(self):
        """Tests if FileStorage is a subclass of object"""
        self.assertTrue(issubclass(FileStorage, object))

    def test_is_instance(self):
        """Tests if an object is an instance of FileStorage"""
        file_1 = FileStorage()
        self.assertIsInstance(file_1, FileStorage)
