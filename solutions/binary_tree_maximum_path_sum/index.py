# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from _class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxPathSum(self, root: TreeNode) -> int:
        self.res: float = float("-inf")

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left: int = dfs(root.left)
            right: int = dfs(root.right)
            self.res = max(self.res, root.val + max(left, right, left + right, 0))
            return root.val + max(left, right, 0)

        dfs(root)
        return int(self.res)
