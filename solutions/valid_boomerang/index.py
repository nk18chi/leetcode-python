# 1037. Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/

import unittest
from typing import List


def main():
    unittest.main()


class Test(unittest.TestCase):
    def test_isBoomerang(self):
        test_patterns = [
            ([[0, 1], [2, 10], [5, 5]], True),
            ([[0, 4], [2, 10], [5, 1]], True),
            ([[1, 1], [5, 5], [2, 10]], True),
            ([[1, 1], [2, 3], [3, 2]], True),
            ([[1, 1], [3, 3], [2, 2]], False),
            ([[2, 1], [3, 1], [1, 4]], True),
            ([[2, 2], [2, 2], [2, 2]], False),
            ([[2, 1], [2, 1], [2, 3]], False),
            ([[1, 1], [2, 4], [3, 6]], True),
            ([[1, 2], [2, 3], [2, 0]], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isBoomerang(arg), expected)


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x = points[0][0] - points[1][0]
        y = points[0][1] - points[1][1]

        x2 = points[1][0] - points[2][0]
        y2 = points[1][1] - points[2][1]

        if x == y == x2 == y2 == 0:
            return False
        if x * y2 == y * x2:
            return False

        return True


if __name__ == "__main__":
    main()
