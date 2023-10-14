#!/usr/bin/env python3
"""The test file for base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def test_two_obj_ids(self):
        """Tests inequality of two objects ids"""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_is_instance(self):
        """Tests an instance of BaseModel"""
        model_1 = BaseModel()
        self.assertIsInstance(model_1, BaseModel)

    def test_not_equal_instances(self):
        """Tests inequality of two instances of BaseModel"""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertIsNot(model_1, model_2)

    def test_id_is_string(self):
        """Tests if the id is string"""
        model_1 = BaseModel()
        self.assertIsInstance(model_1.id, str)

    def test_created_at_eq_updated_at(self):
        """Test if created_at equals updated_at"""
        model_1 = BaseModel()
        self.assertAlmostEqual(model_1.created_at, model_1.updated_at)

    def test_BaseModel_is_object(self):
        """Test if the BaseModel originates from object class"""
        self.assertIsInstance(BaseModel, object)

    def test_updated_and_created_after_save(self):
        """the inequality of created_at and updated_at attributes
            after using the save(self) method
        """
        model_1 = BaseModel()
        model_1.save()
        self.assertNotEqual(model_1.created_at, model_1.updated_at)

    def test_updated_before_and_updated_after_save(self):
        """the inequality of upadted_at attributes
            before and after using the save(self) method
        """
        model_1 = BaseModel()
        before = model_1.updated_at
        model_1.save()
        after = model_1.updated_at
        self.assertNotEqual(before, after)

    def test_created_at_and_now(self):
        """Test if the created time is always less than the current time"""
        model_1 = BaseModel()
        self.assertLess(model_1.created_at, datetime.now())

    def test_uuid_len(self):
        """Test if id is a uuid4 string (len == 36)"""
        model_1 = BaseModel()
        self.assertEqual(len(model_1.id), 36)
