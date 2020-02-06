# 367. Valid Perfect Square - Easy
# https://leetcode.com/problems/valid-perfect-square/

# from typing import List


class Solution:
    # third solution
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while (True):
            mid = (end + start) // 2
            if num == mid * mid:
                return True
            elif start > end:
                return False
            elif num < mid * mid:
                end = mid - 1
            else:
                start = mid + 1

    # # fourth solution
    # def isPerfectSquare(self, num: int) -> bool:
    #     i = 1
    #     while num > 0:
    #         num -= i
    #         i += 2
    #     return num == 0

    # # second solution
    # def isPerfectSquare(self, num: int) -> bool:
    #     return self.isSqrtByBinarySearch(num, 0, num)

    # def isSqrtByBinarySearch(self, num, start, end):
    #     mid = (end + start) // 2
    #     if start > end:
    #         return False
    #     elif num == mid * mid:
    #         return True
    #     elif num < mid * mid:
    #         return self.isSqrtByBinarySearch(num, start, mid - 1)
    #     else:
    #         return self.isSqrtByBinarySearch(num, mid + 1, end)

    # # first solution
    # def isPerfectSquare(self, num: int) -> bool:
    #     index = 2
    #     while (num / 2 >= index):
    #         if index == num / index:
    #             return True
    #         index += 1

    #     return False


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
