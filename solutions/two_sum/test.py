# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import unittest

import solutions.two_sum.index as main


class Test(unittest.TestCase):

    def test_twoSum(self):
        test_patterns = [
            ([2, 7, 11, 15], 9, [0, 1]),
        ]

        for i, (arg, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.twoSum(arg, arg2), expected)


if __name__ == '__main__':
    unittest.main()
