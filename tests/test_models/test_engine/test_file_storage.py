#!/usr/bin/env python3
"""Tests for file_storage.py"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class Test_FileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""
    model = BaseModel()

    def test_is_subclass(self):
        """Tests if FileStorage is a subclass of object"""
        self.assertTrue(issubclass(FileStorage, object))

    def test_is_instance(self):
        """Tests if an object is an instance of FileStorage"""
        file_1 = FileStorage()
        self.assertIsInstance(file_1, FileStorage)

    def New_reload(self):
        """ testing the reload """
        storage._FileStorage__file_path = "file.json"
        storage.reload()

    def test_Has_Attributes(self):
        """Testing the filestorage attributes """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_new(self):
        """tests if the method is able to save an obj to
        __objects dictionary with the format <classname>.id"""
        self.assertIn("{}.{}".format("BaseModel", Test_FileStorage.model.id),
                      storage._FileStorage__objects)
