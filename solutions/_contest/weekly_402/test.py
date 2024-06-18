import unittest
import _contest.weekly_402.index as main


class Test(unittest.TestCase):
    def test_countCompleteDayPairs(self):
        test_patterns = [
            ([72, 48, 24, 3], 3),
            ([13, 11], 1),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countCompleteDayPairs(arg1), expected)

    def test_maximumTotalDamage(self):
        test_patterns = [
            ([2, 2, 3, 5, 7], 11),
            ([5, 9, 2, 10, 2, 7, 10, 9, 3, 8], 31),
            ([8, 1, 9, 6, 6, 7, 7, 8], 22),
            ([1, 6, 6, 7], 13),
            ([1, 6, 6, 7, 7], 15),
            ([1, 6, 6, 7, 7, 8], 15),
            ([1, 6, 6, 7, 7, 8, 8], 17),
            ([1, 6, 6, 7, 7, 8, 8, 9], 22),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumTotalDamage(arg1), expected)


if __name__ == "__main__":
    unittest.main()
