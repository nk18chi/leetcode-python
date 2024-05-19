import unittest
import merge_intervals.index as main


class Test(unittest.TestCase):
    def test_merge(self):
        test_patterns = [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[8, 10], [1, 3], [2, 6], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 3], [4, 5]], [[1, 3], [4, 5]]),
            ([[1, 3]], [[1, 3]]),
            ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.merge(arg), expected)


if __name__ == "__main__":
    unittest.main()
