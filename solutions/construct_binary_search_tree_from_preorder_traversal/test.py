# import unittest
# import construct_binary_search_tree_from_preorder_traversal.index as main
# from _class.tree_node import TreeNode, createTreeNode


# class Test(unittest.TestCase):
#     def test_bstFromPreorder(self):
#         test_patterns = [
#             ([8, 5, 1, 7, 10, 12], [8, 5, 10, 1, 7, None, 12]),
#             ([10, 3, 19, 14], [8, 5, 10, 1, 7, None, 12]),
#         ]

#         for i, (arg, expected) in enumerate(test_patterns):
#             with self.subTest(test=i):
#                 s = main.Solution()
#                 tree: TreeNode = createTreeNode(expected)
#                 self.assertEqual(s.bstFromPreorder(arg), tree)


# if __name__ == '__main__':
#     unittest.main()
