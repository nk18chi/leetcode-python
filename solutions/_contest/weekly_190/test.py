import unittest
import solutions._contest.weekly_190.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_maxVowels(self):
        test_patterns = [
            ("leetcode", 3, 2),
            ("tryhard", 4, 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxVowels(arg1, arg2), expected)

    def test_pseudoPalindromicPaths(self):
        test_patterns = [
            ([2, 3, 1, 3, 1, 0, 1], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.pseudoPalindromicPaths(tree), expected)

    def test_maxDotProduct(self):
        test_patterns = [
            ([-1, -1], [1, 1], -1),
            ([2, 1, -2, 5], [3, 0, -6], 18)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxDotProduct(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
