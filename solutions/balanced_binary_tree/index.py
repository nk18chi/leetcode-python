# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# from typing import List


class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root) -> int:
            if root is None:
                return 0
            else:
                left: int = self.isBalanced(root.left)
                right: int = self.isBalanced(root.right)

                if left == -1 or right == -1 or abs(left - right) > 1:
                    return -1
                return 1 + max(left, right)

        return dfs(root) != -1
