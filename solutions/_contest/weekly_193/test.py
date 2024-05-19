import unittest
import _contest.weekly_193.index as main


class Test(unittest.TestCase):
    def test_findLeastNumOfUniqueInts(self):
        test_patterns = [
            ([4, 3, 1, 1, 3, 3, 2], 3, 2),
            ([5, 5, 4], 1, 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findLeastNumOfUniqueInts(arg1, arg2), expected)

    def test_minDays(self):
        test_patterns = [
            ([3, 1, 2, 4, 10], 2, 2, 4),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minDays(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
