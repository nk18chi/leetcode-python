# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        if len1 < len2:
            len1, len2 = len2, len1
            str1, str2 = str2, str1

        index = len2
        while (index > 0):
            if len1 % index == 0 and len2 % index == 0:
                divide = str2[: index]
                canDivide = True
                for i in range(0, len1, index):
                    if str1[i:i + index] != divide:
                        canDivide = False
                        break
                if canDivide:
                    for i in range(0, len2, index):
                        if str2[i:i + index] != divide:
                            canDivide = False
                            break
                    if canDivide:
                        return divide
            index -= 1

        return ""


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
