# 430. Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

from solutions._class.node import Node


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def flatten(self, head: 'Node') -> 'Node':
        res: Node = head
        if head is None:
            return None
        if head.child is None:
            self.flatten(head.next)
            return res
        tmp: Node = head.next
        head.next = head.child
        head.child = None
        head.next.prev = head
        newNode: Node = self.flatten(head.next)
        while newNode.next:
            newNode = newNode.next
        if tmp:
            tmp.prev = newNode
        newNode.next = tmp

        return res
