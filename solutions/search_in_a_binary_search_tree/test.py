import unittest
import search_in_a_binary_search_tree.index as main
from _class.tree_node import TreeNode, createTreeNode, getTreeNode


class Test(unittest.TestCase):
    def test_searchBST(self):
        test_patterns = [([4, 2, 7, 1, 3, 6, 10], 2, [2, 1, 3])]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg1)
                self.assertEqual(getTreeNode(s.searchBST(tree, arg2)), expected)


if __name__ == "__main__":
    unittest.main()
