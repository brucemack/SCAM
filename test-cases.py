import unittest
import math
from utils import *

class TestCases(unittest.TestCase):

    def test_rotate(self):
        c = round_coords(rotate((1, 0), 90))
        self.assertEqual(0.0, c[0])
        self.assertEqual(1.0, c[1])

    def test_mill_0(self):
        bl = (0, 0)
        tr = (10, 2.5)
        tool_mm = 1.0
        result = mill_calc_h(bl, tr, tool_mm)
        # Three passes will be needed
        self.assertEqual(6, len(result))
        print(result)

    def test_mill_1(self):
        bl = (0, 0)
        tr = (10, 1)
        tool_mm = 1.0
        result = mill_calc_h(bl, tr, tool_mm)
        self.assertEqual(2, len(result))
        print(result)

if __name__ == '__main__':
    unittest.main()