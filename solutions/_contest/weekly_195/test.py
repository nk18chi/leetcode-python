import unittest
import _contest.weekly_195.index as main


class Test(unittest.TestCase):
    def test_isPathCrossing(self):
        test_patterns = [
            ("NES", False),
            ("NESWW", True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isPathCrossing(arg), expected)

    def test_canArrange(self):
        test_patterns = [
            (
                [
                    5,
                    3,
                    10,
                    1,
                    -7,
                    0,
                    33,
                    -1,
                    10,
                    8,
                    -3,
                    0,
                    -10,
                    47,
                    -9,
                    -6,
                    38,
                    8,
                    5,
                    38,
                    -4,
                    4,
                    -5,
                    -8,
                    -4,
                    0,
                    -8,
                    5,
                    7,
                    3,
                    -3,
                    0,
                    6,
                    8,
                    47,
                    39,
                    35,
                    39,
                    4,
                    9,
                ],
                43,
                True,
            ),
            ([-1, -1, 0, 0, 1, 2, 3, 4, 1, 1], 5, True),
            ([-4, -7, 5, 2, 9, 1, 10, 4, -8, -3], 3, True),
            ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.canArrange(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
