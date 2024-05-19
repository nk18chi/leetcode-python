import unittest

import longest_palindrome.index as main


class Test(unittest.TestCase):
    def test_longestPalindrome(self):
        test_patterns = [
            ("abccccdd", 7),
            ("abbb", 3),
            ("bbb", 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestPalindrome(arg), expected)


if __name__ == "__main__":
    unittest.main()
