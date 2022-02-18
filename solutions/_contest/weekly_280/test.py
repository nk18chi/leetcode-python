import unittest
import solutions._contest.weekly_280.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_countOperations(self):
        test_patterns = [
            (2, 3, 3),
            (10, 10, 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countOperations(arg1, arg2), expected)

    def test_minimumOperations(self):
        test_patterns = [
            ([3, 1, 3, 2, 4, 3], 3),
            ([1, 2, 2, 2, 2], 2),
            ([2, 2, 2, 2, 2], 2),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumOperations(arg1), expected)

    def test_minimumRemoval(self):
        test_patterns = [
            ([4, 1, 6, 5], 4),
            ([2, 10, 3, 2], 7),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumRemoval(arg1), expected)


if __name__ == '__main__':
    unittest.main()
