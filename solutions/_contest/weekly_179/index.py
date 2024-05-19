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
    def generateTheString(self, n: int) -> str:
        res: str = ""
        for _ in range(n):
            res += "a"
        if n % 2 == 0:
            res = res[:-1] + "b"
        return res

    # def numTimesAllBlue(self, light: List[int]) -> int:
    #     checked: List[int] = [0] * (len(light) + 1)
    #     checked[0] = 1
    #     maxVal: int = 0
    #     count: int = 0
    #     for n in light:
    #         checked[n] = 1
    #         if maxVal == n - 1:
    #             maxVal = n
    #             while maxVal < len(light) and checked[maxVal + 1]:
    #                 maxVal += 1
    #             if sum(checked) == maxVal + 1:
    #                 count += 1
    #     return count

    def numTimesAllBlue(self, light: List[int]) -> int:
        right = res = 0
        for i, a in enumerate(light, 1):
            right = max(right, a)
            res += right == i
        return res

    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        assitance: Dict[int, List[int]] = {}
        interval: Dict[int, int] = {}
        for i in range(len(manager)):
            interval[i] = informTime[i]
            if manager[i] == -1:
                continue
            newAssitance: List[int] = assitance.get(manager[i], [])
            newAssitance.append(i)
            assitance[manager[i]] = newAssitance

        def helper(self, i, time) -> int:
            if i not in assitance:
                return time
            time += interval[i]
            timeList: List[int] = []
            for a in assitance[i]:
                timeList.append(helper(self, a, time))
            return max(timeList)

        return helper(self, headID, 0)

    # def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
    #     node: Dict[int, List[int]] = {}
    #     for e in edges:
    #         new: List[int] = node.get(e[0], [])
    #         new.append(e[1])
    #         node[e[0]] = new

    #     def dfs(self, n: int, probability: List[int], rest: int) -> float:
    #         if rest == 0 or n not in node:
    #             if n == target:
    #                 if len(probability) == 0:
    #                     return 1
    #                 res: float = 1 / probability[0]
    #                 for p in probability[1:]:
    #                     res *= 1 / p
    #                 return res
    #             else:
    #                 return 0
    #         probability.append(len(node[n]))
    #         for num in node[n]:
    #             val: float = dfs(self, num, probability, rest - 1)
    #             if val > 0:
    #                 return val
    #         return 0
    #     return dfs(self, 1, [], t)
