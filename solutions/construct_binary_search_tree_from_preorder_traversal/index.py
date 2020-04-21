# 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

from typing import List
from solutions._class.tree_node import TreeNode


class Solution:
    # # Time complexity: O(nlogn)
    # # Space cpmplexity: O(n)
    # def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    #     def bs(arr: List[int], target: int) -> int:
    #         start: int = 0
    #         end: int = len(arr) - 1
    #         while start <= end:
    #             mid: int = (start + end) // 2
    #             if arr[mid] > target:
    #                 end = mid - 1
    #             else:
    #                 start = mid + 1
    #         return end + 1

    #     if not preorder:
    #         return None
    #     node: TreeNode = TreeNode(preorder[0])
    #     i: int = bs(preorder[1:], preorder[0]) + 1
    #     node.left = self.bstFromPreorder(preorder[1:i])
    #     node.right = self.bstFromPreorder(preorder[i:])
    #     return node

    # Time complexity: O(n)
    # Space cpmplexity: O(n)
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index: int = 0

        def helper(root: float) -> TreeNode:
            if self.index == len(preorder) or preorder[self.index] > root:
                return None
            node: TreeNode = TreeNode(preorder[self.index])
            self.index += 1
            node.left = helper(node.val)
            node.right = helper(root)
            return node
        return helper(float("inf"))
