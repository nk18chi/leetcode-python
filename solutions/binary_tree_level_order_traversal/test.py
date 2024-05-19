import unittest
import binary_tree_level_order_traversal.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_levelOrder(self):
        test_patterns = [
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1], [[1]]),
            ([None], []),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.levelOrder(tree), expected)


if __name__ == "__main__":
    unittest.main()
