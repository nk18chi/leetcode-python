# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

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
    # def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
    #     self.res: List[List[int]] = []

    #     def dfs(self, root: TreeNode, path: List[int]):
    #         if root is None:
    #             return
    #         path.append(root.val)
    #         if root.left is None and root.right is None:
    #             if sum(path) == total:
    #                 self.res.append(path)
    #             return
    #         dfs(self, root.left, path[:])
    #         dfs(self, root.right, path[:])
    #     dfs(self, root, [])
    #     return self.res

    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(root: TreeNode):
            if root is None:
                return
            path.append(root.val)
            if root.left is None and root.right is None:
                if sum(path) == total:
                    res.append(path[:])
                path.pop()
                return
            dfs(root.left)
            dfs(root.right)
            path.pop()

        dfs(root)
        return res
