import unittest
import importlib
f = importlib.import_module('solutions.119_pascals_triangle_2.index')


class Test(unittest.TestCase):
    def test_getRow(self):
        test_patterns = [
            (4, [1, 4, 6, 4, 1]),
            (5, [1, 5, 10, 10, 5, 1]),
            (6, [1, 6, 15, 20, 15, 6, 1]),
            (2, [1, 2, 1]),
            (0, [1]),
            (1, [1, 1]),
            (3, [1, 3, 3, 1]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.getRow(arg), expected)


if __name__ == '__main__':
    unittest.main()
