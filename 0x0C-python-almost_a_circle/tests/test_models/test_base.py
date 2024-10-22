#!/usr/bin/python3
"""test file for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing cass"""

    def setUp(self):
        Base.reset_nb_objects()

    def test_1_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_2_with_id(self):
        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    def test_3_mixed_id(self):
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 12)

if __name__ == "__main__":
    unittest.main()
