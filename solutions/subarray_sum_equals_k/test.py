import unittest
import solutions.subarray_sum_equals_k.index as main


class Test(unittest.TestCase):
    def test_subarraySum(self):
        test_patterns = [
            ([3, 4, 7, -2, -2, 1, 4, 2], 7, 4),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.subarraySum(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
