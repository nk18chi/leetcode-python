# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import List, Deque, Optional, Tuple
from solutions._class.tree_node import TreeNode
from collections import deque


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        queue: Deque[Tuple[TreeNode, int]] = deque([(root, 0)])
        while len(queue) > 0:
            q: Tuple[TreeNode, int] = queue.popleft()
            if not q[0] or not q[0].val:
                continue
            if len(res) <= q[1]:
                res.append([])
            res[q[1]].append(q[0].val)
            queue.append((q[0].left, q[1] + 1))
            queue.append((q[0].right, q[1] + 1))
        return res
