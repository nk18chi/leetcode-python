# 112. Path Sum - Easy
# https://leetcode.com/problems/path-sum/

# from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


class Solution:
    # second solution
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        else:
            if root.left is None and root.right is None and root.val == sum:
                return True

            sum -= root.val
            return self.hasPathSum(
                root.left, sum) or self.hasPathSum(
                root.right, sum)

    # # first solution
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if root is None:
    #         return False
    #     else:
    #         if root.left is None and root.right is None:
    #             sum -= root.val
    #             if sum == 0:
    #                 return True
    #             sum += root.val
    #             return False

    #         sum -= root.val
    #         flag = False
    #         if root.left is not None:
    #             flag = self.hasPathSum(root.left, sum)
    #             if flag:
    #                 return True
    #         if root.right is not None:
    #             flag = self.hasPathSum(root.right, sum)
    #             if flag:
    #                 return True

    #         if not flag:
    #             return False


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
