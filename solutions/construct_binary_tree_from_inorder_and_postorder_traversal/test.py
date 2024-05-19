import unittest
import construct_binary_tree_from_inorder_and_postorder_traversal.index as main
from _class.tree_node import createTreeNode, getTreeNode


class Test(unittest.TestCase):
    def test_buildTree(self):
        test_patterns = [
            (
                [11, 9, 14, 3, 15, 20, 7],
                [11, 14, 9, 15, 7, 20, 3],
                [3, 9, 20, 11, 14, 15, 7],
            ),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    getTreeNode(s.buildTree(arg1, arg2)),
                    getTreeNode(createTreeNode(expected)),
                )


if __name__ == "__main__":
    unittest.main()
