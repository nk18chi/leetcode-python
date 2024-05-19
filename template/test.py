import unittest
import format.index as main
# from _class.tree_node import TreeNode, createTreeNode, getTreeNode
# from _class.list_node import ListNode, createListNode, getListNode
# from _class.node import Node, createDoublyNode, getFlattenDoublyNode


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            ([2, 7, 11, 15], 9),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree: TreeNode = createTreeNode(arg)
                # node: Node = createDoublyNode(arg)
                self.assertEqual(s.functionName(arg), expected)

        # (test) List Node
        # for i, (arg, expected) in enumerate(test_patterns):
        #     with self.subTest(test=i):
        #         s = main.Solution()
        #         ln = createListNode(arg)
        #         ans: ListNode = getValFromListNode(s.functionName(ln))
        #         self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
