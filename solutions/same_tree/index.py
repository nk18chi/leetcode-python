# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# from typing import List, Dict
from _class.tree_node import TreeNode


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
