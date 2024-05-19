import unittest

import maximum_average_subarray.index as main


class Test(unittest.TestCase):
    def test_findMaxAverage(self):
        test_patterns = [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),
            ([4, 0, 4, 3, 3], 5, 2.8),
            ([5], 1, 5),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findMaxAverage(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
