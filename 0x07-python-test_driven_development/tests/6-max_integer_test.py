import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()