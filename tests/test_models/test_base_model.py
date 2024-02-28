#!/usr/bin/python3
import sys
import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from datetime import datetime, timedelta
import os
sys.path.insert(0, os.path.abspath(os.path.join
                                   (os.path.dirname(__file__), '../../')))


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel class."""
    def test_init_no_args(self):
        """Test initialization without arguments."""
        model = BaseModel()
        time_diff = model.updated_at - model.created_at
        self.assertLess(abs(time_diff.total_seconds()), 0.1)
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs = {
            "id": "123",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        model = BaseModel(**kwargs)
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                self.assertEqual(getattr(model, key).isoformat(), value)
            else:
                self.assertEqual(getattr(model, key), value)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), expected_str)

    def test_save(self):
        """Test the save method updates `updated_at`."""
        model = BaseModel()
        first_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, first_updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)

    def test_datetime_attributes_conversion(self):
        """Test that `created_at` and `updated_at` are correctly
                converted from strings."""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        created_at_str = datetime.now().strftime(time_format)
        updated_at_str = (datetime.now() +
                          timedelta(days=1)).strftime(time_format)
        model = BaseModel(created_at=created_at_str, updated_at=updated_at_str)
        self.assertEqual(model.created_at.isoformat(), created_at_str)
        self.assertEqual(model.updated_at.isoformat(), updated_at_str)

    def test_save_and_reload(self):
        """Test saving to FileStorage and reloading."""
        model = BaseModel()
        model_id = model.id
        model.save()
        storage.reload()
        self.assertIn(f"BaseModel.{model_id}", storage.all())

    def test_unique_id_for_each_instance(self):
        """Test that each BaseModel instance has a unique id."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_invalid_kwargs(self):
        """Test initialization with invalid kwargs does not set
                unexpected attributes."""
        model = BaseModel(unsupported_attribute="test")
        self.assertFalse(hasattr(model, "unsupported_attribute"))

    def test_overwriting_attributes_with_kwargs(self):
        """Test overwriting default attributes with kwargs during
                initialization."""
        custom_id = "12345"
        custom_created_at = datetime.now() - timedelta(days=1)
        custom_updated_at = datetime.now()
        model = BaseModel(id=custom_id,
                          created_at=custom_created_at.isoformat(),
                          updated_at=custom_updated_at.isoformat())
        self.assertEqual(model.id, custom_id)
        self.assertEqual(model.created_at, custom_created_at)
        self.assertEqual(model.updated_at, custom_updated_at)

    def test_storage_new_called_on_save(self):
        """Test if `storage.new` is called when `save` is called."""
        model = BaseModel()
        model.save()
        self.assertIn(f"BaseModel.{model.id}", storage.all())

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created during the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
