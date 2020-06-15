# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

from solutions._class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
