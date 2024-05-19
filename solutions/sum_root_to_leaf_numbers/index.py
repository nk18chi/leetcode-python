# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from _class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def sumNumbers(self, root: TreeNode) -> int:
        self.res: int = 0

        def dfs(root: TreeNode, total: int):
            if root is None:
                return
            dfs(root.left, total * 10 + root.val)
            dfs(root.right, total * 10 + root.val)
            if root.left is None and root.right is None:
                self.res += total * 10 + root.val

        dfs(root, 0)
        return self.res
