import unittest
import _contest.weekly_171.index as main


class Test(unittest.TestCase):
    def test_getNoZeroIntegers(self):
        test_patterns = [
            (69, [68, 1]),
            (1010, [999, 11]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getNoZeroIntegers(arg), expected)

    def test_minFlips(self):
        test_patterns = [
            (4, 2, 7, 1),
            (1, 2, 3, 0),
            (2, 6, 5, 3),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minFlips(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
