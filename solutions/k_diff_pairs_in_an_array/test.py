import unittest

import k_diff_pairs_in_an_array.index as main


class Test(unittest.TestCase):
    def test_findPairs(self):
        test_patterns = [
            ([1, 3, 1, 5, 4], 0, 1),
            ([3, 1, 4, 1, 5], 2, 2),
            ([1, 2, 3, 4, 5], 1, 4),
            ([1, 3, 1, 5, 4], 0, 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.findPairs(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
