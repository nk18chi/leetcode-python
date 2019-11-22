# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List
import unittest


def main():
    unittest.main()


class Test(unittest.TestCase):

    def test_maxSubArray(self):
        test_patterns = [
            ([2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -2, -2, 1, -3, 4, -1, 2, 1, -5, 4], 18),
            ([-2, -2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([-1, 2, -1, 1, 1, -2, 1, -3, 4, -1, 2, 1, -5, 4], 3),
            ([-2, -2, -1, -3, 0], 0),
            ([-2, -2, -1, -3, -1], -1)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = Solution()
                self.assertEqual(s.maxSubArray(arg), expected)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_int = max(nums)
        if max_int <= 0:
            return max_int

        sum = 0
        for n in nums:
            if n + sum <= 0:
                sum = 0
                continue

            sum += n
            if max_int < sum:
                max_int = sum

        return max_int


if __name__ == '__main__':
    main()
