# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

from _class.list_node import ListNode


class Solution:
    # # loop twice
    # # Time complexity: O(n + n/2) -> O(n)
    # # Space complexity: O(1)
    # def middleNode(self, head: ListNode) -> ListNode:
    #     length: int = 0
    #     copy: ListNode = head
    #     while copy:
    #         length += 1
    #         copy = copy.next
    #     mid: int = length // 2
    #     while mid > 0:
    #         head = head.next
    #         mid -= 1
    #     return head

    # two pointer
    # Time complexity: O(n/2) -> O(n)
    # Space complexity: O(1)
    def middleNode(self, head: ListNode) -> ListNode:
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
