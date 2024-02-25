import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up method to start each test."""
        self.user1 = User()
        self.user2 = User(email="test@example.com", password="password",
                          first_name="John", last_name="Doe")

    def tearDown(self):
        """Tear down method to clean up any setup objects."""
        del self.user1
        del self.user2

    def test_instance_creation(self):
        """Test the instance and its attributes are correctly created."""
        self.assertTrue(isinstance(self.user1, User))
        self.assertTrue(isinstance(self.user2, User))

    def test_initial_values(self):
        """Test the initial values of attributes for both instances."""
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

        self.assertEqual(self.user2.email, "test@example.com")
        self.assertEqual(self.user2.password, "password")
        self.assertEqual(self.user2.first_name, "John")
        self.assertEqual(self.user2.last_name, "Doe")

    def test_attribute_types(self):
        """Test the type of User attributes."""
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)

    def test_inheritance(self):
        """Test that User is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.user1), BaseModel))


if __name__ == "__main__":
    unittest.main()
