# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional
from solutions._class.list_node import ListNode


class Solution:
    # Time complexity: O(Max(N,M))
    # Space complexity: O(Max(N,M))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodeList: Optional[ListNode] = ListNode(0)
        head = nodeList
        total: int = 0
        while l1 or l2 or total:
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0
            node: ListNode = ListNode(total % 10)
            nodeList.next = node
            nodeList = nodeList.next
            total = total // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return head.next
