# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import unittest
import importlib
f = importlib.import_module('solutions.1_two_sum.index')


class Test(unittest.TestCase):

    def test_twoSum(self):
        test_patterns = [
            ("[2, 7, 11, 15]", 9, [0, 1]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.twoSum(arg), expected)


if __name__ == '__main__':
    unittest.main()
