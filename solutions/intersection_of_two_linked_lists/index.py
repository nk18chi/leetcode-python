# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

from solutions._class.list_node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB:
            A, B = headA, headB
            while A != B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A
