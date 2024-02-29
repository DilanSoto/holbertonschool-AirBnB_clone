#!/usr/bin/python3
"""Unittest Module for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing the correct functioning of the User class."""

    def setUp(self):
        """Set up for the tests."""
        self.user = User()

    def tearDown(self):
        """Clean up after the tests."""
        del self.user

    def test_str_attr_initialization(self):
        """Test attributes initialization."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_attr_types(self):
        """Attribute type test."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_setting_attributes(self):
        """Test setting attribute values."""
        self.user.email = "user@example.com"
        self.user.password = "securepassword"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
