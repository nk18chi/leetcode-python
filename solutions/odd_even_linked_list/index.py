# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

from solutions._class.list_node import ListNode


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        oddLast: ListNode = head
        evenLast: ListNode = head.next
        while evenLast and evenLast.next:
            tmp: ListNode = oddLast.next
            oddLast.next = evenLast.next
            evenLast.next = evenLast.next.next
            oddLast.next.next = tmp
            oddLast = oddLast.next
            evenLast = evenLast.next
        return head
