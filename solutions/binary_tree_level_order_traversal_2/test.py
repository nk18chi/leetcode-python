import unittest
import binary_tree_level_order_traversal_2.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_levelOrderBottom(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7], [[4, 5, 6, 7], [2, 3], [1]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.levelOrderBottom(tree), expected)


if __name__ == "__main__":
    unittest.main()
