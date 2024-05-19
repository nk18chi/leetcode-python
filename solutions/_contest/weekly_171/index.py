from typing import List


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


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = n
        while True:
            if "0" in str(i - 1) or "0" in str(n - i + 1):
                i -= 1
                continue
            else:
                return [i - 1, n - i + 1]

    def minFlips(self, a: int, b: int, c: int) -> int:
        A = format(a, "b")
        B = format(b, "b")
        C = format(c, "b")

        max_len = max([len(A), len(B), len(C)])
        if max_len != len(A):
            for i in range(max_len - len(A)):
                A = "0" + A
        if max_len != len(B):
            for i in range(max_len - len(B)):
                B = "0" + B
        if max_len != len(C):
            for i in range(max_len - len(C)):
                C = "0" + C

        cnt = 0
        for a, b, c in zip(A, B, C):
            if not int(a) | int(b) == int(c):
                if int(c) == 0 and int(a) == int(b) == 1:
                    cnt += 2
                else:
                    cnt += 1
        return cnt
