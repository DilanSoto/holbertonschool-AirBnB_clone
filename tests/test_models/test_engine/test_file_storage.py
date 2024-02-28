#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down after tests."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all returns the __objects dict."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test that new adds an object correctly to __objects."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save correctly serializes __objects to the JSON file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{obj.id}", data)

    def test_reload(self):
        """Test that reload correctly deserializes the JSON
                file to __objects."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_all_type(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_key_format(self):
        """
        Test that new adds an object with correct key format to __objects.
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_file_exists(self):
        """Test that save creates a file."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_save_correctly_serializes(self):
        """
        Test that save correctly serializes a BaseModel instance to the JSON
        file.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['__class__'], 'BaseModel')

    def test_reload_deserializes(self):
        """
        Test that reload correctly deserializes the JSON file to __objects.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
