import unittest
import importlib
f = importlib.import_module('solutions.299_bulls_and_cows.index')


class Test(unittest.TestCase):
    def test_getHint(self):
        test_patterns = [
            ("1123", "0111", "1A1B"),
            ("1807", "7810", "1A3B"),
            ("1122", "1222", "3A0B"),
            ("1807", "2222", "0A0B"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.getHint(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
