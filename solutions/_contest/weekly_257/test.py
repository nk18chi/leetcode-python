import unittest
import _contest.weekly_257.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_countQuadruplets(self):
        test_patterns = [
            ([1, 2, 3, 6], 1),
            ([3, 3, 6, 4, 5], 0),
            ([1, 1, 1, 3, 5], 4),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countQuadruplets(arg), expected)

    def test_numberOfWeakCharacters(self):
        test_patterns = [
            (
                [
                    [1, 1],
                    [2, 2],
                    [3, 4],
                    [10, 2],
                    [2, 2],
                    [9, 1],
                    [8, 1],
                    [7, 1],
                    [12, 3],
                ],
                7,
            ),
            ([[5, 5], [6, 3], [3, 6]], 0),
            ([[2, 2], [3, 3]], 1),
            ([[1, 5], [10, 4], [4, 3]], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numberOfWeakCharacters(arg), expected)


if __name__ == "__main__":
    unittest.main()
