# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

from solutions._class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        left: TreeNode = self.invertTree(root.left)
        right: TreeNode = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
