#!/usr/bin/python3
"""Defines unittests for models/base_model.py

Unittests classes:
    TestBasemodel_instantiation
    TestBasemodel_methods
"""

from time import sleep
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBasemodel_instantiation(unittest.TestCase):
    """Test cases for the instantiation of the BaseModel class"""

    def test_instance_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_unique_id(self):
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_different_created_at(self):
        model_1 = BaseModel()
        sleep(0.005)
        model_2 = BaseModel()
        self.assertNotEqual(model_1.created_at, model_2.created_at)

    def test_different_updated_at(self):
        model_1 = BaseModel()
        sleep(0.005)
        model_2 = BaseModel()
        self.assertNotEqual(model_1.updated_at, model_2.updated_at)

    def test_string_representation(self):
        dt = datetime.now()
        dt_repr = repr(dt)  # printable str representation of datetime object
        model = BaseModel()
        model.created_at = model.updated_at = dt
        model.id = "12345"
        model.name = "My Model"
        model.number = 10
        str_rep = model.__str__()
        self.assertIn("[BaseModel] (12345)", str_rep)
        self.assertIn("'name': 'My Model'", str_rep)
        self.assertIn("'number': 10", str_rep)
        self.assertIn("'created_at': " + dt_repr, str_rep)
        self.assertIn("'updated_at': " + dt_repr, str_rep)

    def test_args_unused(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.items())

    def test_kwargs_instantiated(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        model = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, dt)
        self.assertEqual(model.updated_at, dt)

    def test_kwargs_instantiated_with_None(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs_and_args_instantiated(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        model = BaseModel("10", id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, dt)
        self.assertEqual(model.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Test cases for the save() method of BaseModel class"""

    def test_save_once(self):
        model = BaseModel()
        sleep(0.005)
        first_update = model.updated_at
        model.save()
        self.assertLess(first_update, model.updated_at)

    def test_save_twice(self):
        model = BaseModel()
        sleep(0.005)
        first_update = model.updated_at
        model.save()
        second_update = model.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.005)
        model.save()
        self.assertLess(second_update, model.updated_at)

    def test_save_with_args(self):
        """Test save() with an argument"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Test cases for the to_dict() method of BaseModel class"""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertEqual(dict, type(model.to_dict()))

    def test_to_dict_keys(self):
        """Tests to see if certain keys are present in the dictionary"""
        model = BaseModel()
        model.name = "My Model"
        model.number = 10
        dic_rep = model.to_dict()
        self.assertIn("name", dic_rep)
        self.assertIn("number", dic_rep)
        self.assertIn("id", dic_rep)
        self.assertIn("created_at", dic_rep)
        self.assertIn("updated_at", dic_rep)
        self.assertIn("__class__", dic_rep)

    def test_to_dict_attributes_str(self):
        """Tests to see if the values of created_at
        and updated_at are strings"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(str, type(model_dict["created_at"]))
        self.assertEqual(str, type(model_dict["updated_at"]))

    def test_to_dict_output(self):
        """Tests to see if dictionary output is correct"""
        dt = datetime.now()
        model = BaseModel()
        model.name = "My Model"
        model.number = 10
        model.id = "12345"
        model.created_at = model.updated_at = dt
        dict_out = {
            'id': '12345',
            'number': 10,
            'name': 'My Model',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(dict_out, model.to_dict())

    def test_to_dict_with_args(self):
        """Test to_dict() with an argument"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == "__main__":
    unittest.main()
