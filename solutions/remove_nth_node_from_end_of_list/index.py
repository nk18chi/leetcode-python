# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

from typing import Optional
from _class.list_node import ListNode


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left: Optional[ListNode] = head
        right: Optional[ListNode] = head
        for _ in range(n):
            right = right.next if right else None
        if left is None:
            return None
        if right is None:
            return left.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
