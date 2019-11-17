# id. Title
# url

# from typing import List


def main():
    tree = createTreeNode([5, 5, 5, 1, 1, 5])
    s = Solution()
    print(s.functionName())


class Solution:
    def functionName(self, args: str) -> str:
        return


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


if __name__ == '__main__':
    main()
