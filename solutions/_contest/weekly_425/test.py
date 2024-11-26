import unittest
import _contest.weekly_425.index as main


class Test(unittest.TestCase):
    def test_minimumSumSubarray(self):
        test_patterns = [
            ([3, -2, 1, 4], 2, 3, 1),
            ([-2, 2, -3, 1], 2, 3, -1),
            ([1, 2, 3, 4], 2, 4, 3),
        ]
        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.minimumSumSubarray(arg1, arg2, arg3),
                    expected,
                )

    def test_isPossibleToRearrange(self):
        test_patterns = [
            ("abcd", "cdab", 2, True),
            ("aabbcc", "bbaacc", 3, True),
            ("aabbcc", "bbaacc", 2, False),
        ]
        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.isPossibleToRearrange(arg1, arg2, arg3),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
