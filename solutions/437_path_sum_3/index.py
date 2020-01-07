# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/


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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(self, root, list):
            if not root:
                return
            if root.val == sum:
                self.total += 1
            for i in range(len(list)):
                list[i] += root.val
                if list[i] == sum:
                    self.total += 1
            list.append(root.val)
            helper(self, root.left, list[::])
            helper(self, root.right, list[::])

        self.total = 0
        helper(self, root, [])
        return self.total
