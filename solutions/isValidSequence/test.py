import unittest
import isValidSequence.index as main
from _class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_isValidSequence(self):
        test_patterns = [
            ([0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1], True),
            ([0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0], False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg1)
                self.assertEqual(s.isValidSequence(tree, arg2), expected)


if __name__ == "__main__":
    unittest.main()
