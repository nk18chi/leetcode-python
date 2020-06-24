# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

from solutions._class.tree_node import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
