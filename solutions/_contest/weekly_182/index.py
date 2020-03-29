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
    def findLucky(self, arr: List[int]) -> int:
        dict: Dict = {}
        for a in arr:
            dict[a] = dict.get(a, 0) + 1
        res: int = -1
        for k, v in dict.items():
            if k == v:
                res = max(res, v)
        return res

    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        pattern: List[List[int]] = [[rating[0]]]
        res: int = 0
        for r in rating[1:]:
            arr: List[int] = []
            for p in pattern:
                if len(p) == 2:
                    if p[0] < p[1] < r or p[0] > p[1] > r:
                        res += 1
                else:
                    arr.append(p + [r])
            pattern.extend(arr)
            pattern.append([r])
        return res

    class UndergroundSystem:

        def __init__(self):
            self.checkin: Dict[str, List[int]] = {}
            self.time: Dict[int, List[int]] = {}

        def checkIn(self, id: int, stationName: str, t: int) -> None:
            self.checkin[id] = [stationName, t]

        def checkOut(self, id: int, stationName: str, t: int) -> None:
            name = self.checkin[id][0] + "@@@" + stationName
            if name in self.time:
                self.time[name][0] += t - self.checkin[id][1]
                self.time[name][1] += 1
            else:
                self.time[name] = [t - self.checkin[id][1], 1]

        def getAverageTime(self, startStation: str, endStation: str) -> float:
            name = startStation + "@@@" + endStation
            return self.time[name][0] / self.time[name][1]
