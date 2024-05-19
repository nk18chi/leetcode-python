import unittest
import _contest.weekly_186.index as main


class Test(unittest.TestCase):
    def test_maxScore(self):
        test_patterns = [("00", 1), ("011101", 5), ("00111", 5), ("1111", 3)]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxScore(arg), expected)

    def test_maxScore2(self):
        test_patterns = [
            ([96, 90, 41, 82, 39, 74, 64, 50, 30], 8, 536),
            ([100, 40, 17, 9, 73, 75], 3, 248),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxScore2(arg1, arg2), expected)

    def test_findDiagonalOrder(self):
        test_patterns = [
            (
                [[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]],
                [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11],
            ),
            ([[1, 2, 3, 4, 5, 6]], [1, 2, 3, 4, 5, 6]),
            ([[6], [8], [6, 1, 6, 16]], [6, 8, 6, 1, 6, 16]),
            (
                [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
                [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
            ),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findDiagonalOrder(arg1), expected)


if __name__ == "__main__":
    unittest.main()
