import unittest
import maximum_subarray.index as main


class Test(unittest.TestCase):
    def test_maxSubArray(self):
        test_patterns = [
            (
                [
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    2,
                    -1,
                    -2,
                    -2,
                    1,
                    -3,
                    4,
                    -1,
                    2,
                    1,
                    -5,
                    4,
                ],
                18,
            ),
            ([-2, -2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([-1, 2, -1, 1, 1, -2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([-2, -2, -1, -3, 0], 0),
            ([-2, -2, -1, -3, -1], -1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxSubArray(arg), expected)


if __name__ == "__main__":
    unittest.main()
