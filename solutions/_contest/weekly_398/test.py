import unittest
import _contest.weekly_398.index as main


class Test(unittest.TestCase):
    def test_isArraySpecial(self):
        test_patterns = [
            ([1], True),
            ([2, 1, 4], True),
            ([4, 3, 1, 6], False),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isArraySpecial(arg1), expected)

    def test_isArraySpecial2(self):
        test_patterns = [
            (
                [3, 4, 1, 2, 6, 1, 2, 3],
                [[0, 1], [0, 2], [0, 4], [1, 2], [3, 4], [6, 7]],
                [True, True, False, True, False, True],
            ),
            ([1], [[0, 0]], [True]),
            ([1], [[0, 0]], [True]),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isArraySpecial2(arg1, arg2), expected)

    def test_sumDigitDifferences(self):
        test_patterns = [
            ([13, 23, 12], 4),
            ([10, 10, 10, 10], 0),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.sumDigitDifferences(arg1), expected)


if __name__ == "__main__":
    unittest.main()
