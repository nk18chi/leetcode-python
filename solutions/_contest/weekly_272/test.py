import unittest
import _contest.weekly_272.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_firstPalindrome(self):
        test_patterns = [
            (["xngla", "e", "itrn", "y", "s", "pfp", "rfd"], "e"),
            (["abc", "car", "ada", "racecar", "cool"], "ada"),
            (["notapalindrome", "racecar"], "racecar"),
            (["def", "ghi"], ""),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.firstPalindrome(arg1), expected)

    def test_addSpaces(self):
        test_patterns = [
            ("LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"),
            ("icodeinpython", [1, 5, 7, 9], "i code in py thon"),
            ("spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.addSpaces(arg1, arg2), expected)

    def test_getDescentPeriods(self):
        test_patterns = [
            ([3, 2, 1, 4], 7),
            ([3, 2, 1, 0, 4], 11),
            ([8, 6, 7, 7], 4),
            ([1], 1),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getDescentPeriods(arg1), expected)

    def test_kIncreasing(self):
        test_patterns = [
            ([12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3], 1, 12),
            ([12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3], 11, 5),
            ([4, 1, 5, 2, 6, 2], 3, 2),
            ([5, 4, 3, 2, 1], 1, 4),
            ([5, 2, 3], 1, 1),
            ([5, 6, 3], 1, 1),
            ([4, 1, 5, 2, 6, 2], 2, 0),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kIncreasing(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
