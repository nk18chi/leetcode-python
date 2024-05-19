from typing import List, Dict


class Node:
    def __init__(self, val, prev=None, next=None, child=None, neighbors=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        self.neighbors = neighbors if neighbors else []

    def __str__(self):
        return f"<{self.val}, {self.prev}, {self.next}, {self.child}>"


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


def createDoublyNeighborNode(arr) -> Node:
    history: Dict[int, Node] = {}
    for i in range(len(arr)):
        if i + 1 not in history:
            history[i + 1] = Node(i + 1)
        for n in arr[i]:
            if n not in history:
                history[n] = Node(n)
            history[i + 1].neighbors.append(history[n])
    return history[1]


def getFlattenDoublyNode(node):
    res: List[int] = []
    while node and node.val:
        res.append(node.val)
        node = node.next
    return res


def getFlattenNeighborNode(node):
    res: List[List[int]] = []
    stack: List[Node] = [node]
    while stack:
        cur: Node = stack.pop()
        if len(res) < cur.val:
            for i in range(cur.val):
                if len(res) < (i + 1):
                    res.append([])
        if len(res[cur.val - 1]) > 0:
            continue
        for n in cur.neighbors:
            res[cur.val - 1].append(n.val)
            stack.append(n)
    return res
