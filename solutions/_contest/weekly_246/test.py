import unittest
import _contest.weekly_246.index as main
from _class.tree_node import TreeNode, createTreeNode


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


if __name__ == "__main__":
    unittest.main()
