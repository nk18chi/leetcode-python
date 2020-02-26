# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/

# from typing import List, Dict


class Solution:
    class RecentCounter:
        # # first solution(array)
        # def __init__(self):
        #     self.queue = []

        # def ping(self, t: int) -> int:
        #     self.queue.append(t)
        #     while self.queue[0] < t - 3000:
        #         self.queue.pop(0)
        #     return len(self.queue)

        # # second solution(binary search)

        # def __init__(self):
        #     self.list = []

        # def ping(self, t: int) -> int:
        #     def bs(self, target):
        #         left, right = 0, len(self.list) - 1
        #         while left <= right:
        #             mid = (right + left) // 2
        #             if self.list[mid] == target:
        #                 return mid
        #             if self.list[mid] < target:
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         return left
        #     index = bs(self, t - 3000)
        #     self.list.append(t)
        #     return len(self.list[index:])

        # third solution(library)

        def __init__(self):
            import collections
            self.q = collections.deque()

        def ping(self, t):
            self.q.append(t)
            while self.q[0] < t - 3000:
                self.q.popleft()

            return len(self.q)


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
