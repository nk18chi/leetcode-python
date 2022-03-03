import unittest
import solutions.longest_palindromic_substring.index as main


class Test(unittest.TestCase):
    def test_longestPalindrome(self):
        test_patterns = [
            ("babad", "bab"),
            ("abba", "abba"),
            ("aacabdkacaa", "aca"),
            ("cbbd", "bb"),
            ("bb", "bb"),


        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestPalindrome(arg1), expected)


if __name__ == '__main__':
    unittest.main()
