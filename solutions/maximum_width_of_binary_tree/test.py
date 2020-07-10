import unittest
import solutions.maximum_width_of_binary_tree.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_widthOfBinaryTree(self):
        test_patterns = [
            ([0, 0, 0, 0, None, None, 0, None, None, None, 0], 4),
            ([1, 3, 2, 5, 3, None, 9], 4),
            ([0], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.widthOfBinaryTree(tree), expected)


if __name__ == '__main__':
    unittest.main()
