import unittest
import median_of_two_sorted_arrays.index as main


class Test(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        test_patterns = [
            ([1, 2], [3, 4], 2.50000),
            ([3, 4], [1, 2], 2.50000),
            ([1, 3], [2], 2.00000),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findMedianSortedArrays(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
