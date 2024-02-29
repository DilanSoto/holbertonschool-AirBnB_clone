#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity class."""

    def setUp(self):
        """Set up for the tests."""
        self.amenity = Amenity()
        self.amenity.name = "Pool"

    def test_instantiation(self):
        """Test instantiation of Amenity object."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attribute(self):
        """Test that the name attribute is present and correctly set."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "Pool")

    def test_inheritance(self):
        """Test if Amenity correctly inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes_types(self):
        """Test the type of Amenity attributes."""
        self.assertIsInstance(self.amenity.name, str)

    def test_base_model_attributes(self):
        """Test if Amenity has BaseModel attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
