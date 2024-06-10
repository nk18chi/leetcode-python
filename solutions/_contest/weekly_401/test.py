import unittest
import _contest.weekly_401.index as main


class Test(unittest.TestCase):
    def test_numberOfChild(self):
        test_patterns = [
            (3, 5, 1),
            (5, 6, 2),
            (4, 2, 2),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numberOfChild(arg1, arg2), expected)

    def test_valueAfterKSeconds(self):
        test_patterns = [
            (4, 5, 56),
            (5, 3, 35),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.valueAfterKSeconds(arg1, arg2), expected)

    def test_maxTotalReward(self):
        test_patterns = [
            ([1, 2, 7, 8, 13, 19, 19], 35),
            ([1, 1, 3, 4], 7),
            ([1, 6, 4, 3, 2], 11),
            ([1, 2, 3, 4], 7),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxTotalReward(arg1), expected)


if __name__ == "__main__":
    unittest.main()
