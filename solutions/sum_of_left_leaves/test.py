# import solutions.sum_of_left_leaves.index as main
import unittest

import solutions.sum_of_left_leaves.index as main


class Test(unittest.TestCase):
    def test_sumOfLeftLeaves(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], 4),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg)
                self.assertEqual(s.sumOfLeftLeaves(tree), expected)


if __name__ == '__main__':
    unittest.main()
