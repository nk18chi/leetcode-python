import unittest
import _contest.weekly_278.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_findFinalValue(self):
        test_patterns = [
            ([4, 7, 1, 16, 1, 2, 7, 13], 1, 8),
            ([8, 19, 2, 15, 3], 2, 4),
            ([2], 2, 4),
            ([5, 3, 6, 1, 12], 3, 24),
            ([2, 7, 9], 4, 4),
            ([8, 19, 4, 2, 15, 3], 2, 16),
            (
                [
                    161,
                    28,
                    640,
                    264,
                    81,
                    561,
                    320,
                    2,
                    61,
                    244,
                    183,
                    108,
                    773,
                    61,
                    976,
                    122,
                    988,
                    2,
                    370,
                    392,
                    488,
                    375,
                    349,
                    432,
                    713,
                    563,
                ],
                61,
                1952,
            ),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findFinalValue(arg1, arg2), expected)

    def test_maxScoreIndices(self):
        test_patterns = [
            ([0, 0, 1, 0], [2, 4]),
            ([0, 0, 0], [3]),
            ([1, 1], [0]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxScoreIndices(arg1), expected)

    def test_subStrHash(self):
        test_patterns = [
            ("leetcode", 7, 20, 2, 0, "ee"),
            ("fbxzaad", 31, 100, 3, 32, "fbx"),
        ]

        for i, (arg1, arg2, arg3, arg4, arg5, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.subStrHash(arg1, arg2, arg3, arg4, arg5), expected)


if __name__ == "__main__":
    unittest.main()
