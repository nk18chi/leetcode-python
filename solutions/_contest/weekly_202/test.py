import unittest
import solutions._contest.weekly_202.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_threeConsecutiveOdds(self):
        test_patterns = [
            ([2, 6, 4, 1], False),
            ([1, 2, 34, 3, 4, 5, 7, 23, 12], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.threeConsecutiveOdds(arg), expected)

    def test_minOperations(self):
        test_patterns = [
            (3, 2),
            (6, 9),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minOperations(arg), expected)

    def test_maxDistance(self):
        test_patterns = [
            ([1, 2, 3, 4, 7], 3, 3),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxDistance(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
