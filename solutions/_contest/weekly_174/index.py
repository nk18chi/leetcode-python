from typing import List


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
        except BaseException:
            break

    return tree


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list = []
        for i, m in enumerate(mat):
            list.append((i, sum(m)))
        list.sort(key=lambda x: x[1])
        res = []
        for i in range(k):
            res.append(list[i][0])
        return res

    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2
        dict = {}
        for a in arr:
            dict[a] = dict.get(a, 0) + 1
        d = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        i = 1
        sum = 0
        for v in d:
            sum += v[1]
            if sum >= target:
                return i
            i += 1

    def maxProduct(self, root: TreeNode) -> int:
        self.answer = []

        def helper(self, root):
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                self.answer.append(root.val)
                return root.val
            else:
                left = helper(self, root.left)
                right = helper(self, root.right)
                self.answer.append(root.val + left + right)

                return root.val + left + right

        helper(self, root)
        _max = max(self.answer)
        target = 0
        for a in self.answer:
            target = max(target, a * (_max - a))
        return target % (10**9 + 7)
