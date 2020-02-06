import unittest

import solutions.maximize_sum_of_array_after_k_negations.index as main


class Test(unittest.TestCase):
    def test_largestSumAfterKNegations(self):
        test_patterns = [
            ([4, 2, 3], 1, 5),
            ([-8, 3, -5, -3, -5, -2], 6, 22),
            ([-2, 9, 9, 8, 4], 5, 32),
            ([3, -1, 0, 2], 3, 6),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.largestSumAfterKNegations(
                        arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
