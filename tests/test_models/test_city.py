import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def test_city_instantiation(self):
        """Test instantiation of a City object."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        city.name = "San Francisco"
        city.state_id = "CA"
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")


if __name__ == '__main__':
    unittest.main()
