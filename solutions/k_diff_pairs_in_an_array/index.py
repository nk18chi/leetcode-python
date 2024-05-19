# 532. K-diff Pairs in an Array - Easy
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from typing import List


class Solution:
    # second solution
    def findPairs(self, nums: List[int], k: int) -> int:
        dict = {}
        for n in nums:
            dict[n] = dict[n] + 1 if n in dict else 1

        count = 0
        for i in dict.keys():
            if (i + k in dict and k > 0) or (k == 0 and dict[i] > 1):
                count += 1
        return count

    # # first solution
    # def findPairs(self, nums: List[int], k: int) -> int:
    #     if k < 0:
    #         return 0
    #     if k == 0:
    #         dict = {}
    #         for n in nums:
    #             if n in dict:
    #                 dict[n] += 1
    #             else:
    #                 dict[n] = 1
    #         count = 0
    #         for v in dict.values():
    #             if v > 1:
    #                 count += 1
    #         return count

    #     count = 0
    #     set_nums = set(nums)
    #     for n in set_nums:
    #         count += len(set_nums.intersection([n + k]))

    #     return count


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
