import unittest
import solutions._contest.weekly_181.index as main


class Test(unittest.TestCase):
    def test_createTargetArray(self):
        test_patterns = [
            ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.createTargetArray(arg1, arg2), expected)

    def test_sumFourDivisors(self):
        test_patterns = [
            ([21, 4, 7], 32),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.sumFourDivisors(arg), expected)

    def test_hasValidPath(self):
        test_patterns = [
            ([[2, 6]], False),
            ([[6, 1, 3], [4, 1, 5]], True),
            ([[4, 1], [6, 1]], True),
            ([[2, 4, 3], [6, 5, 2]], True),
            ([[1, 1, 2]], False),
            ([[1, 1, 1, 1, 1, 1, 3]], True),
            ([[2], [2], [2], [2], [2], [2], [6]], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.hasValidPath(arg), expected)

    def test_longestPrefix(self):
        test_patterns = [
            ("level", "l"),
            ("ababab", "abab"),
            ("leetcodeleet", "leet"),
            ("a", "")
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestPrefix(arg), expected)


if __name__ == '__main__':
    unittest.main()
