# 538. Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/

# from typing import List


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
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)

        return root

    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     self.total = 0
    #     self.helper(root)
    #     return root

    # def helper(self, root):
    #     if not root:
    #         return
    #     self.helper(root.right)
    #     self.total += root.val
    #     root.val = self.total
    #     self.helper(root.left)
