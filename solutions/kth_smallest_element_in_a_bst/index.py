# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from _class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res: int = 0
        self.isAnswer: bool = False
        self.k = k

        def dfs(root: TreeNode):
            if root is None or self.isAnswer:
                return
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                self.isAnswer = True
            dfs(root.right)

        dfs(root)
        return self.res
