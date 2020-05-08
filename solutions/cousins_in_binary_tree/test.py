import unittest
import solutions.cousins_in_binary_tree.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_isCousins(self):
        test_patterns = [
            ([1, 2, 3, 6, 7, 4, 5], 6, 5, True),
            ([1, 2, 3, 6, 7, 4, 5], 4, 5, False),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg1)
                self.assertEqual(s.isCousins(tree, arg2, arg3), expected)


if __name__ == '__main__':
    unittest.main()
