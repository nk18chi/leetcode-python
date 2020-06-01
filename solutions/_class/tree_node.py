from typing import List, Deque
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


def createTreeNode(list):
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


def getTreeNode(root: TreeNode):
    res: List[int] = []
    d: Deque[TreeNode] = deque([root])
    while d:
        nxt: Deque[TreeNode] = deque()
        while d:
            node: TreeNode = d.popleft()
            res.append(node.val)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        d = nxt
    return res
