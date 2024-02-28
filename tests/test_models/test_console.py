#!/usr/bin/python3

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.cmd = HBNBCommand()

    def test_instantiation(self):
        """Test instantiation of HBNBCommand"""
        self.assertIsInstance(self.cmd, HBNBCommand)

    # def test_quit(self):
    #     """Test quit command"""
    #     with self.assertRaises(SystemExit):
    #         self.cmd.do_quit(None)


if __name__ == '__main__':
    unittest.main()
