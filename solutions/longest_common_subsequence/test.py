import unittest
import longest_common_subsequence.index as main


class Test(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        test_patterns = [
            ("abaa", "ab", 2),
            ("abcde", "ace", 3),
            ("bsbininm", "jmjkbkjkv", 1),
            ("abc", "abc", 3),
            ("abc", "def", 0),
            ("bl", "yby", 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestCommonSubsequence(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
