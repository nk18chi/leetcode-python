import unittest
import count_complete_tree_nodes.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_countNodes(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6], 6),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.countNodes(tree), expected)


if __name__ == "__main__":
    unittest.main()
