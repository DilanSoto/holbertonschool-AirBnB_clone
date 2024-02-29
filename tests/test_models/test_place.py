#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up method to start each test."""
        self.place1 = Place()
        self.place2 = Place(city_id="city_id_1", user_id="user_id_1",
                            name="Place 1", description="A nice place",
                            number_rooms=3, number_bathrooms=2, max_guest=4,
                            price_by_night=100, latitude=10.0, longitude=20.0,
                            amenity_ids=["amenity_id_1", "amenity_id_2"])

    def tearDown(self):
        """Tear down method to clean up any setup objects."""
        del self.place1
        del self.place2

    def test_instance_creation(self):
        """Test the instance and its attributes are correctly created."""
        self.assertTrue(isinstance(self.place1, Place))
        self.assertTrue(isinstance(self.place2, Place))

    def test_initial_values(self):
        """Test the initial values of attributes for both instances."""
        self.assertEqual(self.place1.city_id, "")
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])

        self.assertEqual(self.place2.city_id, "city_id_1")
        self.assertEqual(self.place2.user_id, "user_id_1")
        self.assertEqual(self.place2.name, "Place 1")
        self.assertEqual(self.place2.description, "A nice place")
        self.assertEqual(self.place2.number_rooms, 3)
        self.assertEqual(self.place2.number_bathrooms, 2)
        self.assertEqual(self.place2.max_guest, 4)
        self.assertEqual(self.place2.price_by_night, 100)
        self.assertEqual(self.place2.latitude, 10.0)
        self.assertEqual(self.place2.longitude, 20.0)
        self.assertListEqual(self.place2.amenity_ids,
                             ["amenity_id_1", "amenity_id_2"])

    def test_attribute_types(self):
        """Test the type of Place attributes."""
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.user_id, str)
        self.assertIsInstance(self.place1.name, str)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.longitude, float)
        self.assertIsInstance(self.place1.amenity_ids, list)

    def test_inheritance(self):
        """Test that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.place1), BaseModel))


if __name__ == "__main__":
    unittest.main()
