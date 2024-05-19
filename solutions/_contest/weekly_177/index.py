from typing import List, Dict, Set


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
        except BaseException:
            break

    return tree


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        import math

        timestamp1 = int(
            datetime.datetime(
                int(date1[0:4]), int(date1[5:7]), int(date1[8:10])
            ).strftime("%s")
        )
        timestamp2 = int(
            datetime.datetime(
                int(date2[0:4]), int(date2[5:7]), int(date2[8:10])
            ).strftime("%s")
        )
        if timestamp1 < timestamp2:
            timestamp1, timestamp2 = timestamp2, timestamp1
        diff = (timestamp1 - timestamp2) / (60 * 60 * 24)

        return math.floor(abs(diff))

    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        def dfs(self, target: int):
            if not self.res:
                return
            if target in self.seen:
                self.res = False
                return
            self.seen.add(target)
            if leftChild[target] > -1:
                self.sum += 1
                dfs(self, leftChild[target])
            if rightChild[target] > -1:
                self.sum += 1
                dfs(self, rightChild[target])

        self.res: bool = True
        self.seen: Set[int] = set()
        self.sum: int = 1
        dfs(self, 0)
        return self.res if n == self.sum else False

    def closestDivisors(self, num: int) -> List[int]:
        def helper(self, n) -> List[int]:
            import math

            for i in range(math.floor(math.sqrt(n)), -1, -1):
                if n % i == 0:
                    return [n // i, i]
            return [0, 0]

        first: List[int] = helper(self, num + 1)
        second: List[int] = helper(self, num + 2)
        return first if first[0] - first[1] < second[0] - second[1] else second

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        total: int = sum(digits)
        digits.sort(reverse=True)

        def helper(self, d: List[int]) -> str:
            if not d:
                return ""
            if sum(digits) == 0:
                return "0"
            return "".join(map(str, d))

        if total % 3 == 0:
            return helper(self, digits)

        dict: Dict[int, List[int]] = {}
        for d in digits:
            if d % 3 in dict:
                dict[d % 3].append(d)
            else:
                dict[d % 3] = [d]

        if total % 3 == 1 and 1 in dict:
            digits.remove(dict[1][-1])
            return helper(self, digits)
        if total % 3 == 2 and 2 in dict:
            digits.remove(dict[2][-1])
            return helper(self, digits)
        if 0 in dict:
            return helper(self, dict[0])
        return ""

        # time limit exceeded
        # def helper(self, num: str, rests: List[int]):
        #     if self.res != "":
        #         return
        #     if len(num) > 0 and int(num) % 3 == 0:
        #         if len(rests) < 1:
        #             self.res = str(int(num))
        #         self.dict[len(num)] = max(self.dict[len(num)], int(num))
        #     for i in range(len(rests)):
        #         if not num + str(rests[i]) in self.seen:
        #             self.seen.add(num + str(rests[i]))
        #             helper(self, num + str(rests[i]), rests[:i] + rests[i + 1:])
        #     return

        # self.res: str = ""
        # self.seen: Set[str] = set()
        # self.dict: Dict[int, int] = {}
        # for i in range(len(digits)):
        #     self.dict[i + 1] = -1
        # digits.sort(reverse=True)
        # helper(self, "", digits)
        # if self.res != "":
        #     return self.res
        # for i in range(len(digits), 0, -1):
        #     if self.dict[i] > -1:
        #         return str(self.dict[i])
        # return ""
