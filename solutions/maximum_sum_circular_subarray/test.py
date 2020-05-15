import unittest
import solutions.maximum_sum_circular_subarray.index as main


class Test(unittest.TestCase):
    def test_maxSubarraySumCircular(self):
        test_patterns = [
            ([0, 5, 8, -9, 9, -7, 3, -2], 16),
            ([6, 9, -3], 15),
            ([2, -2, 2, 7, 8, 0], 19),
            ([5, -3, 5], 10),
            ([-1, 10, -100, 20, -2], 27),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxSubarraySumCircular(arg), expected)


if __name__ == '__main__':
    unittest.main()
