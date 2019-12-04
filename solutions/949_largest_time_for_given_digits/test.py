import unittest
import importlib
f = importlib.import_module(
    'solutions.949_largest_time_for_given_digits.index')


class Test(unittest.TestCase):

    def test_largestTimeFromDigits(self):
        test_patterns = [
            ([2, 0, 6, 6], "06:26"),
            ([1, 2, 3, 4], "23:41"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.largestTimeFromDigits(arg), expected)


if __name__ == '__main__':
    unittest.main()
