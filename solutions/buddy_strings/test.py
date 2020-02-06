import unittest
import solutions.buddy_strings.index as main


class Test(unittest.TestCase):

    def test_buddyStrings(self):
        test_patterns = [
            ("ba", "ab", True),
            ("ab", "ab", False),
            ("aa", "aa", True),
            ("aaaaaaabc", "aaaaaaacb", True),
            ("", "aa", False),
            ("abcaa", "abcbb", False)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.buddyStrings(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
