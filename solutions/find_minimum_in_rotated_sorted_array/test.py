import unittest
import find_minimum_in_rotated_sorted_array.index as main


class Test(unittest.TestCase):
    def test_findMin(self):
        test_patterns = [
            ([3, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([3, 4, 5, 1, 2], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findMin(arg), expected)


if __name__ == "__main__":
    unittest.main()
