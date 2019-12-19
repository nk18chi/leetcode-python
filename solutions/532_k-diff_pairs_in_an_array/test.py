import unittest
import importlib
f = importlib.import_module('solutions.532_k-diff_pairs_in_an_array.index')


class Test(unittest.TestCase):
    def test_findPairs(self):
        test_patterns = [
            ([1, 3, 1, 5, 4], 0, 1),
            ([3, 1, 4, 1, 5], 2, 2),
            ([1, 2, 3, 4, 5], 1, 4),
            ([1, 3, 1, 5, 4], 0, 1)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.findPairs(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
