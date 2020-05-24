# 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

from typing import List
from solutions._class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space cpmplexity: O(n)
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index: int = 0

        def helper(v: int) -> TreeNode:
            if self.index == len(preorder) or preorder[self.index] > v:
                return None
            node: TreeNode = TreeNode(preorder[self.index])
            self.index += 1
            node.left = helper(node.val)
            node.right = helper(v)
            return node
        return helper(10 ** 8 + 1)
