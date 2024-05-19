from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from _class.tree_node import TreeNode


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res: List[str] = ["" for _ in range(len(s))]
        for i, n in enumerate(indices):
            res[n] = s[i]
        return "".join(res)

    def minFlips(self, target: str) -> int:
        intTarget: int = int(target)
        target = str(intTarget)
        if target == "0":
            return 0
        count: int = 0
        for i in range(1, len(target)):
            if target[i - 1] == target[i]:
                count += 1
        return len(target) - count

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res: int = 0

        def dfs(root: TreeNode):
            if root is None:
                return None
            left: Deque[int] = dfs(root.left)
            right: Deque[int] = dfs(root.right)
            if left is None and right is None:
                return deque([1])
            if left is None or right is None:
                d: Deque[int] = left if right is None else right
                while d and d[0] + 1 >= distance:
                    d.popleft()
                if d:
                    for i in range(len(d)):
                        d[i] += 1
                return d
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i] + right[j] > distance:
                        break
                    self.res += 1
            nxt: Deque[int] = deque([])
            while left and right:
                if left[0] < right[0]:
                    nxt.append(left.popleft() + 1)
                else:
                    nxt.append(right.popleft() + 1)
            d = left if left else right
            while d:
                nxt.append(d.popleft() + 1)
            return nxt

        dfs(root)
        return self.res
