import unittest
import _contest.weekly_197.index as main


class Test(unittest.TestCase):
    def test_maxProbability(self):
        test_patterns = [
            (
                4,
                [
                    [1, 2],
                    [0, 2],
                    [2, 3],
                    [0, 1],
                ],
                [
                    0.5,
                    0.2,
                    1,
                    0.5,
                ],
                0,
                3,
                0.25000,
            ),
            (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25000),
        ]

        for i, (arg1, arg2, arg3, arg4, arg5, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.maxProbability(arg1, arg2, arg3, arg4, arg5), expected
                )


if __name__ == "__main__":
    unittest.main()
