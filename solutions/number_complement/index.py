# 476. Number Complement
# https://leetcode.com/problems/number-complement/

# from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        # # first solution
        # bit_num = format(num, 'b')
        # res = ""
        # for n in bit_num:
        #     res += "0" if n == '1' else "1"

        # return int(res, 2)

        # second solution
        bit_num = format(num, 'b')
        res = ""
        for n in bit_num:
            res += str(int(n) ^ 1)

        return int(res, 2)


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
