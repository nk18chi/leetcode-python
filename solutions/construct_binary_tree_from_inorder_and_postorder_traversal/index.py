# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List, Dict
from _class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            idx: int = postorder.pop()
            root: TreeNode = TreeNode(idx)
            divided: int = indexMap[idx]
            root.right = helper(divided + 1, end)
            root.left = helper(start, divided - 1)
            return root

        indexMap: Dict[int, int] = {}
        for i, n in enumerate(inorder):
            indexMap[n] = i
        return helper(0, len(inorder) - 1)
