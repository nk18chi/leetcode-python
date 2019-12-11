import unittest
import importlib
f = importlib.import_module('solutions.859_buddy_strings.index')


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
                s = f.Solution()
                self.assertEqual(s.buddyStrings(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
