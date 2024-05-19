# 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Deque, Tuple
from _class.tree_node import TreeNode
from collections import deque


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res: int = 0
        stack: Deque[Tuple[int, TreeNode]] = deque([(1, root)])  # order, node
        while stack:
            res = max(res, stack[-1][0] - stack[0][0] + 1)
            nxt: Deque[Tuple[int, TreeNode]] = deque([])
            while stack:
                order, node = stack.popleft()
                if node.left and node.left.val is not None:
                    nxt.append((order * 2 - 1, node.left))
                if node.right and node.right.val is not None:
                    nxt.append((order * 2, node.right))
            stack = nxt
        return res
