import unittest
import importlib
f = importlib.import_module('solutions.404_sum_of_left_leaves.index')


class Test(unittest.TestCase):
    def test_sumOfLeftLeaves(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], 4),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree = f.createTreeNode(arg)
                self.assertEqual(s.sumOfLeftLeaves(tree), expected)


if __name__ == '__main__':
    unittest.main()
