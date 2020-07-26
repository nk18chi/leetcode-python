import unittest
import solutions.binary_tree_zigzag_level_order_traversal.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_zigzagLevelOrder(self):
        test_patterns = [
            ([3, 9, 20, 10, 2, 15, 7], [[3], [20, 9], [10, 2, 15, 7]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.zigzagLevelOrder(tree), expected)


if __name__ == '__main__':
    unittest.main()
