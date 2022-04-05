import unittest
import solutions._contest.weekly_287.index as main


class Test(unittest.TestCase):
    def test_convertTime(self):
        test_patterns = [
            ("02:30", "04:35", 3),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.convertTime(arg1, arg2), expected)

    def test_findWinners(self):
        test_patterns = [
            ([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]], [[1, 2, 10], [4, 5, 7, 8]]),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findWinners(arg1), expected)

    def test_maximumCandies(self):
        test_patterns = [
            ([5, 8, 6], 3, 5),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumCandies(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
