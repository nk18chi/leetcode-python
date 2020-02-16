import unittest
import solutions._contest.weekly_176.index as main


class Test(unittest.TestCase):
    def test_countNegatives(self):
        test_patterns = [
            ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
            ([[3, 2], [1, 0]], 0),
            ([[1, -1], [-1, -1]], 3),
            ([[-1]], 1)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countNegatives(arg), expected)

    def test_maxEvents(self):
        test_patterns = [
            ([[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]], 5),
            ([[1, 4], [1, 4], [1, 4], [1, 4], [1, 4]], 4),
            ([[26, 27], [24, 26], [1, 4], [1, 2], [3, 6], [2, 6], [9, 13], [6, 6], [25, 27], [22, 25], [20, 24], [8, 8], [27, 27], [30, 32]], 14),
            ([[1, 100000]], 1),
            ([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]], 4),
            ([[1, 2], [2, 3], [3, 4]], 3),
            ([[1, 2], [2, 3], [3, 4], [1, 2]], 4),
            ([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]], 7),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxEvents(arg), expected)

    def test_isPossible(self):
        test_patterns = [
            ([9, 3, 5], True),
            ([29799, 253, 1, 4016, 1007, 1, 1, 1, 14936, 7528], False),
            ([5, 2], True),
            ([1, 1, 1, 2], False),
            ([8, 5], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isPossible(arg), expected)


if __name__ == '__main__':
    unittest.main()
