import unittest
import importlib
f = importlib.import_module('solutions.9_palindrome_number.index')


class Test(unittest.TestCase):
    def test_isPalindrome(self):
        test_patterns = [
            (112211, True),
            (121, True),
            (10, False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.isPalindrome(arg), expected)


if __name__ == '__main__':
    unittest.main()
