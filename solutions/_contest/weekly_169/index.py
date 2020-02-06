from typing import List

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true

# Input: words = ["SEND","MORE"], result = "MONEY"
# Output: true
# Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


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


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def check(self, start):
            if self.check_list[start] == 1:
                return False
            val = arr[start]
            self.check_list[start] = 1
            if val == 0:
                return True

            f = False
            if val + start < self.length:
                f = check(self, val + start)
            if not f and 0 <= start - val:
                f = check(self, start - val)

            return f

        self.length = len(arr)
        self.check_list = [0] * self.length
        self.flag = False

        return check(self, start)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getAllNode(self, node):
            if node is None:
                return

            self.list.append(node.val)
            getAllNode(self, node.left)
            getAllNode(self, node.right)

        self.list: List[int] = []
        getAllNode(self, root1)
        getAllNode(self, root2)

        self.list.sort()
        return self.list

    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        ans = []
        if n % 2 == 1:
            n -= 1
            ans.append(0)

        for i in range(1, int(n / 2) + 1):
            ans.append(i)
            ans.append(-i)

        return ans
