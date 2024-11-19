#!/usr/bin/python3
"""test file fpr rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test rectangle methpds"""
    def test_1_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 12)

    def test_2_TypeError(self):
        with self.assertRaises(TypeError):
            Rectangle("12", 2)
        with self.assertRaises(TypeError):
            Rectangle(12, "2")
        with self.assertRaises(TypeError):
            Rectangle(12.2, 4)
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 2)
        with self.assertRaises(TypeError):
            Rectangle(12)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3', 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')

    def test_3_ValueError(self):
        with self.assertRaises(ValueError):
            Rectangle(-13, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_4_area(self):
        r1 = Rectangle(2, 10)
        r3 = Rectangle(2, 2, 0, 0, 12)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r3.area(), 4)
