import unittest
import _contest.weekly_199.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_restoreString(self):
        test_patterns = [
            ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.restoreString(arg1, arg2), expected)

    def test_minFlips(self):
        test_patterns = [
            ("10111", 3),
            ("00000", 0),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minFlips(arg1), expected)

    def test_countPairs(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7], 3, 2),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg1)
                self.assertEqual(s.countPairs(tree, arg2), expected)


if __name__ == "__main__":
    unittest.main()
