from typing import List


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        return f'<{self.val}, {self.prev}, {self.next}, {self.child}>'


def createDoublyNode(nums):
    if len(nums) == 0:
        return None
    node: Node = Node(nums[0], None, None, None)
    head: Node = node
    for i in range(1, len(nums)):
        if nums[i - 1] is None and nums[i]:
            head.child = Node(nums[i], None, None, None)
            head = head.child
            continue
        elif nums[i - 1] is None is nums[i] is None:
            head = head.next
            continue
        elif nums[i] is None:
            while head.prev:
                head = head.prev
            continue
        if head.next is None:
            head.next = Node(nums[i], head, None, None)
        head = head.next

    return node


def getFlattenDoublyNode(node):
    res: List[int] = []
    while node and node.val:
        res.append(node.val)
        node = node.next
    return res
