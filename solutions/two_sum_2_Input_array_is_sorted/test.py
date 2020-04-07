import unittest
import solutions.two_sum_2_Input_array_is_sorted.index as main


class Test(unittest.TestCase):
    def test_twoSum(self):
        test_patterns = [
            ([-2, 2, 4, 4, 5, 7, 10, 15], 25, [7, 8]),
            ([2, 3, 4, 5], 6, [1, 3]),
            ([2, 3, 4], 6, [1, 3]),
            ([2, 7, 11, 15], 9, [1, 2]),
            ([-2, 2, 3, 4, 5, 7, 10, 21], 19, [1, 8]),
            ([-2, 2, 3, 4, 5, 7, 10, 21], 25, [4, 8]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.twoSum(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
