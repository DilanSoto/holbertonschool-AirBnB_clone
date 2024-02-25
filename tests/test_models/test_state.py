import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up method to start each test."""
        self.state_instance = State()
        self.state_instance.name = "California"

    def tearDown(self):
        """Tear down method to clean up any setup objects."""
        del self.state_instance

    def test_instance_creation(self):
        """Test the instance and its attributes are correctly created."""
        self.assertTrue(isinstance(self.state_instance, State))

    def test_attributes_existence(self):
        """Test that the instance has all the expected attributes."""
        self.assertTrue(hasattr(self.state_instance, "name"))
        self.assertTrue(hasattr(self.state_instance, "id"))
        self.assertTrue(hasattr(self.state_instance, "created_at"))
        self.assertTrue(hasattr(self.state_instance, "updated_at"))

    def test_attribute_type(self):
        """Test the type of State attributes."""
        self.assertIsInstance(self.state_instance.name, str)

    def test_inheritance(self):
        """Test that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.state_instance), BaseModel))


if __name__ == "__main__":
    unittest.main()
