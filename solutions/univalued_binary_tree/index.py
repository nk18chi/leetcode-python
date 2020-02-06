# 965. Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/


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
    def isUnivalTree(self, root: TreeNode) -> bool:
        # second solution
        if not root:
            return True

        if root.right and root.val != root.right.val:
            return False
        if root.left and root.val != root.left.val:
            return False

        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)

        # # first solution
        # def dfs(self, node):
        #     if not node:
        #         return

        #     self.seen.add(node.val)
        #     dfs(self, node.left)
        #     dfs(self, node.right)

        # self.seen = set()
        # dfs(self, root)
        # return len(self.seen) == 1
