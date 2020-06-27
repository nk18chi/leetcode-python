import unittest
import solutions.sum_root_to_leaf_numbers.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_sumNumbers(self):
        test_patterns = [
            ([1, 2, 3], 25),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.sumNumbers(tree), expected)


if __name__ == '__main__':
    unittest.main()
