import unittest
import importlib
f = importlib.import_module('solutions.231_power_of_two.index')


class Test(unittest.TestCase):

    def test_isPowerOfTwo(self):
        test_patterns = [
            (0, False),
            (1, True),
            (16, True),
            (32, True),
            (218, False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.isPowerOfTwo(arg), expected)


if __name__ == '__main__':
    unittest.main()
