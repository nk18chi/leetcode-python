import unittest
import solutions.count_square_submatrices_with_all_ones.index as main


class Test(unittest.TestCase):
    def test_countSquares(self):
        test_patterns = [
            ([[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1], [1, 1, 0]], 8),
            ([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 15),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countSquares(arg), expected)


if __name__ == '__main__':
    unittest.main()
