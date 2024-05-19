import unittest
import largest_divisible_subset.index as main


class Test(unittest.TestCase):
    def test_largestDivisibleSubset(self):
        test_patterns = [
            ([4, 8, 10, 240], [4, 8, 240]),
            ([1, 2, 4, 7, 21, 63], [1, 7, 21, 63]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.largestDivisibleSubset(arg), expected)


if __name__ == "__main__":
    unittest.main()
