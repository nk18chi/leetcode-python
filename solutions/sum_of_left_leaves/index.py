# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

# from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"


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
    # first solution
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum: int = 0

        def helper(self, root: TreeNode) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val

            left: int = helper(self, root.left)
            _: int = helper(self, root.right)
            if left > 0:
                self.sum += left
            return 0

        helper(self, root)
        return self.sum

    # # second solution
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     self.sum = 0

    #     def helper(self, root):
    #         if root is None:
    #             return 0
    #         if root.left:
    #             if not root.left.left and not root.left.right:
    #                 self.sum += root.left.val

    #         helper(self, root.left)
    #         helper(self, root.right)
    #     helper(self, root)
    #     return self.sum
