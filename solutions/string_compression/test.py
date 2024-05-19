# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import unittest

import string_compression.index as main


class Test(unittest.TestCase):
    def test_compress(self):
        test_patterns = [
            # (["a", "b", "c"], 3),
            # (["a", "a", "a"], 2),
            # (["a", "a", "b", "b", "c", "c", "c"], 6),
            # (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4),
            (
                [
                    "a",
                    "a",
                    "a",
                    "a",
                    "a",
                    "a",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "b",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                    "c",
                ],
                8,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.compress(arg), expected)


if __name__ == "__main__":
    unittest.main()
