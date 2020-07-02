# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import List, Deque
from solutions._class.tree_node import TreeNode
from collections import deque


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res: List[List[int]] = []
        queue: Deque[TreeNode] = deque([root])
        while queue:
            nxt: Deque[TreeNode] = deque([])
            level: List[int] = []
            while queue:
                node: TreeNode = queue.popleft()
                if node is None:
                    continue
                level.append(node.val)
                nxt.append(node.left)
                nxt.append(node.right)
            if len(level) > 0:
                res.append(level)
            queue = nxt
        res.reverse()
        return res
