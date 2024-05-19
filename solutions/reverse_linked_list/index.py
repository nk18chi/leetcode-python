# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

from typing import List, Dict


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
    def reverseList(self, head: ListNode) -> ListNode:
        res: ListNode = ListNode(0)
        self.cur = res

        def dfs(self, node: ListNode):
            if node is None:
                return
            dfs(self, node.next)
            self.cur.next = ListNode(node.val)
            self.cur = self.cur.next

        dfs(self, head)

        return res.next
