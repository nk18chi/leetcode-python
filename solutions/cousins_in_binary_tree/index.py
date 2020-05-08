# 993. Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/

from typing import List
from solutions._class.tree_node import TreeNode


class Solution:
    # BFS solution
    # Time complexity: O(n)
    # Space complexity: O(logn)
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack: List[TreeNode] = [root]
        parentDiff: int = 0
        while len(stack) > 0:
            newStack: List[TreeNode] = []
            while len(stack) > 0:
                n: TreeNode = stack.pop()
                for child in (n.left, n.right):
                    if not child:
                        continue
                    if child.val == x:
                        x = 0
                        parentDiff += n.val
                    elif child.val == y:
                        y = 0
                        parentDiff -= n.val
                    newStack.append(child)
            stack.extend(newStack)
            if x == 0 or y == 0:
                return x == 0 and y == 0 and parentDiff != 0
            stack = newStack

        return False
