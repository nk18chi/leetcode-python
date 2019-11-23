# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import unittest
import importlib
f = importlib.import_module('solutions.12_integer_to_roman.index')


class Test(unittest.TestCase):

    def test_intToRoman(self):
        test_patterns = [
            (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.intToRoman(arg), expected)


if __name__ == '__main__':
    unittest.main()
