# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

from typing import List, Dict


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
    # # solution1
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     if head is None:
    #         return None
    #     head.next = self.removeElements(head.next, val)
    #     if head.val == val:
    #         return head.next
    #     return head

    # solution2
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        res.next = head

        prev = res
        cur = head
        while cur:
            if cur.val == val:
                while cur and cur.next and cur.next.val == val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return res.next
