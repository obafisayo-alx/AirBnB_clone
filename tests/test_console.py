import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from console import HBNBCommand

# Add the directory containing console.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class TestHBNBCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        # self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        self.console.onecmd("all BaseModel")
        # self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        self.console.onecmd("update BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.console.emptyline()
        self.assertEqual("", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
