# 687. Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/


def main():
    tree = createTreeNode([1, 4, 5, 4, 4, 5, 4, 4])
    s = Solution()
    print(s.longestUnivaluePath(tree))


# Definition for a binary tree node.
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.sum = 0
        self.getMaxLengthPath(root)
        return self.sum

    def getMaxLengthPath(self, node: TreeNode) -> int:
        if not node:
            return 0
        elif not node.left and not node.right:
            return 0
        else:
            l = r = 0
            if node.left:
                child = self.getMaxLengthPath(node.left)
                l = child + 1 if node.val == node.left.val else 0
            if node.right:
                child = self.getMaxLengthPath(node.right)
                r = child + 1 if node.val == node.right.val else 0

            if node.left and node.right and node.val == node.left.val == node.right.val:
                self.sum = max(self.sum, l + r)
            else:
                self.sum = max(self.sum, max(l, r))

            return max(l, r)


if __name__ == '__main__':
    main()
