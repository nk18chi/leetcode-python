import unittest
import solutions.invert_binary_tree.index as main
from solutions._class.tree_node import TreeNode, createTreeNode, getTreeNode


class Test(unittest.TestCase):
    def test_invertTreee(self):
        test_patterns = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(getTreeNode(s.invertTree(tree)), expected)


if __name__ == '__main__':
    unittest.main()
