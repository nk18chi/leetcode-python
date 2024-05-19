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
    def maximum69Number(self, num: int) -> int:
        res = list(str(num))
        for i in range(len(res)):
            if res[i] == "6":
                res[i] = "9"
                break
        return int("".join(res))

    def printVertically(self, s: str) -> List[str]:
        string = s.split(" ")
        max_length = 0
        for s in string:
            max_length = max(max_length, len(s))

        res = []
        index = 0
        while index < max_length:
            word = ""
            i = 0
            for s in string:
                if index > len(s) - 1:
                    str = " "
                    i += 1
                else:
                    str = s[index]
                    i = 0
                word += str
            res += [word[: len(word) - i]]
            index += 1
        return res

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None

        lft = self.removeLeafNodes(root.left, target)
        rgt = self.removeLeafNodes(root.right, target)
        if lft is None and rgt is None and root.val == target:
            root = None

        return root

    def minTaps(self, n: int, ranges: List[int]) -> int:
        res = []
        for i, r in enumerate(ranges):
            res.append([i - r, i + r])

        def helper(self, list, switch):
            count = 0
            for li in list:
                init = 0
                if li[0] > 0:
                    init = li[0]
                last = li[1]
                if li[1] > len(switch):
                    last = len(switch)
                for i in range(init, last):
                    switch[i] = 0
                count += 1
                if sum(switch) == 0:
                    return count
            return -1

        min_number = -1
        length = len(res)
        for i in range(length):
            switch = [1] * n
            if i != 0:
                del res[0]
            num = helper(self, res, switch)
            if num > 0:
                if min_number == -1:
                    min_number = num
                else:
                    min_number = min(min_number, num)
        return min_number
