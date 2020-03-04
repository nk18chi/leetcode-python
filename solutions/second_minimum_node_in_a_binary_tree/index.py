# 671. Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

from typing import List, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


def createTreeNode(list):

    from collections import deque

    data = list
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break

    return tree


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        minList: List[int] = [root.val, -1]

        def dfs(root):
            if root is None:
                return
            if minList[1] != -1 and root.val >= minList[1]:
                return
            if root.val != minList[0]:
                minList[1] = root.val
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return minList[1]
