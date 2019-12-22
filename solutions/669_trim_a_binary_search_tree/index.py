# 669. Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/

# from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        else:
            if root.val < L:
                return self.trimBST(root.right, L, R)
            elif root.val > R:
                return self.trimBST(root.left, L, R)

            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)

            return root

        return
