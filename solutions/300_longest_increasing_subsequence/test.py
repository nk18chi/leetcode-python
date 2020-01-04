import unittest
import importlib
f = importlib.import_module(
    'solutions.300_longest_increasing_subsequence.index')


class Test(unittest.TestCase):
    def test_lengthOfLIS(self):
        test_lengthOfLIS = [
            ([10, 9, 2, 5, 6, 7, 3, 4, 8, 9], 6),
            ([], 0),
            ([0], 1),
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ]

        for i, (arg, expected) in enumerate(test_lengthOfLIS):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.lengthOfLIS(arg), expected)


if __name__ == '__main__':
    unittest.main()
