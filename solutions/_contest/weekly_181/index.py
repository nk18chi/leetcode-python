from typing import List, Dict, Set


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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createListNode(list):
    from collections import deque
    data = list
    n = iter(data)
    node = ListNode(next(n))
    fringe = deque([node])
    while True:
        head = fringe.popleft()
        try:
            head.next = ListNode(next(n))
            fringe.append(head.next)
        except StopIteration:
            break

    return node


def getValFromListNode(node: ListNode):
    res: List[int] = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res: List[int] = []
        for n, i in zip(nums, index):
            res.insert(i, n)

        return res

    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        self.res: int = 0

        def helper(num: int):
            divisor: Set[int] = set()
            sqrt: int = math.floor(math.sqrt(num))
            for i in range(1, sqrt + 1):
                if num % i == 0:
                    divisor.add(i)
                    divisor.add(num // i)
                    if len(divisor) > 4:
                        break
            if len(divisor) == 4:
                self.res += sum(divisor)

        for n in nums:
            helper(n)

        return self.res

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.res: bool = False
        lastRow: int = len(grid) - 1
        lastCol: int = len(grid[0]) - 1

        def dfs(row: int, col: int, come: int):
            if row == len(grid) and col == len(grid[0]) - 1:
                self.res = True
                return
            if row == len(grid) - 1 and col == len(grid[0]):
                self.res = True
                return
            if row == len(grid) - 2 and col == len(grid[0]) - 1 and grid[lastRow][lastCol] == 0:
                self.res = True
                return
            if row == len(grid) - 1 and col == len(grid[0]) - 2 and grid[lastRow][lastCol] == 0:
                self.res = True
                return
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == 0:
                return

            if grid[row][col] == 1:
                grid[row][col] = 0
                if come == 2:
                    dfs(row, col - 1, come)
                elif come == 4:
                    dfs(row, col + 1, come)
                grid[row][col] = 1
                return
            if grid[row][col] == 2:
                grid[row][col] = 0
                if come == 1:
                    dfs(row + 1, col, come)
                elif come == 3:
                    dfs(row - 1, col, come)
                grid[row][col] = 2
                return
            if grid[row][col] == 3:
                grid[row][col] = 0
                if come == 3:
                    dfs(row, col - 1, 2)
                elif come == 4:
                    dfs(row + 1, col, 1)
                grid[row][col] = 3
                return
            if grid[row][col] == 4:
                grid[row][col] = 0
                if come == 2:
                    dfs(row + 1, col, 1)
                elif come == 3:
                    dfs(row, col + 1, 4)
                grid[row][col] = 4
                return
            if grid[row][col] == 5:
                grid[row][col] = 0
                if come == 1:
                    dfs(row, col - 1, 2)
                elif come == 4:
                    dfs(row - 1, col, 3)
                grid[row][col] = 5
                return
            if grid[row][col] == 6:
                grid[row][col] = 0
                if come == 1:
                    dfs(row, col + 1, 4)
                elif come == 2:
                    dfs(row - 1, col, 3)
                grid[row][col] = 6
                return

        for i in range(1, 5):
            dfs(0, 0, i)
            if self.res:
                return self.res
        return self.res

    def longestPrefix(self, s: str) -> str:
        if len(s) < 2:
            return ""
        res: str = ""
        for i in range(len(s)):
            if s[:i] == s[-i:]:
                res = s[:i]
        return res
