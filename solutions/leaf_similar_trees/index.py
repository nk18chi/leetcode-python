# 872. Leaf-Similar Trees - Easy
# https://leetcode.com/problems/leaf-similar-trees/

from typing import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.list1 = []
        self.list2 = []
        self.getLeavesVal(root1, self.list1)
        self.getLeavesVal(root2, self.list2)

        return True if self.list1 == self.list2 else False

    def getLeavesVal(self, root, list):
        if root is None:
            return
        else:
            if root.left is None and root.right is None:
                return list.append(root.val)
            else:
                self.getLeavesVal(root.left, list)
                self.getLeavesVal(root.right, list)
