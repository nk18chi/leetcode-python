# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import unittest
import importlib
f = importlib.import_module('solutions.1_two_sum.index')


class Test(unittest.TestCase):

    def test_intToRoman(self):
        test_patterns = [
            (3, "III"),
            # (4, "IV"),
            # (9, "IX"),
            # (58, "LVIII"),
            # (1994, "MCMXCIV"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.intToRoman(arg), expected)


if __name__ == '__main__':
    unittest.main()
