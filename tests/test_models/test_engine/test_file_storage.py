#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the test case environment."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down the test case environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the dictionary of objects correctly."""
        self.assertEqual(len(self.storage.all()), 0)
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        """Test adding a new object to storage."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test object serialization to a file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test object deserialization from a file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_reload_no_file(self):
        """Test reloading without a pre-existing file."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()


if __name__ == '__main__':
    unittest.main()
