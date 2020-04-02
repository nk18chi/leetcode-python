# import unittest
# import solutions.lowest_common_ancestor_of_a_binary_search_tree.index as main


# class Test(unittest.TestCase):
#     def test_lowestCommonAncestor(self):
#         test_patterns = [
#             ([6, 2, 8, 0, 4, 7, 9], [2, 0, 4], [8, 7, 9], [6, 2, 8, 0, 4, 7, 9]),
#         ]

#         for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
#             with self.subTest(test=i):
#                 s = main.Solution()
#                 tree1 = main.createTreeNode(arg1)
#                 tree2 = main.createTreeNode(arg2)
#                 tree3 = main.createTreeNode(arg3)
#                 tree4 = main.createTreeNode(expected)
#                 self.assertEqual(s.lowestCommonAncestor(tree1, tree2, tree3), tree4)


# if __name__ == '__main__':
#     unittest.main()
