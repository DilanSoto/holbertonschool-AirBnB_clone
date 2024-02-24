import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel class."""
    def test_init_no_args(self):
        """Test initialization without arguments."""
        model = BaseModel()
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


if __name__ == '__main__':
    unittest.main()
