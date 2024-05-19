import unittest
import _contest.weekly_256.index as main


class Test(unittest.TestCase):
    def test_minimumDifference(self):
        test_patterns = [
            ([90], 1, 0),
            ([9, 4, 1, 7], 2, 2),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumDifference(arg1, arg2), expected)

    def test_kthLargestNumber(self):
        test_patterns = [
            (["2", "21", "12", "1"], 3, "2"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kthLargestNumber(arg1, arg2), expected)

    def test_minSessions(self):
        test_patterns = [
            ([2, 3, 3, 4, 4, 4, 5, 6, 7, 10], 12, 4),
            ([2, 3, 4], 6, 2),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSessions(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
