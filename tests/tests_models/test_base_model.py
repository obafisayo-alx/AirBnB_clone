import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self) -> None:
        """Set up a BaseModel object for testing."""
        self.base_model = BaseModel()

    def test_to_dict(self):
        # Test if returned dictionary contains all expected keys
        """Test the to_dict method of the BaseModel class."""
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

        # Test if '__class__' key contains correct class name
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

        # Test if 'created_at' and 'updated_at'
        # values are ISO formatted strings
        self.assertTrue(isinstance(obj_dict['created_at'], str))
        self.assertTrue(isinstance(obj_dict['updated_at'], str))

        # Test if 'created_at' and 'updated_at' strings are
        # valid datetime strings
        created_at = datetime.strptime(obj_dict['created_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(obj_dict['updated_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        self.assertTrue(isinstance(created_at, datetime))
        self.assertTrue(isinstance(updated_at, datetime))

        # Test if 'created_at' and 'updated_at' values are the same as
        # BaseModel object's attributes
        self.assertEqual(created_at, self.base_model.created_at)
        self.assertEqual(updated_at, self.base_model.updated_at)

    def test_save_method(self):
        """Test the save method of the BaseModel class"""
        # Test if Save method updates 'updated_at' attribute
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
