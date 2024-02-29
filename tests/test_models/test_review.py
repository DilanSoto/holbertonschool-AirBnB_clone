#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def setUp(self):
        """Set up for the tests."""
        self.review1 = Review()
        self.review2 = Review(place_id="place_id_1", user_id="user_id_1",
                              text="Great place!")

    def test_init_without_args(self):
        """Test initialization without arguments."""
        self.assertIsInstance(self.review1, Review)
        self.assertIs(self.review1.place_id, "")
        self.assertIs(self.review1.user_id, "")
        self.assertIs(self.review1.text, "")

    def test_init_with_args(self):
        """Test initialization with arguments."""
        self.assertEqual(self.review2.place_id, "place_id_1")
        self.assertEqual(self.review2.user_id, "user_id_1")
        self.assertEqual(self.review2.text, "Great place!")

    def test_attributes_types(self):
        """Test the types of attributes."""
        self.assertIsInstance(self.review1.place_id, str)
        self.assertIsInstance(self.review1.user_id, str)
        self.assertIsInstance(self.review1.text, str)


if __name__ == "__main__":
    unittest.main()
