import unittest
import _contest.weekly_258.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_reversePrefix(self):
        test_patterns = [
            ("abcdefd", "d", "dcbaefd"),
            ("xyxzxe", "z", "zxyxxe"),
            ("abcd", "z", "abcd"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reversePrefix(arg1, arg2), expected)

    def test_interchangeableRectangles(self):
        test_patterns = [
            ([[4, 8], [3, 6], [10, 20], [15, 30]], 6),
            ([[4, 5], [7, 8]], 0),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.interchangeableRectangles(arg1), expected)


if __name__ == "__main__":
    unittest.main()
