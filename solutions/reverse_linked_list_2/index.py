# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        res: ListNode = ListNode(0)
        res.next = head
        index: int = 1
        prev: ListNode = res
        cur: ListNode = res
        while index <= n:
            if index < m:
                prev = prev.next
                cur = cur.next
            elif index == m:
                cur = cur.next
            else:
                cTmp = cur.next
                pTmp = prev.next
                cur.next = cur.next.next if cur.next and cur.next.next else None
                prev.next = cTmp
                prev.next.next = pTmp
            index += 1
        return res.next
