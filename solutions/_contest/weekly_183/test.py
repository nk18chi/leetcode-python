import unittest
import solutions._contest.weekly_183.index as main


class Test(unittest.TestCase):
    def test_minSubsequence(self):
        test_patterns = [
            ([4, 4, 7, 6, 7], [7, 7, 6]),
            ([4, 3, 10, 9, 8], [10, 9]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSubsequence(arg), expected)

    def test_numSteps(self):
        test_patterns = [
            ("1101", 6),
            ("10", 1),
            ("1", 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numSteps(arg), expected)

    def test_longestDiverseString(self):
        test_patterns = [
            (1, 1, 7, "ccaccbcc"),
            (2, 2, 1, "aabbc"),
            (7, 1, 0, "aabaa")
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestDiverseString(arg1, arg2, arg3), expected)

    def test_stoneGameIII(self):
        test_patterns = [
            ([1, 2, 3, -9], "Alice"),
            ([1, 2, 3, 7], "Bob"),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.stoneGameIII(arg1), expected)


if __name__ == '__main__':
    unittest.main()
