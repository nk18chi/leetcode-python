import unittest
import _contest.weekly_200.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_countGoodTriplets(self):
        test_patterns = [
            ([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countGoodTriplets(arg1, arg2, arg3, arg4), expected)

    def test_getWinner(self):
        test_patterns = [
            ([1, 25, 35, 42, 68, 70], 1, 25),
            ([2, 1, 3, 5, 4, 6, 7], 2, 5),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getWinner(arg1, arg2), expected)

    def test_minSwaps(self):
        test_patterns = [
            ([[0, 0, 1], [1, 1, 0], [1, 0, 0]], 3),
            ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]], -1),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSwaps(arg1), expected)


if __name__ == "__main__":
    unittest.main()
