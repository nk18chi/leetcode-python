import unittest
import solutions.kth_smallest_element_in_a_bst.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_kthSmallest(self):
        test_patterns = [
            ([4, 2, 6, 1, 3, 5, 7], 1, 1),
            ([4, 2, 6, 1, 3, 5, 7], 3, 3),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree: TreeNode = createTreeNode(arg1)
                self.assertEqual(s.kthSmallest(tree, arg2), expected)


if __name__ == '__main__':
    unittest.main()
