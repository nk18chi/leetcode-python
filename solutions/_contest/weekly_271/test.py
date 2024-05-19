import unittest
import _contest.weekly_271.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_countPoints(self):
        test_patterns = [
            ("B0B6G0R6R0R6G9", 1),
            ("B0R0G0R9R0B0G0", 1),
            ("G4", 0),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countPoints(arg1), expected)

    def test_subArrayRanges(self):
        test_patterns = [
            ([1, 2, 3], 4),
            ([1, 3, 3], 4),
            ([4, -2, -3, 4, 1], 59),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.subArrayRanges(arg1), expected)

    def test_minimumRefill(self):
        test_patterns = [
            ([7, 7, 7, 7, 7, 7, 7], 8, 7, 5),
            ([1, 2, 4, 4, 5], 6, 5, 2),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumRefill(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
