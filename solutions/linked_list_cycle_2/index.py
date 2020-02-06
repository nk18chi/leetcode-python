# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or (not head.next):
            return None
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
