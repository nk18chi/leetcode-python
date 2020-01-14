import unittest
import importlib
f = importlib.import_module('solutions.977_squares_of_a_sorted_array.index')


class Test(unittest.TestCase):
    def test_sortedSquares(self):
        test_patterns = [
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.sortedSquares(arg), expected)


if __name__ == '__main__':
    unittest.main()
