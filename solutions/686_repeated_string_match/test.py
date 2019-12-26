import unittest
import importlib
f = importlib.import_module('solutions.686_repeated_string_match.index')


class Test(unittest.TestCase):
    def test_repeatedStringMatch(self):
        test_patterns = [
            ("abc", "cabcabca", 4),
            ("abc", "aabcbabcc", -1),
            ("a", "aa", 2),
            ("abcd", "cdabcdab", 3),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.repeatedStringMatch(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
