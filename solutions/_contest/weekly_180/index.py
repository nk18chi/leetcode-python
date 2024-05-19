from typing import List, Dict, Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"


def createTreeNode(list):
    from collections import deque

    data = list
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break

    return tree


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createListNode(list):
    from collections import deque

    data = list
    n = iter(data)
    node = ListNode(next(n))
    fringe = deque([node])
    while True:
        head = fringe.popleft()
        try:
            head.next = ListNode(next(n))
            fringe.append(head.next)
        except StopIteration:
            break

    return node


def getValFromListNode(node: ListNode):
    res: List[int] = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row: Set[int] = set()
        col: Set[int] = set()
        for i in range(len(matrix)):
            row.add(min(matrix[i]))
        for i in range(len(matrix[0])):
            li: List[int] = []
            for j in range(len(matrix)):
                li.append(matrix[j][i])
            col.add(max(li))

        # res: List[int] = []
        # for r in row:
        #     if r in col:
        #         res.append(r)
        # return res

        return list(row & col)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        array: List[int] = []

        def dfs(root: TreeNode):
            if root is None:
                return
            dfs(root.left)
            array.append(root.val)
            dfs(root.right)

        dfs(root)

        res: TreeNode = TreeNode(None)

        def helper(list: List, root: TreeNode):
            if len(list) == 0:
                return
            mid: int = len(list) // 2
            root.val = list[mid]
            root.left = helper(list[:mid], TreeNode(None))
            root.right = helper(list[mid + 1 :], TreeNode(None))
            return root

        res = helper(array, res)

        return res

    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        total: List[List[int]] = []
        i: int = 0
        for s, e in zip(speed, efficiency):
            total.append([s * e, e, i])
            i += 1
        sortedArray = sorted(total, key=lambda x: (x[0], x[1]), reverse=True)
        order: List[int] = []
        order.append(sortedArray[0][2])
        minEfficiency: int = sortedArray[0][1]
        i = 1
        while i < k:
            for sa in sortedArray[1:]:
                if minEfficiency >= sa[1]:
                    order.append(sa[2])
                    k += 1
                    break

        return 1
