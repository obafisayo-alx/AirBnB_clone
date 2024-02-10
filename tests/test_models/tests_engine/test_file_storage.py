import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self) -> None:
        """Set up test environment"""
        self.storage = FileStorage

    def tearDown(self) -> None:
        """Tear down test envirnoment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        # Initially, the storage should be empty
        self.assertEqual(self.storage.all(), {})

        # Add some objects to storge
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()

        # Check if all methods returns all objects
        objects = self.storage.all()
        self.assertIn("BaseModel." + obj1.id, objects)
        self.assertIn("BaseModel." + obj2.id, objects)
        self.assertEqual(len(objects), 2)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel." + obj.id, self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods."""
        obj = BaseModel()
        obj.name = "Test Object"
        obj.save()

        # Create a new storage instance and reload data
        new_storage = FileStorage
        new_storage.reload()

        # Retrieve the saved object
        objects = new_storage.all()
        self.assertIn("BaseModel." + obj.id, objects)
        self.assertEqual(objects["BaseModel." + obj.id].name, "Test Object")
