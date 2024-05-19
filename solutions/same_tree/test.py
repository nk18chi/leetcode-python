import unittest
import same_tree.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_isSameTree(self):
        test_patterns = [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2], [1, None, 2], False),
            ([1, 2, 1], [1, 1, 2], False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree1: TreeNode = createTreeNode(arg1)
                tree2: TreeNode = createTreeNode(arg2)
                self.assertEqual(s.isSameTree(tree1, tree2), expected)


if __name__ == "__main__":
    unittest.main()
