import unittest
import _contest.weekly_423.index as main


class Test(unittest.TestCase):
    def test_hasIncreasingSubarrays(self):
        test_patterns = [
            ([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3, True),
            ([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5, False),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.hasIncreasingSubarrays(arg1, arg2),
                    expected,
                )

    def test_maxIncreasingSubarrays(self):
        test_patterns = [
            ([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3),
            ([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 2),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.maxIncreasingSubarrays(arg1),
                    expected,
                )

    def test_sumOfGoodSubsequences(self):
        test_patterns = [([1, 2, 1], 14), ([3, 4, 5], 40)]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.sumOfGoodSubsequences(arg1),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
