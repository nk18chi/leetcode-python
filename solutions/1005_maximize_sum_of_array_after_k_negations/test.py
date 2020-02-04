import unittest
import importlib
f = importlib.import_module(
    'solutions.1005_maximize_sum_of_array_after_k_negations.index')


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
                s = f.Solution()
                self.assertEqual(
                    s.largestSumAfterKNegations(
                        arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
