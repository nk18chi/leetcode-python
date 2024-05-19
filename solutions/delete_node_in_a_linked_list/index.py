# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/

from _class.list_node import ListNode


class Solution:
    # Time complexit: O(1)
    # Space complexit: O(1)
    def deleteNode(self, node: ListNode):
        node.val, node.next = node.next.val, node.next.next
