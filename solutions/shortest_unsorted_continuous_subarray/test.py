import unittest
import shortest_unsorted_continuous_subarray.index as main


class Test(unittest.TestCase):
    def test_findUnsortedSubarray(self):
        test_patterns = [
            ([1, 3, 2, 2, 2], 4),
            ([1, 2, 3, 3, 3], 0),
            ([5, 4, 3, 2, 1], 5),
            ([2, 6, 4, 8, 10, 9, 15], 5),
            ([2, 1], 2),
            ([0], 0),
            ([1, 2, 3, 4], 0),
            ([1, 2, 1, 4], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findUnsortedSubarray(arg), expected)


if __name__ == "__main__":
    unittest.main()
