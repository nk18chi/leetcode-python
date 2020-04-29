import unittest
import solutions.binary_tree_maximum_path_sum.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_maxPathSum(self):
        test_patterns = [
            ([-10, 9, 20, 0, 0, 15, 7], 42),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.maxPathSum(tree), expected)


if __name__ == '__main__':
    unittest.main()
