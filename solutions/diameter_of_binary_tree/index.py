# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

from _class.tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxPath: int = 0

        def dfs(root: TreeNode):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxPath = max(self.maxPath, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.maxPath
