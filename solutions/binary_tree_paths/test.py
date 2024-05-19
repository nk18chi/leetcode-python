import unittest
import binary_tree_paths.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_binaryTreePaths(self):
        test_patterns = [
            ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.binaryTreePaths(tree), expected)


if __name__ == "__main__":
    unittest.main()
