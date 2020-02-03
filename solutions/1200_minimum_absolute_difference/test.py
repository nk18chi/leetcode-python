import unittest
import importlib
f = importlib.import_module('solutions.1200_minimum_absolute_difference.index')


class Test(unittest.TestCase):
    def test_minimumAbsDifference(self):
        test_patterns = [
            ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.minimumAbsDifference(arg), expected)


if __name__ == '__main__':
    unittest.main()
