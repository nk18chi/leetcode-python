import unittest
import _contest.weekly_403.index as main


class Test(unittest.TestCase):
    def test_minimumAverage(self):
        test_patterns = [
            ([7, 8, 3, 4, 15, 13, 4, 1], 5.5),
            ([1, 9, 8, 3, 10, 5], 5.5),
            ([1, 2, 3, 7, 8, 9], 5),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumAverage(arg1), expected)

    def test_minimumArea(self):
        test_patterns = [
            ([[0, 1, 0], [1, 0, 1]], 6),
            ([[1, 0], [0, 0]], 1),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumArea(arg1), expected)

    def test_maximumTotalCost(self):
        test_patterns = [
            ([-1, -100, -2, -3, -4], 98),
            ([-5, 2, 5], 2),
            ([-3, -6, 9, -9], 21),
            ([1, -2, 3, 4], 10),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumTotalCost(arg1), expected)


if __name__ == "__main__":
    unittest.main()
