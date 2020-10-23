import unittest
from utils import *


class TestCases(unittest.TestCase):

    def test_rotate(self):
        c = round_coords(rotate((1, 0), 90))
        self.assertEqual(0.0, c[0])
        self.assertEqual(1.0, c[1])


if __name__ == '__main__':
    unittest.main()