import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
import models


class TestBaseModel(unittest.TestCase):

    def test_init_no_args(self):
        """Test BaseModel initialization with no arguments."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs = {
            "id": "123",
            "created_at": "2021-06-29T15:27:48.789123",
            "updated_at": "2021-06-29T15:27:48.789123",
            "name": "TestName",
            "my_number": 42
        }
        model = BaseModel(**kwargs)
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                value = datetime.fromisoformat(value)
            self.assertEqual(getattr(model, key), value)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_save(self):
        """
        Test the save method updates `updated_at` and calls storage methods.
        """
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test conversion of model instance to dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_datetime_attributes(self):
        """Test that datetime attributes are instances of datetime."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_invalid_datetime_kwargs(self):
        """Test initialization with invalid datetime formats in kwargs."""
        kwargs = {
            "created_at": "invalid datetime",
            "updated_at": "another invalid datetime"
        }
        model = BaseModel(**kwargs)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
