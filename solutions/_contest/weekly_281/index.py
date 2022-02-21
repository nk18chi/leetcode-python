from typing import Dict, List, Set, Tuple, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def countEven(self, num: int) -> int:
        own: int = 0
        for n in str(num):
            own += int(n)
        if own % 2 == 0:
            return num // 2
        else:
            return math.ceil(num / 2) - 1

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left: Optional[ListNode] = head
        right: Optional[ListNode] = head
        total: int = 0
        right = right.next
        while right is not None:
            if right.val == 0:
                left.val = total
                left.next = right
                total = 0
                right = right.next
            else:
                if left.val != 0:
                    left = left.next
                total += right.val
                right = right.next
        left.next = right
        return head
