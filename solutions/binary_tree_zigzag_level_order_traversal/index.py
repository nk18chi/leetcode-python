# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List
from _class.tree_node import TreeNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res: List[List[int]] = []
        queue: List[TreeNode] = [root]
        isLeftToRight: bool = True
        while queue:
            nxt: List[TreeNode] = []
            level: List[int] = []
            while queue:
                node: TreeNode = queue.pop()
                if node is None:
                    continue
                level.append(node.val)
                if isLeftToRight:
                    nxt.append(node.left)
                    nxt.append(node.right)
                else:
                    nxt.append(node.right)
                    nxt.append(node.left)
            if level:
                res.append(level)
            queue = nxt
            isLeftToRight = not isLeftToRight
        return res
